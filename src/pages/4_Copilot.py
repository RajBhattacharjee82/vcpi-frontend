import streamlit as st

st.title("Bonus: Co-pilot Recommendations")
st.caption("Natural language guidance when risk is high")

st.markdown(
    """
    This panel can be wired to your backend recommendation table.

    Example output:
    "This trade has a high probability of failing settlement because counterparty instructions are missing.
    Please contact the back office to update SSIs now."
    """
)

error_type = st.selectbox(
    "Error category",
    ["SETTLEMENT_BREAK", "MISSING_INSTRUCTIONS", "COUNTERPARTY_TIMEOUT"],
)

if st.button("Generate recommendation"):
    st.success(
        f"[{error_type}] Suggested next step: Send an immediate SSI completion request and hold settlement confirmation until updated."
    )
