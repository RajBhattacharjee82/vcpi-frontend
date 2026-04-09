import streamlit as st

st.title("Tier 2: Variant Diagnostics")
st.caption("Interactive branch for failed activity analysis and root-cause hints")

st.markdown(
    """
    Planned interactions:
    - Filter by failed activity name
    - Compare successful vs failed case paths
    - Show top correlated attributes (for example has_settlement_instructions)
    """
)

selected_activity = st.selectbox(
    "Failed activity",
    options=["Settle Trade", "Confirm with Counterparty", "Validate Data"],
)

st.warning(f"Diagnostics placeholder for activity: {selected_activity}")
st.json(
    {
        "root_cause_hypothesis": "Missing settlement instructions",
        "evidence": "Majority of failed cases have has_settlement_instructions = FALSE",
    }
)
