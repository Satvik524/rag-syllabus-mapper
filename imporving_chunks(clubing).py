import json
import os
import math
import numpy

n=5
for filename in os.listdir("jsons"):
    if filename.endswith(".json"):
        file_path= "jsons/"+filename
        with open(file_path,"r",encoding="utf-8") as f:
            data= json.load(f)
            new_chunks=[]
            num_chunks= len(data["chunks"])
            num_grp= math.ceil(num_chunks/n)
            for i in range(num_grp):
                



