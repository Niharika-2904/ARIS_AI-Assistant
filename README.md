# 🌸 Aris — FastAPI + Google Gemini LLM App

## 📋 Overview :-

Aris is a web application built with **FastAPI** and **Google Gemini (LLM)** to generate responses to user prompts.  
It features an attractive web interface built with Bootstrap and serves predictions via FastAPI.


## 🚀 Features :-
✅ FastAPI-based API & web app  
✅ Connects to Google Gemini LLM  
✅ User-friendly HTML GUI  
✅ Version controlled with Git  
✅ Ready for deployment!


## 📂 Project Structure :-

Aris/
├── app.py
├── templates/index.html
├── static/style.css
├── requirements.txt
├── .gitignore
├── .env
└── README.md


## 🔧 Setup & Run Locally :-

### 1️⃣ Clone the repository;

git clone <your-repo-url>
cd AI_Assistant/Aris

### 2️⃣ Create & activate virtual environment;

python -m venv venv
venv\Scripts\activate    # on Windows
source venv/bin/activate # on Linux/Mac

### 3️⃣ Install dependencies;

pip install -r requirements.txt

### 4️⃣ Add your Gemini API Key;

* Create a `.env` file in the `Aris` folder.
* Add:
GEMINI_API_KEY=your_google_gemini_api_key

### 5️⃣ Run the app;

uvicorn app:app --reload


## 🌐 Deployment :-

You can deploy on platforms like **Render**:

* Push your code to GitHub.
* Create a new web service on Render.
* Set up environment variables.
* Done!


## 📝 Tech Stack :-

* ⚡ **FastAPI** — backend web framework
* 🌸 **Jinja2** — HTML templating
* 🤖 **Google Gemini LLM** — AI text generation
* 🎨 **HTML/CSS** — frontend styling
* 📦 **Uvicorn** — ASGI server with hot-reload

## Author :-

NIHARIKA SAXENA 





