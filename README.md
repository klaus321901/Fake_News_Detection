 # 🔎 TRUTHLENS
_AI-Powered Real-Time Fact Checker_

_A fact-checking application built with FastAPI, Google Gemini API, and SerpAPI_

---

## 📖 Project Description

✨ **Problem Statement:**  
Manual fact-checking is too slow to keep up with the viral spread of misinformation. While automated detectors exist, they often lack context, nuance, and transparency, leaving users with verdicts but no explanation. The challenge is to build a system that enables individuals to quickly verify whether online news is real or fake in real time, with evidence and reasoning.

💡 **Proposed Solution:**  
Our project verifies textual claims in real-time by combining:  
- **SerpAPI** for retrieving live web evidence.  
- **Gemini 2.5 Pro** for structured reasoning.  
- **FastAPI backend** for claim preprocessing and orchestration.  
- **Angular frontend** for a simple, interactive interface.  

The system outputs:  
- Final Verdict (REAL / FAKE / UNKNOWN)  
- Confidence Score (0–100)  
- Reasoning (explanation of result)  
- Evidence (supporting snippets)  
- Warnings (weak or contradictory context)  

🎯 **Target Users / Use Cases:**  
- Journalists verifying breaking news.  
- Social media platforms moderating misinformation.  
- Students and researchers validating claims.  
- Citizens checking suspicious news or viral content.  

---

## 🔬 Methodology

- **Research & Ideation** – Studied misinformation, NLP techniques, and APIs.  
- **Design** – Created system architecture (Angular frontend + FastAPI backend + external APIs).  
- **Develop** – Implemented claim ingestion, context retrieval, reasoning, and structured output.  
- **Test** – Unit and integration testing with real/fake claims.  
- **Deploy** – Local deployment using FastAPI + Angular.  
- **Future Scope** – Multilingual support, caching, multiple APIs (Bing, NewsAPI), and analytics dashboard.  

---

## 👥 Team Details

**Team Name:** [Add Your Team Name Here]

| Name           | Role            | Email               |
|----------------|-----------------|---------------------|
| Sana Tasneem   | Team Lead       | sanatasneem@gmail.com|
| Yasmeen Begum  | Backend Dev     | member2@example.com |
| Amtul Jameel   | Frontend Dev    | member3@example.com |

---

## 🛠️ Technology Stack

- **Frontend:** Angular 16 (TypeScript, HTML5, SCSS)  
- **Backend:** Python 3.11, FastAPI, Uvicorn  
- **AI Model:** Gemini 2.5 Pro (Google Generative AI SDK)  
- **Web Search API:** SerpAPI  
- **Other Tools:** VS Code, Postman, Browser DevTools  

---

## 📹 Demonstration Video
▶️ [Add Video Link Here]

---

## 🌐 Deployment

This project has not been deployed online. To run locally:

## 1. Clone the repository
   ```
   git clone https://github.com/<your-username>/Fake_News_Detection.git
   cd Fake_News_Detection
```
   
## 2. Create a virtual environment & install dependencies
   
```
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt

```

## 3. Add API keys
Create a .env file with:
```
GEMINI_API_KEY=your-gemini-api-key
SERPAPI_API_KEY=your-serpapi-api-key
```

## 4. Run the backend
```
uvicorn main2:app --reload

Backend will run at: http://127.0.0.1:8000
```

## 5. Run the frontend
```
cd fact-chex
npm install
ng serve

Frontend will run at: http://localhost:4200
```
## 📚 References

1. Shu, K., Sliva, A., Wang, S., Tang, J., & Liu, H. (2017). Fake News Detection on Social Media: A Data Mining Perspective. ACM SIGKDD Explorations Newsletter, 19(1), 22-     36.
   https://doi.org/10.1145/3137597.3137600

2. Zhou, X., & Zafarani, R. (2020). A Survey of Fake News: Fundamental Theories, Detection Methods, and Opportunities. ACM Computing Surveys, 53(5), 1–40.
   https://doi.org/10.1145/3395046

3. Google AI. Gemini LLM Documentation.
   https://ai.google.dev

## 🖼️ Assets / Screenshots

<img src="https://github.com/klaus321901/Fake_News_Detection/blob/69e536ae00c9036d674f785420eb76f65d2de904/Problem%20Statement.png" width="700"/>

<img src="https://github.com/klaus321901/Fake_News_Detection/blob/d96297c8546308fb61f7e322ed42c5004e3cd7b8/Problem%20Statement%20(1).png" width="700"/>

<img src="https://github.com/klaus321901/Fake_News_Detection/blob/d96297c8546308fb61f7e322ed42c5004e3cd7b8/Problem%20Statement%20(2).png" width="700"/>










