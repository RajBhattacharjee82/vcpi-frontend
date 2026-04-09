import pandas as pd
import streamlit as st

from api.client import upload_preview

st.title("Tier 1: Process Discovery")
st.caption("Upload event log and inspect structure before persistence")

uploaded = st.file_uploader("Upload CSV/XLSX event log", type=["csv", "xlsx", "xls"])

if uploaded is not None:
    with st.spinner("Previewing file via backend..."):
        result = upload_preview(uploaded.name, uploaded.getvalue())

    st.success(f"Rows detected: {result['rows']}")
    st.write("Columns", result["columns"])

    preview_df = pd.DataFrame(result["preview"])
    st.dataframe(preview_df, use_container_width=True)
