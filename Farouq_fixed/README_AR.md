# تشغيل مشروع فاروق (الإصدار المصحّح)

## أولًا: مهم قبل البدء

المشروع الأصلي احتوى على مفاتيح API داخل ملفات Python؛ **ألغِي تلك المفاتيح وأنشئي مفاتيح جديدة** لدى مزودي الخدمة. لا تنشري مفاتيحك على GitHub ولا تشاركي ملف `.env`.

## 1. تجهيز بيئة جديدة

يفضّل Python 3.11 أو 3.12، واستخدام بيئة جديدة بدل نسخ `venv` من جهاز شخص آخر.

على Windows PowerShell داخل مجلد المشروع:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

في حال عدم تثبيت Python 3.12 يمكنك استخدام `py -3.11`. على macOS/Linux استعملي `python3 -m venv .venv` و `source .venv/bin/activate`.

## 2. المفاتيح

انسخي `.env.example` إلى ملف جديد اسمه `.env` واكتبي:

```ini
TAVILY_API_KEY=YOUR_NEW_TAVILY_KEY
OPENROUTER_API_KEY=YOUR_OPENROUTER_KEY
OPENROUTER_MODEL=openrouter/free
```

**اختاري أحد مزوّدي النماذج فقط:** لا تضعي مفتاح OpenAI في `OPENROUTER_API_KEY`؛ إن أردت استخدام OpenAI احذفي سطر OpenRouter، وضعي `OPENAI_API_KEY` بدلًا منه مع `OPENAI_MODEL=gpt-4o-mini`.

قد تتغير النماذج المتاحة في OpenRouter؛ إذا ظهرت رسالة `model not found` اختاري نموذجًا متاحًا لحسابك وعدّلي `OPENROUTER_MODEL`.

## 3. تشغيل Streamlit

```powershell
python -m streamlit run app.py
```

لا تنقلي مجلد `venv` من الأرشيف الأصلي إلى مشروعك.

## 4. Streamlit Community Cloud

ضعي المتغيرات في App settings → Secrets بنفس الأسماء من دون أي مفاتيح داخل ملف Python؛ مثال **بقِيَم وهمية**:

```toml
TAVILY_API_KEY = "YOUR_NEW_TAVILY_KEY"
OPENROUTER_API_KEY = "YOUR_OPENROUTER_KEY"
OPENROUTER_MODEL = "openrouter/free"
```

## 5. عند حدوث مشكلة

- رسالة missing key: تحققي من الملف `.env` ومكانه في نفس مجلد `app.py`، أو من Secrets عند الاستضافة.
- `401`: لا يطابق مفتاح API مزوّد الخدمة أو انتهت صلاحيته. تأكدي من وجود رصيد/صلاحية ومن نوع المفتاح.
- `ModuleNotFoundError`: ثبتي المكتبات من `requirements.txt` داخل البيئة المفعّلة.
- أخطاء الشبكة/الرصيد: لا يمكن التأكد منها من الكود دون تجربة مفاتيح سليمة واتصال بالإنترنت.

**حدود الإصدار:** تم تنظيف الأخطاء الظاهرة وتجهيز بنية قابلة للاختبار دون مفاتيح حقيقية. لم يتم اختبار استجابة فعلية من Tavily أو OpenRouter/OpenAI بحسابك.
