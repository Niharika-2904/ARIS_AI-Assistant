from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load env variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("models/gemini-1.5-flash")


# FastAPI app
app = FastAPI()
templates = Jinja2Templates(directory="templates")


# serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/generate", response_class=HTMLResponse)
async def generate(request: Request, prompt: str = Form(...)):
    response = "Error generating response."
    try:
        result = model.generate_content(prompt)
        response = result.text
    except Exception as e:
        response = f"Error: {str(e)}"
    return templates.TemplateResponse("index.html", {"request": request, "response": response, "prompt": prompt})
