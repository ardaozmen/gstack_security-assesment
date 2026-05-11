"""
SecOps Pipeline Lab — Streamlit UI for LLM-backed step runs.
Run from repo: streamlit run secops/ui/app.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import streamlit as st
import yaml

# -----------------------------------------------------------------------------
# Paths
# -----------------------------------------------------------------------------

UI_DIR = Path(__file__).resolve().parent
SECOPS_ROOT = UI_DIR.parent
MANIFEST_PATH = SECOPS_ROOT / "pipeline" / "orchestrator.manifest.yaml"

# -----------------------------------------------------------------------------
# Theme — elite minimal dark (Streamlit inject)
# -----------------------------------------------------------------------------

THEME_CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Instrument+Sans:wght@400;500;600;700&display=swap');
  html, body, [class*="css"] { font-family: 'Instrument Sans', ui-sans-serif, system-ui, sans-serif; }
  .block-container { padding-top: 2rem; max-width: 1100px; }
  .hero-title {
    font-family: 'Instrument Sans', sans-serif;
    font-weight: 700;
    font-size: 1.65rem;
    letter-spacing: -0.03em;
    color: #f0f3f6;
    margin-bottom: 0.35rem;
  }
  .hero-sub {
    color: #8b949e;
    font-size: 0.95rem;
    margin-bottom: 1.75rem;
    line-height: 1.55;
  }
  .pill {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 500;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    background: #21262d;
    color: #79c0ff;
    border: 1px solid #30363d;
    margin-right: 0.35rem;
    margin-bottom: 0.35rem;
  }
  .card {
    background: linear-gradient(165deg, #161b22 0%, #0d1117 100%);
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 1.15rem 1.25rem;
    margin-bottom: 1rem;
  }
  .metric-label { color: #8b949e; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; }
  .stTabs [data-baseweb="tab-list"] { gap: 8px; border-bottom: 1px solid #30363d !important; }
  div[data-testid="stSidebar"] {
    background: #0d1117;
    border-right: 1px solid #21262d;
  }
  hr { border-color: #21262d !important; }
</style>
"""


def load_manifest() -> dict[str, Any]:
    if not MANIFEST_PATH.exists():
        st.error(f"Manifest bulunamadı: `{MANIFEST_PATH}`")
        st.stop()
    with open(MANIFEST_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_spec_path(step: dict[str, Any]) -> Path:
    rel = step.get("spec", "")
    base = SECOPS_ROOT / "pipeline"
    return (base / rel).resolve()


def read_text(p: Path) -> str:
    if not p.exists():
        return f"(Dosya yok: `{p}`)"
    return p.read_text(encoding="utf-8")


def parse_gate_marker(text: str) -> tuple[str, str]:
    """Extract <!-- GATE: PASS|WARNING|FAIL --> and strip from display body."""
    m = re.search(r"<!--\s*GATE:\s*(PASS|WARNING|FAIL)\s*-->", text, re.I)
    status = (m.group(1).upper() if m else "PASS")
    body = re.sub(r"<!--\s*GATE:\s*(PASS|WARNING|FAIL)\s*-->\s*", "", text, flags=re.I).strip()
    return status, body


def build_system_prompt() -> str:
    return """You are a senior SecOps analyst executing one pipeline skill only.
Output MUST be valid Markdown for the artifact(s) requested.
End your response with EXACTLY one line (HTML comment) on its own line:
<!-- GATE: PASS --> or <!-- GATE: WARNING --> or <!-- GATE: FAIL -->
Choose FAIL only if mandatory sections are impossible from the given context.
Be concise but professional; use tables and bullet lists where appropriate.
Do not invent secrets, credentials, or real customer data."""


def run_skill_step(
    *,
    api_key: str,
    model: str,
    step_no: int,
    step_id: str,
    command: str,
    spec_text: str,
    gate_name: str,
    outputs: list[str],
    project_context: str,
    prior_artifacts: dict[str, str],
) -> tuple[str, str, str]:
    from openai import OpenAI

    prior_summary = ""
    if prior_artifacts:
        chunks = []
        for name, body in prior_artifacts.items():
            snippet = body[:6000] + ("\n… [truncated]" if len(body) > 6000 else "")
            chunks.append(f"### Prior artifact: `{name}`\n{snippet}")
        prior_summary = "\n\n".join(chunks)

    user_msg = f"""## Pipeline step {step_no}: `{command}` ({step_id})

### Skill specification
{spec_text}

### Quality gate name
{gate_name}

### Expected output filenames
{", ".join(outputs)}

### Project context (user-provided)
{project_context}

### Previously produced artifacts (may be empty)
{prior_summary}

Produce Markdown content for the primary deliverable(s). If multiple files are listed,
use clear headings like `## File: FILENAME` before each file's body.
Remember the final gate line: <!-- GATE: PASS|WARNING|FAIL -->"""

    client = OpenAI(api_key=api_key)
    resp = client.chat.completions.create(
        model=model,
        temperature=0.2,
        messages=[
            {"role": "system", "content": build_system_prompt()},
            {"role": "user", "content": user_msg},
        ],
    )
    raw = (resp.choices[0].message.content or "").strip()
    gate_status, body = parse_gate_marker(raw)
    return gate_status, body, raw


def init_session() -> None:
    if "artifacts" not in st.session_state:
        st.session_state.artifacts = {}
    if "run_log" not in st.session_state:
        st.session_state.run_log = []
    if "last_mode" not in st.session_state:
        st.session_state.last_mode = "full"


def main() -> None:
    st.set_page_config(
        page_title="SecOps Pipeline Lab",
        page_icon="◆",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    init_session()
    st.markdown(THEME_CSS, unsafe_allow_html=True)

    manifest = load_manifest()
    modes = manifest.get("modes", {})
    catalog = manifest.get("step_catalog", {})

    # Sidebar
    with st.sidebar:
        st.markdown("### Credentials")
        api_key = st.text_input(
            "OpenAI API key",
            type="password",
            placeholder="sk-…",
            help="Stored only in this browser session (Streamlit session state).",
        )
        model = st.selectbox(
            "Model",
            ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo"],
            index=0,
        )
        st.markdown("---")
        st.markdown("### Execution")
        mode = st.selectbox(
            "Mode",
            ["full", "fast", "compliance"],
            index=["full", "fast", "compliance"].index(st.session_state.last_mode)
            if st.session_state.last_mode in ("full", "fast", "compliance")
            else 0,
        )
        st.session_state.last_mode = mode
        clear_btn = st.button("Clear artifacts & log")

    if clear_btn:
        st.session_state.artifacts = {}
        st.session_state.run_log = []
        st.rerun()

    # Hero
    st.markdown(
        '<p class="hero-title">SecOps Pipeline Lab</p>'
        '<p class="hero-sub">LLM-backed evaluation against your machine-readable '
        "orchestrator manifest and class-based skill specs. Expert console — minimal noise.</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<span class="pill">orchestrator.manifest.yaml</span>'
        '<span class="pill">skills/specs/*.spec.md</span>'
        '<span class="pill">quality gates</span>',
        unsafe_allow_html=True,
    )
    st.markdown("")

    col_a, col_b = st.columns([2, 1])
    with col_a:
        project_context = st.text_area(
            "Project context",
            height=220,
            placeholder="Name, one-line purpose, environment (cloud/on-prem), regulated sector (e.g. banking), integrations, go-live target…",
        )
    with col_b:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="metric-label">Active mode</p>', unsafe_allow_html=True)
        st.markdown(f"**{mode}** → steps `{modes.get(mode, {}).get('steps', [])}`")
        st.markdown('<p class="metric-label">Manifest</p>', unsafe_allow_html=True)
        try:
            st.caption(str(MANIFEST_PATH.relative_to(SECOPS_ROOT)))
        except ValueError:
            st.caption(str(MANIFEST_PATH))
        st.markdown("</div>", unsafe_allow_html=True)

    run = st.button("Run pipeline", type="primary", width="stretch")

    step_numbers: list[int] = modes.get(mode, {}).get("steps", [])
    if not step_numbers:
        st.warning("Mod için adım tanımı yok.")
        st.stop()

    if run:
        if not api_key or not api_key.strip():
            st.error("OpenAI API anahtarı girin (sidebar).")
            st.stop()
        if not project_context.strip():
            st.error("Project context alanı boş olamaz.")
            st.stop()

        st.session_state.run_log = []
        progress = st.progress(0.0)
        status_ph = st.empty()

        for idx, step_no in enumerate(step_numbers):
            step_key = str(step_no)
            step = catalog.get(step_key)
            if not step:
                st.session_state.run_log.append({"step": step_no, "status": "SKIP", "detail": "Unknown step"})
                continue

            step_id = step.get("id", "")
            command = step.get("command", "")
            spec_path = resolve_spec_path(step)
            spec_text = read_text(spec_path)
            outputs = step.get("outputs", [])
            gate_name = step.get("gate", "")

            status_ph.markdown(f"**Running** `{command}` — _{step_id}_ …")

            try:
                gate_status, body, raw = run_skill_step(
                    api_key=api_key.strip(),
                    model=model,
                    step_no=step_no,
                    step_id=step_id,
                    command=command,
                    spec_text=spec_text,
                    gate_name=gate_name,
                    outputs=outputs,
                    project_context=project_context,
                    prior_artifacts=dict(st.session_state.artifacts),
                )
            except Exception as e:
                st.session_state.run_log.append(
                    {"step": step_no, "command": command, "status": "ERROR", "detail": str(e)}
                )
                st.error(f"Step {step_no} failed: {e}")
                progress.progress((idx + 1) / len(step_numbers))
                break

            # Store primary output under first filename
            primary_name = outputs[0] if outputs else f"STEP_{step_no}.md"
            st.session_state.artifacts[primary_name] = body

            st.session_state.run_log.append(
                {
                    "step": step_no,
                    "command": command,
                    "gate": gate_status,
                    "output": primary_name,
                }
            )

            progress.progress((idx + 1) / len(step_numbers))

            if gate_status == "FAIL":
                st.warning(f"Gate **FAIL** at step {step_no} (`{command}`). Pipeline stopped.")
                break

        status_ph.markdown("**Idle** — last run complete.")

    # Results
    if st.session_state.run_log:
        st.markdown("---")
        st.markdown("### Run summary")
        st.dataframe(st.session_state.run_log, width="stretch", hide_index=True)

    if st.session_state.artifacts:
        st.markdown("---")
        st.markdown("### Artifacts")
        names = sorted(st.session_state.artifacts.keys())
        tabs = st.tabs(names)
        for tab, name in zip(tabs, names):
            with tab:
                st.markdown(st.session_state.artifacts[name])


if __name__ == "__main__":
    main()
