import streamlit as st

from utils.pdf_reader import extract_text
from agents.requirement_agent import analyze_requirements
from agents.api_agent import generate_api_design
from agents.database_agent import generate_database_design
from agents.risk_agent import generate_risk_analysis
from agents.testcase_agent import generate_test_cases

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

    with st.spinner("Analyzing Requirements..."):
        analysis = analyze_requirements(text)

    st.markdown("Agent completed.")

    st.subheader("Requirement Analysis")
    st.markdown(analysis)

    from agents.userstory_agent import generate_user_stories
    with st.spinner("Generating userstories..."):
        stories = generate_user_stories(text)

    st.subheader("User Stories")
    st.markdown(stories)
    with st.spinner("generating api designs..."):
        api_design = generate_api_design(text)

    st.subheader("API Design")
    st.markdown(api_design)
    with st.spinner("Generating database design..."):
        database_design = generate_database_design(text)

    st.subheader("Database Design")
    st.markdown(database_design)
    with st.spinner("Generating risk analysis..."):
        risk_analysis = generate_risk_analysis(text)

    st.subheader("Risk Analysis")
    st.markdown(risk_analysis)
    with st.spinner("Generating Test Cases..."):
        test_cases = generate_test_cases(text)

    st.subheader("Test Cases")
    st.markdown(test_cases)