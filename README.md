# GCE
#  Farouq (فاروق) — Jordanian News Fact-Checking Platform

Farouq is a Streamlit web app that helps users verify news claims, with a focus on Jordanian sources. The user enters a news claim or headline, the app searches trusted sources on the web, and an LLM analyzes the evidence and returns a verdict with its reasoning and references.

##  Features

- Claim verification: enter a news item or claim and get an analysis based on live search results
- Focus on Jordanian news sources
- Clear verdict with explanation and links to the sources used
- Arabic-friendly interface
- Simple web UI built with Streamlit

##  How It Works

1. The user submits a claim.
2. **Tavily** searches the web for relevant articles from trusted sources.
3. The results are passed to an LLM through **OpenRouter** (or OpenAI).
4. The LLM compares the claim with the evidence and returns a verdict with an explanation.
5. The result is displayed in the Streamlit interface.

##  Tech Stack

| Component | Technology |
|-----------|------------|
| Interface | Streamlit |
| Web search | Tavily API |
| LLM | OpenRouter / OpenAI |
| Language | Python 3.10+ |
| Config | python-dotenv |

##  Project Structure

GCE/
├── README.md
└── Farouq_fixed/
    ├── app.py              # Streamlit entry point
    ├── intent_router.py    # Detects the intent of the user's input
    ├── router.py           # Routes the request to the right handler
    ├── verificator.py      # Claim verification logic
    ├── llm_call.py         # LLM calls (OpenRouter / OpenAI)
    ├── Data/
    │   └── config.py       # Loads settings and API keys from .env
    ├── requirements.txt
    ├── README_AR.md        # Arabic README
    └── .env                # API keys (not committed)
```

.

##  Installation

```bash
git clone https://github.com/<USERNAME>/<REPO>.git
cd <REPO>
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

##  Configuration

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_key
OPENROUTER_API_KEY=your_openrouter_key
```

Never commit `.env` to GitHub. Make sure it is listed in `.gitignore`.

##  Running the App

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

##  Disclaimer

Farouq is an AI-assisted tool. Its results depend on available online sources and the language model, and they may be inaccurate. Always double-check important claims with official sources.

##  Future Work

- Support more Jordanian and Arab news sources
- Save verification history
- Add confidence scores for each verdict

##  Author

Mohmmad Alhmoud — Data Science & AI, Yarmouk University
