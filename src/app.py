import streamlit as st

from api.client import get_health
from components.status_badge import status_badge

st.set_page_config(page_title="VCPI Accelerator", layout="wide")

st.title("VC Process Intelligence Accelerator")
st.caption("Streamlit frontend for discovery, diagnostics, and predictive monitoring")

left, right = st.columns([2, 1])

with left:
    st.markdown(
        """
        This UI is organized around your hackathon roadmap:
        - Tier 1: Event ingestion + process visibility
        - Tier 2: Variant diagnostics
        - Tier 3: Live risk predictions + copilot hints
        """
    )

with right:
    try:
        health = get_health()
        status_badge("Backend", health.get("status", "unknown"))
    except Exception as exc:
        status_badge("Backend", "offline")
        st.error(f"Backend check failed: {exc}")

st.info("Use the left sidebar to open each feature page.")
