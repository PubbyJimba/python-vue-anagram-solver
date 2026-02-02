# Anagram Solver 2

A full-stack Anagram Solver built with **FastAPI** (Python) and **Vue.js** (Vite).

## Project Structure
- `backend/`: FastAPI application and dictionary file.
- `frontend/`: Vue.js frontend application.

## Prerequisites
- **Python 3.9+**
- **Node.js 18+** and **npm**

## Setup Instructions

### 1. Backend Setup
1. Navigate to the root directory.
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
5. Start the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```
   The API will be running at `http://127.0.0.1:8000`.

### 2. Frontend Setup
1. Open a new terminal window and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be running at the URL shown in the terminal (typically `http://localhost:5173`).

## Usage
1. Open the frontend URL in your browser.
2. Enter up to 7 letters in the search bar.
3. Click **Solve** to see all possible anagrams from the dictionary.

## Dictionary
The solver uses a dictionary of over 50,000 words located at `backend/dictionary.txt`.
