# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controllers.GetData import getListOfNseCompanies

app = FastAPI()

origins = [
    "http://localhost:5173",  # SvelteKit dev server
    "http://127.0.0.1:5173",
    "http://localhost:3000",  # optional, for other setups
    "http://yourdomain.com"   # your deployed frontend (for production)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # <- Frontend URLs allowed
    allow_credentials=True,
    allow_methods=["*"],              # <- Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # <- Allow all headers
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/nse")
def nseCompanies():
    return getListOfNseCompanies()