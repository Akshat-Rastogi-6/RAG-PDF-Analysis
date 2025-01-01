# PDF Analysis Tool using Retrieval-Augmented Generation (RAG)

This project is designed to perform **pdf analysis** using a **Retrieval-Augmented Generation (RAG)** model. The system extracts relevant information from a pdf in PDF format based on user queries. It uses **FAISS** for efficient vector-based retrieval and **Google's Generative AI Model** for embedding the content.

## Features
- Extracts text content from PDF pdfs.
- Splits pdf content into meaningful chunks.
- Embeds the text chunks using a pre-trained generative model.
- Uses FAISS to build an index of embeddings for fast retrieval.
- Retrieves and displays relevant sections of the pdf based on user queries.

## Requirements

To run this project, you will need the following libraries:

- `PyPDF2` for PDF text extraction
- `langchain` for text splitting
- `google-generativeai` for embeddings from Google's generative model
- `torch` for handling embeddings as tensors
- `faiss` for creating a fast search index
- `numpy` for numerical computations

Install the necessary libraries using pip:

```bash
pip install PyPDF2 langchain google-generativeai torch faiss-cpu numpy psutil
