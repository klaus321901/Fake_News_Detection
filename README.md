# 📰 Fake News Detection

A fact-checking application built with FastAPI, Google Gemini API, and SerpAPI.
It accepts a claim, fetches live evidence from the web, and processes it for analysis.
Gemini then evaluates the context to return a verdict with reasoning, confidence score, and supporting evidence.
---

##  Features
- Accepts a claim as input (via API or frontend).  
- Fetches live web search results using **SerpAPI**.  
- Cleans and normalizes the claim text.  
- Passes evidence snippets into **Gemini 1.5 Flash** for structured reasoning.  
- Returns a structured verdict:

Final Verdict: REAL / FAKE / UNKNOWN
Score: Confidence (0–100)
Reasoning: Explanation of why
Evidence: Context snippets
Warnings: Weak/contradictory info if any

---

##  Project Structure
```text
.
├── main2.py                # FastAPI backend with fact-check pipeline  
├── requirements.txt       # Python dependencies  
├── landing_page/          # (Optional) UI assets / screenshots  
├── search_query_result/   # Stored snippets/screenshots from search  
└── README.md              # Documentation  
```
### 1. Clone the repository
```
git clone https://github.com/<your-username>/fake-news-detection.git
cd fake-news-detection
```
### 2. Create a virtual environment
```
python -m venv .venv
```
### 3. Install dependencies
```
On Windows

.venv\Scripts\activate


On macOS/Linux

source .venv/bin/activate
```
### 4. Clone the repository
```
pip install -r requirements.txt
```

### 5. Create a .env file
```
GEMINI_API_KEY=your-gemini-api-key
SERPAPI_API_KEY=your-serpapi-api-key

```

### 6. Run the backend
```
uvicorn main:app --reload

```
### API will be live at:
```
http://127.0.0.1:8000

```

 ### Example Usage
 ```
curl -X POST "http://127.0.0.1:8000/fact-check" \
-H "Content-Type: application/json" \
-d '{"claim": "The Eiffel Tower is in Paris"}'

```
 ### Sample Response
 ```
{
  "verdict": "REAL",
  "score": "95",
  "reasoning": "Multiple sources confirm the Eiffel Tower is in Paris.",
  "evidence": "- The Eiffel Tower is a landmark in Paris, France.",
  "warnings": ""
}

```
 
### API Endpoints
POST /fact-check   → Takes a claim and returns a fact-check result

### Tech Stack

Python 3.10+

FastAPI (backend framework)

Google Gemini API (fact-check reasoning)

SerpAPI (live web search results)

```
##  Frontend Setup (Angular)

### 1. Navigate to the frontend folder
cd fact-chex

```
###  2.Install dependencies
```
npm install

```
## 3. Run the Angular app
```
ng serve

```
### The frontend will be live at: 
http://localhost:4200

### Backend Setup (FastAPI)
Run the backend
```
uvicorn main2:app --reload
```
### The backend will be live at:
```
http://127.0.0.1:8000

```

### Connecting Frontend & Backend
The Angular frontend (http://localhost:4200) sends requests to the FastAPI backend (http://127.0.0.1:8000/fact-check).

Make sure both frontend and backend are running at the same time.

If needed, update the Angular service file (fact-check.service.ts) with the correct backend URL.
















