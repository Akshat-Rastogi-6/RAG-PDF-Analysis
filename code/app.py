import streamlit as st

from analyze import pdfanalyze

def main():
    st.title("PDF Analysis Tool")
    
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

def analyze_pdf(file, query):
    data = pdfanalyze(file, query)
    return data


if __name__ == "__main__":
    main()