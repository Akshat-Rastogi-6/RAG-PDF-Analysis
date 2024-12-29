import faiss
import numpy as np

def store_embeddings(tensor):
    embeddings = np.array([embedding.cpu().numpy() for embedding in tensor])

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])  # L2 similarity
    index.add(embeddings)

    # Save the FAISS index
    faiss.write_index(index, r"data\vectors\resume_index.faiss")
    return index

def search_embeddings(query_embedding, index, chunks):
    k = 3  # Number of top results
    query_embedding_array = np.expand_dims(np.array(query_embedding, dtype='float32'), axis=0)

    # Perform the FAISS search
    distances, indices = index.search(query_embedding_array, k)

    # Retrieve matching chunks
    matching_chunks = [chunks[i] for i in indices[0]]

    return matching_chunks