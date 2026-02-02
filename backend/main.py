from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .solver import AnagramSolver
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Initialize solver with the dictionary
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_PATH = os.path.join(BASE_DIR, "dictionary.txt")

solver = AnagramSolver(DICTIONARY_PATH)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Anagram Solver API"}

@app.get("/solve/{letters}")
def solve_anagram(letters: str):
    # Simple validation to allow only alphabetic characters
    if not letters.isalpha():
         raise HTTPException(status_code=400, detail="Input must contain only letters")
    if len(letters) > 7:
        raise HTTPException(status_code=400, detail="Input must contain 7 or fewer letters")

    anagrams = solver.solve(letters)
    return {"letters": letters, "anagrams": anagrams}
