import os
import sys
from router import process_user_request
import streamlit as st

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="منصة فاروق للتحقق الإخباري", page_icon="🛡️", layout="centered"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stTextInput textarea {
        direction: rtl;
    }
    .report-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title(" منصة فاروق الذكية للتحقق الإخباري")
st.markdown(
    "مرحباً بك! أنا **فاروق**، مساعدك الذكي للتحقق من صحة الأخبار والادعاءات من المصادر الرسمية المعتمدة في الأردن."
)
st.markdown("---")

user_query = st.text_input(
    "اكتب الخبر، الادعاء، أو موضوع البحث الذي ترغب بالتحقق منه أو الاستعلام عنه:",
    placeholder="مثلاً: هل صحيح أن مجلس الوزراء أقر قرارات جديدة؟ أو أعطيني آخر أخبار الاقتصاد...",
)

if st.button("تحقق / ابحث", type="primary"):
  if not user_query.strip():
    st.warning(" الرجاء إدخال نص صحيح للبحث أو التحقق.")
  else:
    with st.spinner(" جاري جاري جاري جاري البيانات وتحليلها بواسطة فاروق..."):
      try:
        # استدعاء الراوتر المركزي الذي بنيناه سابقاً
        result = process_user_request(user_query)

        # عرض النتيجة داخل حاوية منظمة
        st.markdown("###  النتيجة والتقرير:")
        st.markdown(
            f'<div class="report-container">{result}</div>',
            unsafe_allow_html=True,
        )

      except Exception as e:
        st.error(f"حدث خطأ غير متوقع أثناء معالجة الطلب: {str(e)}")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>منصة فاروق الذكية - مدعومة بنماذج الذكاء الاصطناعي ومصادر البيانات الرسمية</p>",
    unsafe_allow_html=True,
)