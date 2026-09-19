import re


class DataCleaner:

  @staticmethod
  def clean_text(text: str) -> str:
    """تقوم هذه الدالة بتنظيف النص الخام وإزالة الشوائب والمسافات الزائدة"""
    if not text:
      return ""

    text = re.sub(r"\n\s*\n", "\n", text)

    unwanted_phrases = ["تسجيل الدخول", "البث المباشر", "مادة إعلانية"]
    for phrase in unwanted_phrases:
      text = text.replace(phrase, "")

    text = " ".join(text.split())

    return text.strip()

  def process_tavily_results(self, raw_data: dict) -> list:
    """تمرير نتائج Tavily بالكامل لاستخراج وتنظيف المحتوى والمصادر"""
    cleaned_documents = []

    results = raw_data.get("results", [])
    for item in results:
      url = item.get("url")
      title = item.get("title")
      raw_content = item.get("content")

      cleaned_content = self.clean_text(raw_content)

      cleaned_documents.append({
          "url": url,
          "title": title,
          "content": cleaned_content,
      })

    return cleaned_documents


if __name__ == "__main__":
  from tavily_fetcher import TavilyFetcher

  fetcher = TavilyFetcher()
  raw_data = fetcher.fetch_raw_data("أحدث اخبار الأردن اليوم")

  cleaner = DataCleaner()
  processed_data = cleaner.process_tavily_results(raw_data)

  print("\n--- النتائج بعد التنظيف والفلترة (Cleaned Data) ---")
  for doc in processed_data:
    print(f"Title: {doc['title']}")
    print(f"URL: {doc['url']}")
    print(f"Content Preview: {doc['content'][:200]}...\n")
    print("-" * 50)