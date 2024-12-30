import os
import google.generativeai as genai
import torch
from dotenv import load_dotenv
load_dotenv()

def embedd(chunks):
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=chunks)
    print(result)
    tensor = torch.tensor(result['embedding'], dtype=torch.float32)
    return tensor

def response(matching_chunks, query):
    context = "\n".join(matching_chunks)
    input_prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"

    # Generate response
    llm = genai.GenerativeModel('gemini-1.5-flash')
    response = llm.generate_content(input_prompt)

    print(response.text)
    return response.text