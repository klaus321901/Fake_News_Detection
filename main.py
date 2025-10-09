

import re
import requests
import google.generativeai as genai
import json
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --------------------------
# Setup
# --------------------------
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Hello Vercel"}

# --------------------------
# CORS Middleware
# --------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------
# Pydantic Models
# --------------------------
class ClaimRequest(BaseModel):
    claim: str

# --------------------------
# Step 1: Claim Preprocessing
# --------------------------
def preprocess_claim(claim: str) -> str:
    claim = claim.strip()
    claim = re.sub(r'\s+', ' ', claim)
    claim = re.sub(r'[“”]', '"', claim)
    claim = re.sub(r"[‘’]", "'", claim)
    claim = re.sub(r"[?]+$", "", claim)
    return claim

# --------------------------
# Step 2: Web Search Context Retrieval
# --------------------------
def get_context(claim: str) -> str:
    print("Fetching context from SerpAPI...")
    url = f"https://serpapi.com/search.json?q={claim}&api_key={SERPAPI_API_KEY}&num=6"
    try:
        response = requests.get(url, timeout=10)
        print("SerpAPI raw response:", response.text)
        response.raise_for_status()
        results = response.json().get("organic_results", [])
        snippets = []
        for result in results:
            snippet = result.get("snippet", "").strip()
            if snippet and len(snippet) > 20 and not snippet.endswith("..."):
                snippets.append(f"- {snippet}")
        # Only use the top 3 most relevant snippets
        return "\n".join(snippets[:3])
    except Exception as e:
        print(f"[ERROR] SerpAPI failed: {e}")
        return ""

# --------------------------    
# Step 3: Structured Prompt for Gemini
# --------------------------
def build_structured_prompt(claim: str, context: str) -> str:
    return f"""
You are a fact-checking assistant.

Your task is to verify the truthfulness of a claim using context from live web search results. Base your reasoning only on the context provided.

⚠️ Note: Some snippets may contain unverified or contradictory information. Prioritize clear, reliable, and confirmed statements over vague or conflicting ones.

Return your answer in the following format:

Final Verdict: <REAL / FAKE / UNKNOWN>
Score: <0 to 100 — how confident you are the claim is true>
Reasoning: <Explain your answer using the evidence.>
Evidence: <Cite specific statements from the context.>
Warnings (if any): <Mention if context is weak, outdated, or conflicting.>

Claim:
"{claim}"

Context:
{context}
""".strip()


# --------------------------
# Step 4: Gemini API Call
# --------------------------
def gemini_fact_check(claim: str, context: str) -> dict:
    prompt = build_structured_prompt(claim, context)
    print("[Gemini] Prepared prompt:")
    print(prompt)
    model = genai.GenerativeModel("gemini-2.5-Pro")

    generation_config = genai.types.GenerationConfig(
        temperature=0.2,  # LOW temperature for factual accuracy
        top_p=1.0,
        top_k=40,
        max_output_tokens=512
    )

    try:
        import time
        print("[Gemini] Sending request to Gemini API...")
        start = time.time()
        response = model.generate_content(prompt, generation_config=generation_config)
        elapsed = time.time() - start
        print(f"[Gemini] Response received in {elapsed:.2f} seconds.")
        return parse_structured_output(response.text.strip())
    except Exception as e:
        print(f"[Gemini] API call failed: {e}")
        return {
            "verdict": "UNKNOWN",
            "score": "0",
            "reasoning": "Gemini API call failed.",
            "evidence": "",
            "warnings": str(e)
        }


# --------------------------
# Step 5: Parse Structured Output
# --------------------------
def parse_structured_output(output: str) -> dict:
    fields = {
        "Final Verdict": "",
        "Score": "",
        "Reasoning": "",
        "Evidence": "",
        "Warnings": ""
    }
    current = None
    for line in output.splitlines():
        line = line.strip()
        for key in fields:
            if line.startswith(key + ":"):
                current = key
                fields[key] = line[len(key) + 1:].strip()
                break
        else:
            if current:
                fields[current] += " " + line
    return {
        "verdict": fields["Final Verdict"],
        "score": fields["Score"],
        "reasoning": fields["Reasoning"],
        "evidence": fields["Evidence"],
        "warnings": fields["Warnings"]
    }

# --------------------------
# Final Pipeline Function
# --------------------------
def fact_check_pipeline(claim: str) -> dict:
    print(f"\n🧠 Claim: {claim}")
    claim = preprocess_claim(claim)
    context = get_context(claim)
    if not context:
        result = {
            "verdict": "UNKNOWN",
            "score": "0",
            "reasoning": "No context available from web.",
            "evidence": "",
            "warnings": "Web search failed or returned no useful data."
        }
    result = gemini_fact_check(claim, context)
    print(json.dumps(result, indent=2))
    return result

@app.post("/fact-check")
async def fact_check_endpoint(request: ClaimRequest):
    return fact_check_pipeline(request.claim)
