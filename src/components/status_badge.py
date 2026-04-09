import streamlit as st


def status_badge(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div style=\"padding:8px 12px;border:1px solid #d8e2dc;border-radius:10px;background:#f8f9fa;\">
            <strong>{label}</strong>: {value}
        </div>
        """,
        unsafe_allow_html=True,
    )
