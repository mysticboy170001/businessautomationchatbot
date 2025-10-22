from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load knowledge base
with open("data/kb.json", "r", encoding="utf-8") as f:
    KB = json.load(f)

class Query(BaseModel):
    query: str

@app.post("/chat")
def chat(query: Query):
    q = query.query.lower()
    # Simple matching search
    for item in KB:
        if any(keyword in q for keyword in item["keywords"]):
            return {"answer": item["answer"]}
    return {"answer": "Sorry, I don't have information about that yet."}

@app.get("/")
def root():
    return {"message": "Chatbot backend is running!"}
