import streamlit as st
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.analyzer import analyze_code

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="Code Reviewer",
    layout="wide"
)

st.title("AI Bug & Code Reviewer")
st.caption("Powered by NVIDIA: Nemotron 3 Super — Paste your code and get instant feedback")

col1, col2 = st.columns([1, 1])

with col1:
    language = st.selectbox(
        "Programming Language",
        ["Python", "JavaScript", "Java", "C++", "C#", "TypeScript", "Other"]
    )
    code_input = st.text_area(
        "Paste your code here",
        height=400,
        placeholder="def hello():\n    print('Hello World')"
    )
    analyze_btn = st.button("Analyze Code", type="primary", use_container_width=True)

with col2:
    if analyze_btn:
        if not code_input.strip():
            st.warning("Please paste some code first!")
        else:
            with st.spinner("Analyzing your code..."):
                result = analyze_code(code_input, language)

            score = int(result["score"]) if result["score"].isdigit() else 5
            color = "green" if score >= 7 else "orange" if score >= 4 else "red"
            st.markdown(f"### Overall Score: :{color}[{score}/10]")
            st.progress(score / 10)

            if result["bugs"].strip():
                with st.expander("Bugs Found", expanded=True):
                    st.markdown(result["bugs"])

            if result["security"].strip():
                with st.expander("Security Issues", expanded=True):
                    st.markdown(result["security"])

            if result["quality"].strip():
                with st.expander("Code Quality"):
                    st.markdown(result["quality"])

            if result["suggestions"].strip():
                with st.expander("Suggestions"):
                    st.markdown(result["suggestions"])
    else:
        st.info("Paste your code on the left and click Analyze")
