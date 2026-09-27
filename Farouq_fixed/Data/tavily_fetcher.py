"""Search a selected group of Jordanian news and government sites."""
from tavily import TavilyClient
from Data.config import get_secret


class TavilyFetcher:
    def __init__(self):
        key = get_secret('TAVILY_API_KEY')
        if not key:
            raise RuntimeError(
                'مفتاح Tavily غير موجود. ضعي TAVILY_API_KEY في ملف .env '
                'أو في Streamlit Secrets.'
            )
        self.client = TavilyClient(api_key=key)
        # The list mixes government websites and privately owned news outlets.
        self.search_domains = [
            'petra.gov.jo', 'pm.gov.jo', 'jrtv.gov.jo', 'alrai.com',
            'addustour.com', 'ammonnews.net', 'royanews.tv', 'psd.gov.jo','jordantimes.com','representatives.jo','senate.jo','jc.jo',
                        'psd.gov.jo',        # الأمن العام
            'jaf.mil.jo',        # القوات المسلحة الأردنية
            'moi.gov.jo',        # وزارة الداخلية
            'civildefense.gov.jo', # الدفاع المدني            # الاقتصاد والمالية
            'cbj.gov.jo',        # البنك المركزي الأردني
            'mof.gov.jo',        # وزارة المالية
            'dos.gov.jo',        # دائرة الإحصاءات العامة
            'istd.gov.jo',       # دائرة ضريبة الدخل والمبيعات
            'jsc.gov.jo',        # هيئة الأوراق المالية
            'ase.com.jo',        # بورصة عمان

            # الصحة
            'moh.gov.jo',        # وزارة الصحة
            'jfda.jo',           # مؤسسة الغذاء والدواء

            # التعليم
            'moe.gov.jo',        # وزارة التربية والتعليم
            'mohe.gov.jo',       # وزارة التعليم العالي
            'yu.edu.jo',         # جامعة اليرموك (مثال جامعة رسمية)
            'ju.edu.jo',         # الجامعة الأردنية

            # الخارجية والعمل الدولي
            'mfa.gov.jo',        # وزارة الخارجية وشؤون المغتربين

            # الطاقة والمياه والبيئة والزراعة
            'memr.gov.jo',       # وزارة الطاقة والثروة المعدنية
            'mwi.gov.jo',        # وزارة المياه والري
            'moa.gov.jo',        # وزارة الزراعة
            'moenv.gov.jo',      # وزارة البيئة

            # التجارة والصناعة والسياحة
            'mit.gov.jo',        # وزارة الصناعة والتجارة
            'mota.gov.jo',       # وزارة السياحة والآثار
            'jordantourismboard.com', # هيئة تنشيط السياحة

            # الاتصالات والاقتصاد الرقمي
            'modee.gov.jo',      # وزارة الاقتصاد الرقمي والريادة
            'trc.gov.jo',        # هيئة تنظيم قطاع الاتصالات

            # الشؤون البلدية والمحلية
            'gam.gov.jo',        # أمانة عمان الكبرى
            'mmra.gov.jo',       # وزارة الإدارة المحلية / الشؤون البلدية

            # الرقابة والشفافية
            'ombudsman.jo',      # ديوان المظالم
            'jaca.gov.jo',       # هيئة النزاهة ومكافحة الفساد
            'ab.gov.jo',         # ديوان المحاسبة (Audit Bureau)

            # بوابة الحكومة الإلكترونية
            'jordan.gov.jo',     # البوابة الوطنية للحكومة الأردنية
            'opendata.gov.jo',
        ]

    def fetch_raw_data(self, query: str) -> dict:
        try:
            return self.client.search(
                query=query,
                max_results=4,
                search_depth='advanced',
                include_domains=self.search_domains,
            )
        except Exception as exc:
            raise RuntimeError(
                'فشل الاتصال بخدمة Tavily. تأكدي من صحة مفتاح TAVILY_API_KEY '
                'وصلاحيته ورصيد الحساب، ثم أعيدي المحاولة.'
            ) from exc
