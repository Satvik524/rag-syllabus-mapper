IMPORTANT:
    1. in terminal write 'ollam serve' to activate it so that you can use ollama
    2. I have created an conda environment for this project named RAG which have many downloads
        like whisper, ollama, ollama3.2 etc


IN THIS PROJECT WE HAVE LEARNED TO :

        1. Download videos from terminal using a youtube playlist link through terminal 
            directly into the folder

        2. Converting the video into audio using ffmpeg

        3. Converting audio to text (translation if needed) using 'WHISPER'

        4. We then created chunks which contained video title, video number, start, end time stamp
            and text at that time stamp
        5. Create embeddings/vector of the text using 'OLLAMA'

        5.5. saving the dataframe using joblib

        6. Using cosine similarity and getting the top 5 result

        7. Creating a prompt for the llm model of your choice which contains context
            some data and that top 5 result so that llm can give you a structured ans

        For LLM i used ollama3.2 it is 1gb in size and give decent response with good speed
        ofcourse you can scale it up using paid api 

