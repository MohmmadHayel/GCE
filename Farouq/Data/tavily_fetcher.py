import json
from Data.config import TAVILY_API_KEY

from tavily import TavilyClient


from Data.config import TAVILY_API_KEY
class TavilyFetcher:

  def __init__(self):
    self.client = TavilyClient(api_key=TAVILY_API_KEY)
    
    # قائمة النطاقات الرسمية والموثوقة في الأردن
    self.official_domains = [
        "petra.gov.jo",
        "pm.gov.jo",
        "jrtv.gov.jo",
        "alrai.com",
        "addustour.com",
        "ammonnews.net",
        "royanews.tv",
        "psd.gov.jo"
    ]

  def fetch_raw_data(self, query: str):
    print(f"[*] Fetching verified data from official sources for query: '{query}'...")

    try:
      # استخدام include_domains ليقتصر البحث فقط على الوكالات والمصادر الرسمية
      response = self.client.search(
          query=query, 
          max_results=4, 
          search_depth="advanced", #  لأننا نبحث في نطاقات محددة لنضمن جودة الخبر
          include_domains=self.official_domains
      )
      return response
    except Exception as e:
      print(f"[!] Error fetching data: {e}")
      return None


#if __name__ == "__main__":
  fetcher = TavilyFetcher()
  # جرب استعلام اختبارى
  raw_data = fetcher.fetch_raw_data("قرارات مجلس الوزراء الأردني")

  print("\n--- النتائج الخام من المصادر الرسمية فقط ---")
  print(json.dumps(raw_data, indent=4, ensure_ascii=False))