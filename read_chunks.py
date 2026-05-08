import requests
import json
import os
import pandas as pd
import time
import numpy as np
import joblib

def create_embeddings(text_list):
    # Sends a batch of text to Ollama
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list
    })

    embeddings = r.json().get("embeddings") 
    return embeddings

my_dict = []
jsons = os.listdir("jsons")
chunk_id = 0

for json_file in jsons:
    # It's good practice to skip non-json files (like .DS_Store on Mac)
    if not json_file.endswith(".json"):
        continue

    with open(f"jsons/{json_file}") as f:
        content = json.load(f)
    
    # Generate embeddings for all chunks in the file at once
    start= time.time()
    embeddings = create_embeddings([c["text"] for c in content["chunks"]])
    end= time.time()
    print("created embeddings of {json_file} in ",end-start,"s")
    
    # FIX 2: Added enumerate() to get both the index 'i' and the 'chunk' object
    for i, chunk in enumerate(content["chunks"]):
        chunk["chunk_id"] = chunk_id
        chunk_id += 1
        # Assign the specific embedding corresponding to this chunk
        chunk["embeddings"] = embeddings[i]
        my_dict.append(chunk)
        
    #break # Stops after the first file (remove this when ready to run all)

df= pd.DataFrame.from_records(my_dict)
# Saving the dataframe
joblib.dump(df,"embeddings.joblib")
