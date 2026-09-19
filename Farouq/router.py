from Data.cleaner import DataCleaner
from Data.tavily_fetcher import TavilyFetcher
from intent_router import classify_user_intent
from langchain_classic.schema import HumanMessage, SystemMessage
from llm_call import llm


def handle_search_intent(query: str):
  """معالجة حالة الاستعلام عن أخبار عامة دون الحاجة لتدقيق صحة"""
  print(f"[*] Executing SEARCH route for: '{query}'")

  fetcher = TavilyFetcher()
  raw_data = fetcher.fetch_raw_data(query)

  if not raw_data or not raw_data.get("results"):
    return "عذراً، لم أتمكن من العثور على أخبار مطابقة لهذه البحث من المصادر الرسمية."

  cleaner = DataCleaner()
  cleaned_docs = cleaner.process_tavily_results(raw_data)

  output = "📰 **أحدث المستجدات الرسمية:**\n\n"
  sources_metadata = []

  for idx, doc in enumerate(cleaned_docs[:3], 1):
    output += (
        f"**{idx}. {doc['title']}**\n{doc['content'][:250]}...\n\n"
    )
    sources_metadata.append({"title": doc["title"], "url": doc["url"]})

  output += "--------------------------------------------------\n📌 **المصادر:**"
  for idx, src in enumerate(sources_metadata, 1):
    output += f"\n{idx}. [{src['title']}]({src['url']})"

  return output


def handle_verify_intent(claim: str):
  """معالجة حالة التحقق من صحة الادعاءات والأخبار"""
  print(f"[*] Executing VERIFY route for claim: '{claim}'")

  fetcher = TavilyFetcher()
  raw_data = fetcher.fetch_raw_data(claim)

  if not raw_data or not raw_data.get("results"):
    return "عذراً، لم أتمكن من العثور على مصادر رسمية كافية للتحقق من هذا الادعاء حالياً."

  cleaner = DataCleaner()
  cleaned_docs = cleaner.process_tavily_results(raw_data)

  sources_context = ""
  sources_metadata = []

  for idx, doc in enumerate(cleaned_docs, 1):
    sources_context += (
        f"Source [{idx}] Title: {doc['title']}\nURL: {doc['url']}\nContent:"
        f" {doc['content']}\n\n"
    )
    sources_metadata.append({"title": doc["title"], "url": doc["url"]})

  system_prompt = SystemMessage(
      """You are "Farooq", an advanced, objective AI news verification assistant. 
Review the user claim against the provided official search evidence. 
Provide:
1. Credibility Assessment (True, False, or Unverified).
2. Neutral reasoning.
IMPORTANT: When mentioning evidence from the sources, explicitly cite them by their source number (e.g., [Source 1] or [1]) so the system knows which sources were actually utilized."""
  )

  formatted_input = f"""
    User Claim to Verify: "{claim}"

    Official Search Evidence:
    {sources_context}
    """

  prompt = HumanMessage(formatted_input)
  response = llm.invoke([system_prompt, prompt]).content


  used_sources = []
  for idx, src in enumerate(sources_metadata, 1):
    if f"[{idx}]" in response or f"Source [{idx}]" in response:
      used_sources.append(src)

  # إذا لم يذكر النموذج رقماً محدداً، نعرض أول مصدرين كاحتياط
  if not used_sources:
    used_sources = sources_metadata[:2]

  final_output = f"""
{response}

--------------------------------------------------
📌 **المصادر المعتمدة في هذا التقرير:**
"""
  for idx, src in enumerate(used_sources, 1):
    final_output += f"\n{idx}. [{src['title']}]({src['url']})"

  return final_output


def process_user_request(user_input: str):
  print(f"\n==========================================")
  print(f"User Input: '{user_input}'")
  print(f"==========================================\n")

  intent = classify_user_intent(user_input)
  print(f"[*] Classified Intent: [{intent}]\n")

  if intent == "VERIFY":
    return handle_verify_intent(user_input)
  else:
    return handle_search_intent(user_input)


# تجربة التشغيل المباشر
#if __name__ == "__main__":
  # تجربة استعلام بحثي واستعلام تحقق
  test_queries = [
      "أعطيني آخر أخبار الاقتصاد في الأردن",
      "هل صحيح أن مجلس الوزراء أقر قرارات جديدة مؤخراً؟",
  ]

  for query in test_queries:
    result = process_user_request(query)
    print(result)
    print("\n" + "=" * 50 + "\n")