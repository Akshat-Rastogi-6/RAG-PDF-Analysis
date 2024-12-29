from PyPDF2 import PdfReader
from chunk import chunk_
from store_embedding import search_embeddings, store_embeddings
from embeddings import embedd, response

def pdfanalyze(file, query):
    reader = PdfReader(file)
    resume_text = " ".join([page.extract_text() for page in reader.pages])
    chunks = chunk_(resume_text)
    embeddings = embedd(chunks)
    index = store_embeddings(embeddings)

    query_embedding = embedd(query)
    result = search_embeddings(query_embedding, index, chunks)
    resp = response(result, query)
    return resp