import streamlit as st
from streamlit_mermaid import st_mermaid
from utils.pdf_reader import extract_text
from workflow.orchestrator import run_workflow
from utils.report_generator import generate_report
st.set_page_config(page_title="Enterprise AI Architect")

st.title("Enterprise AI Architect Agent")

uploaded_file = st.file_uploader(
    "Upload Requirement PDF",
    type=["pdf"]
)

if uploaded_file:

    st.success("PDF Uploaded Successfully")

    text = extract_text(uploaded_file)

    st.subheader("Requirement Content")
    st.markdown(text)

    st.markdown("Calling AI Agent...")

    

    results = run_workflow(text)
    st.subheader("Requirement Analysis")
    st.markdown(results["requirements"])

    st.subheader("User Stories")
    st.markdown(results["stories"])

    st.subheader("API Design")
    st.markdown(results["api"])
    st.subheader("Architecture Diagram")

    st.code(
        results["architecture"],
        language="text"
    )
    st_mermaid(results["architecture"])
    
    pdf_file = generate_report(results)
    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download Enterprise Report",
            data=file,
            file_name=pdf_file,
            mime="application/pdf"
        )