import streamlit as st

st.set_page_config(
    page_title="Documentation Quality Checker",
    page_icon="📝",
    layout="wide"
)

st.title("Documentation Quality Checker")

st.write(
    "An automated tool to improve the quality, "
    "consistency and readability of technical documentation."
)

uploaded_file = st.file_uploader(
    "Upload your documentation",
    type=["md", "txt"]
)

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")

    st.subheader("Document Preview")
    st.text_area("Content", content, height=300)

    st.success("Document uploaded successfully!")