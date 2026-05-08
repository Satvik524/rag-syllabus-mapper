import os
import subprocess
lst = os.listdir("videos")


for i in lst:
    # 1. SAFETY CHECK: Skip hidden files or non-mp4 files
#sometimes the computer generates a ghost file for some reason 
    if not i.endswith(".mp4"):
        continue

    # Now it is safe to process
    try:
        tutorial_number_str = i.split(".")[0].split(" #")[1]
        tutorial_number = int(tutorial_number_str)

        if tutorial_number != 0 and tutorial_number != 1:
            file_name = i.split("：")[0].split("video_")[1].split("_")[1]
            print(tutorial_number, file_name)

        else:
            file_name = i.split(" #")[0].split("video_")[1].split("_")[1]
            print(tutorial_number, file_name)
            
    except IndexError:
        print(f"Skipping malformed file: {i}")

    subprocess.run(["ffmpeg","-i",f"videos/{i}",f"audios/{tutorial_number}_{file_name}.mp3"])