# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controllers.GetData import getListOfNseCompanies
import os

app = FastAPI()

origins = ["*"]


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
    
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("app:app", host="127.0.0.1", port=port)
