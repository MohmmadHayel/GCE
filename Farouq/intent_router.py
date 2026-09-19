from langchain_classic.schema import HumanMessage, SystemMessage
from llm_call import llm


def classify_user_intent(user_input: str) -> str:
  """تقوم هذه الدالة بتحليل نية المستخدم وتحديد ما إذا كان يطلب (تحقق) أو (استعلام عن خبر)"""

  router_system_prompt = SystemMessage("""You are an intent classification router for an AI news platform named "Farooq".
Analyze the user's input and classify their intent into one of two exact categories:
1. "VERIFY": If the user is claiming something, asking about the truth/accuracy of a specific piece of news, rumor, or statement.
2. "SEARCH": If the user is generally asking for latest news, updates, or information about a topic without asking to verify a specific claim.

Return ONLY the category name: either "VERIFY" or "SEARCH". Do not add any extra text or punctuation.""")

  prompt = HumanMessage(f"User Input: {user_input}")
  response = llm.invoke([router_system_prompt, prompt]).content.strip()

  if "VERIFY" in response.upper():
    return "VERIFY"
  else:
    return "SEARCH"


# تجربة عملية للتصنيف
#if __name__ == "__main__":
  test_queries = [
      "هل صحيح أن مجلس الوزراء أقر قانون كذا؟",
      "أعطيني آخر أخبار الاقتصاد في الأردن",
      "يقال إن هناك قرار برفع الدعم، هل هذا صحيح؟",
  ]

  for q in test_queries:
    intent = classify_user_intent(q)
    print(f"Query: '{q}' ---> Classified Intent: [{intent}]")