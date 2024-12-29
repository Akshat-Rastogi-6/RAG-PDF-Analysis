from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_(resume_text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = splitter.split_text(resume_text)
    return chunks