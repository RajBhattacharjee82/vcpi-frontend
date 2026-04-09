import streamlit as st

from api.client import create_prediction

st.title("Tier 3: Live Monitoring")
st.caption("Predict failure probability for in-flight cases")

with st.form("prediction_form"):
    case_id = st.text_input("Case ID", value="T1002")
    has_instructions = st.toggle("Has settlement instructions", value=False)
    submitted = st.form_submit_button("Get Risk Score")

if submitted:
    payload = {
        "case_id": case_id,
        "has_settlement_instructions": has_instructions,
    }
    result = create_prediction(payload)

    st.metric("Failure Probability", f"{result['failure_probability']:.2%}")
    st.info(result["root_cause_hint"])
