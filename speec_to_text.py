import whisper
import time
import json
import os
#model= whisper.load_model("large-v2") to convert non_english speech to english
# result= model.transcribe(audio="audios/filename",
#                          language="hi",
#                          task="translate")
# print(result['text'])
# but warn you that this will take a long time and use alot of cpu

audios = os.listdir("audios")
model = whisper.load_model("base")

for i in audios:
    if i.endswith(".mp3"):
        try:
            title = i.split(".")[0].split("_")[1]
            number = i.split("_")[0]
            
            print(f"Transcribing {i}...")
            
            result = model.transcribe(audio=f"audios/{i}", fp16=False)
            print(result["segments"])

            chunks = []
            for segment in result["segments"]:
                chunks.append({
                    "No.": number, 
                    "title": title, 
                    "start": segment["start"],
                    "end": segment["end"],
                    "text": segment["text"]
                })
            
            chunks_with_metadata = {"chunks": chunks, "text": result["text"]}
            
            #changing output name to replace .mp3 with .json cleanly
            json_filename = i.replace(".mp3", ".json")
            with open(f"jsons/{json_filename}", "w") as f:
                json.dump(chunks_with_metadata, f, indent=4) # indent=4 makes it readable
                
        except Exception as e:
            print(f"Skipping {i} due to error: {e}")