import os
from dotenv import load_dotenv
from langchain_classic.schema import HumanMessage, SystemMessage
from llm_call import llm  # استيراد نموذج اللغة الخاص بك
from Data.cleaner import DataCleaner
from Data.tavily_fetcher import TavilyFetcher
from Data.config import TAVILY_API_KEY

load_dotenv()

system_prompt = SystemMessage("""You are "Farooq", an advanced, objective AI assistant specialized in real-time news verification and fact-checking based strictly on the provided official sources and data.
Your primary task is to review input claims, analyze the provided official search evidence, and provide an accurate credibility assessment with neutral reasoning.
Always adhere to strict accuracy, avoid definitive claims when evidence is insufficient, and remain clear and direct in your responses.""")

def verify_claim_with_sources(user_claim: str):
    print(f"[*] Starting verification process for claim: '{user_claim}'\n")

    fetcher = TavilyFetcher()
    raw_data = fetcher.fetch_raw_data(user_claim)

    if not raw_data or not raw_data.get("results"):
        return "عذراً، لم أتمكن من العثور على مصادر رسمية كافية للتحقق من هذا الادعاء حالياً."

    cleaner = DataCleaner()
    cleaned_docs = cleaner.process_tavily_results(raw_data)

    sources_context = ""
    sources_metadata = []

    for idx, doc in enumerate(cleaned_docs, 1):
        sources_context += f"Source [{idx}] Title: {doc['title']}\nURL: {doc['url']}\nContent: {doc['content']}\n\n"
        sources_metadata.append({"title": doc['title'], "url": doc['url']})

    formatted_input = f"""
    User Claim / News to Verify: "{user_claim}"

    Official Search Evidence (Use ONLY these sources to verify):
    {sources_context}

    Based strictly on the evidence above, provide:
    1. Credibility Assessment (True, False, or Unverified).
    2. Neutral reasoning and explanation based on the official texts.
    """

    print("[*] Analyzing evidence with Farooq...")
    prompt = HumanMessage(formatted_input)
    response = llm.invoke([system_prompt, prompt]).content

    final_output = f"""
{response}

--------------------------------------------------
📌 **المصادر الرسمية المعتمدة:**
"""
    for idx, src in enumerate(sources_metadata, 1):
        final_output += f"\n{idx}. [{src['title']}]({src['url']})"

    return final_output

# تجربة التشغيل المباشر
#if __name__ == "__main__":
    claim_to_test = "قرارات مجلس الوزراء الأخيرة"
    result = verify_claim_with_sources(claim_to_test)
    print("\n--- تقرير منصة فاروق للتحقق ---")
    print(result)