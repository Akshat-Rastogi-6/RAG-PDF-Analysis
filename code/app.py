import streamlit as st
import google.generativeai as genai
from analyze import pdfanalyze

def main():
    st.title("PDF Analysis Tool")

    gemini_api = st.text_input("Enter your Gemini API key:")
    genai.configure(api_key=gemini_api)

    if gemini_api is not None:
        # File uploader
        uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")
        
        # Text input box
        query = st.text_input("Enter your query")
        
        # Output section
        if uploaded_file and query is not None:
            try:
                # Perform analysis on the uploaded file and query
                output = analyze_pdf(uploaded_file, query)
                st.write("Output:")
                st.markdown(output)
            except Exception as e:
                pass
    elif gemini_api is None:
        st.status("Please enter your Gemini API key to continue.")

def analyze_pdf(file, query):
    data = pdfanalyze(file, query)
    return data


if __name__ == "__main__":
    main()