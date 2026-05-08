from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import requests
import joblib

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })
    embeddings = r.json().get("embeddings") 
    return embeddings

def inference(prompt): # feeding into the LLM
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    response= r.json()
    return response



df= joblib.load("embeddings.joblib")

incoming_query= input("ask a qustion: ")
question_embedding= create_embeddings([incoming_query])[0] #[0] as embeddings is in the first part

similarity= cosine_similarity(np.vstack(df["embeddings"]),[question_embedding])
# we used np.vstack to convert 1d to 2d as cosine_similarity requires 2d input

top_result=5
max_ind= similarity.flatten().argsort()[::-1][0:top_result]
# argsort gives in ascending order's index and [::-1] reverses that and [0:top_result] gets top 5

new_df= df.loc[max_ind]
context_data = new_df[["title", "No.", "start", "end", "text"]].to_json(orient="records")
# orient="records" sorts the value in list of dict format


prompt=f'''
You are a helpful teaching assistant. Use the following video subtitle chunks to answer the user's question.
Each chunk contains: Video Title, Video Number (No.), Start Time, End Time, and Text.

CONTEXT DATA:
{context_data}

USER QUESTION:
{incoming_query}

INSTRUCTIONS:
1. Answer the question based ONLY on the context data above.
2. You must provide the specific "Video Number" and "Start Time" timestamps for where the answer is found.
3. If the user's question is completely unrelated to the provided chunks, politely refuse to answer and ask them to stay on topic. Do not hallucinate an answer.
'''

response= inference(prompt)["response"]
print(response)
with open("response.txt","w") as f:
    f.write(response)
    

