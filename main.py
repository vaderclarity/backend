from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from deep_translator import GoogleTranslator

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now (change later in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslationRequest(BaseModel):
    text: str
    target_language: str

@app.get("/")
def home():
    return {"message": "Healthcare Translation API is running!"}

@app.post("/translate")
def translate_text(request: TranslationRequest):
    try:
        translated_text = GoogleTranslator(source="auto", target=request.target_language).translate(request.text)
        return {"translated_text": translated_text}
    except Exception as e:
        return {"error": str(e)}
