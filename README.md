# RAG Syllabus Mapper

A custom Retrieval-Augmented Generation (RAG) system designed to map university syllabus topics to specific timestamps within YouTube video playlists.

Unlike standard implementations that rely on high-level frameworks like LangChain, this project is built from the ground up to provide a deeper understanding of text chunking, vector embeddings, and similarity-based retrieval.

## 🚀 Features

* **YouTube Content Extraction**: Uses `yt-dlp` to fetch metadata and audio from educational playlists.
* **Local Transcription**: High-accuracy speech-to-text using OpenAI's **Whisper** model.
* **Manual RAG Pipeline**:
* Custom text chunking logic for maintaining context.
* Vectorization using **Scikit-learn**.
* Retrieval based on **Cosine Similarity** to match syllabus topics with transcribed segments.
* 
* **Privacy-First Inference**: Runs local LLMs via **Ollama**, optimized for **Apple Silicon (M1)**.
* **Timeline Mapping**: Generates precise timestamps so you can jump directly to the relevant part of a lecture.

## 🛠 Tech Stack

* **Language:** Python 3.9+
* **Speech-to-Text:** OpenAI Whisper
* **LLM Runner:** Ollama (Local)
* **Data Processing:** Scikit-learn, Joblib
* **Video Handling:** yt-dlp
* **Hardware Optimization:** Metal Performance Shaders (MPS) for Mac M1

## 📂 Project Structure

| File | Description |
| --- | --- |
| `process_video.py` | Handles YouTube playlist downloading and metadata extraction. |
| `speec_to_text.py` | Transcribes audio files into text segments using Whisper. |
| `read_chunks.py` | Initial logic for breaking down long transcripts into chunks. |
| `imporving_chunks.py` | Advanced chunking logic (merging/clubbing) for better context retention. |
| `process_incoming.py` | The main RAG engine that takes a syllabus query and finds the match. |

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Satvik524/rag-syllabus-mapper.git
cd rag-syllabus-mapper

```

### 2. Install Dependencies

```bash
pip install yt-dlp openai-whisper scikit-learn joblib

```

### 3. Setup Ollama

Ensure [Ollama](https://ollama.ai/) is installed on your Mac and pull a model (e.g., Llama 3 or Mistral):

```bash
ollama run llama3

```

## 📝 Usage

1. **Process Videos**: Run `process_video.py` with your target YouTube URL to download audio.
2. **Transcribe**: Use `speec_to_text.py` to convert audio into local JSON transcripts.
3. **Index & Query**: Run `process_incoming.py` and input a topic from your syllabus to find the exact video and timestamp.

## 💡 Why "Manual" RAG?

This project was developed to explore the "black box" of RAG systems. By manually handling the chunking and similarity logic rather than using a wrapper library, the system allows for fine-tuned control over how educational content is indexed and retrieved.

---

*Developed by Satvik Singh*
