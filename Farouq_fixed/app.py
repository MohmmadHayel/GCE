# """Streamlit UI for Farouq."""
# import streamlit as st
# from Data.config import get_secret
# from router import process_user_request

# st.set_page_config(page_title='منصة فاروق للتحقق الإخباري', page_icon='🛡️', layout='centered')
# st.title('🛡️ منصة فاروق الذكية للتحقق الإخباري')
# st.markdown('مساعد للتحقق من الأخبار والادعاءات بالاستناد إلى مجموعة مختارة من المصادر الأردنية.')

# missing = []


# # st.write("TAVILY:", bool(get_secret("TAVILY_API_KEY")))
# # st.write("OPENROUTER:", bool(get_secret("OPENROUTER_API_KEY")))


# if not get_secret('TAVILY_API_KEY'):
#     missing.append('TAVILY_API_KEY')
# if not (get_secret('OPENROUTER_API_KEY') or get_secret('OPENAI_API_KEY')):
#     missing.append('OPENROUTER_API_KEY أو OPENAI_API_KEY')
# if missing:
#     st.warning('إعدادات مطلوبة قبل الاستخدام: ' + '، '.join(missing))
#     st.caption('للتشغيل المحلي: انسخي .env.example إلى .env وضعي مفاتيح جديدة. '
#                'على Streamlit Cloud: أضيفي القيم نفسها في Secrets.')

# with st.form('news_check'):
#     query = st.text_area(
#         'اكتبي الخبر أو الادعاء أو الموضوع:',
#         placeholder='مثلًا: هل صدر قرار جديد بشأن ...؟',
#         height=120,
#     )
#     submitted = st.form_submit_button('تحقق / ابحث', type='primary', disabled=bool(missing))

# if submitted:
#     if not query.strip():
#         st.warning('الرجاء إدخال نص صحيح للبحث أو التحقق.')
#     else:
#         with st.spinner('جاري البحث وتحليل النتائج...'):
#             try:
#                 report = process_user_request(query.strip())
#             except (RuntimeError, ValueError) as exc:
#                 st.error(str(exc))
#             except Exception:
#                 st.error('حصل خطأ غير متوقع أثناء معالجة الطلب. راجعي سجل Terminal لمعرفة التفاصيل.')
#                 # Log stack trace to the server instead of exposing internals in HTML.
#                 import logging
#                 logging.exception('Unhandled error while processing request')
#             else:
#                 st.subheader('النتيجة والتقرير')
#                 st.markdown(report)  # Render links correctly; do not allow injected HTML.

# st.markdown('---')
# st.caption('نتائج البحث وتقييمات النموذج قابلة للخطأ، ويُنصح بمراجعة النص الأصلي لكل مصدر.')






"""Streamlit UI for Farouq."""
import streamlit as st
from Data.config import get_secret
from router import process_user_request

st.set_page_config(page_title='منصة فاروق للتحقق الإخباري', page_icon='🛡️', layout='centered')
st.title('🛡️ منصة فاروق الذكية للتحقق الإخباري')
st.markdown('مساعد للتحقق من الأخبار والادعاءات بالاستناد إلى مجموعة مختارة من المصادر الأردنية.')

tab1, tab2 = st.tabs(['التحقق من الأخبار', 'QR code'])

with tab1:
    missing = []

    #st.write("TAVILY:", bool(get_secret("TAVILY_API_KEY")))
    #st.write("OPENROUTER:", bool(get_secret("OPENROUTER_API_KEY")))

    if not get_secret('TAVILY_API_KEY'):
        missing.append('TAVILY_API_KEY')
    if not (get_secret('OPENROUTER_API_KEY') or get_secret('OPENAI_API_KEY')):
        missing.append('OPENROUTER_API_KEY أو OPENAI_API_KEY')
    if missing:
        st.warning('إعدادات مطلوبة قبل الاستخدام: ' + '، '.join(missing))
        st.caption('للتشغيل المحلي: انسخي .env.example إلى .env وضعي مفاتيح جديدة. '
                   'على Streamlit Cloud: أضيفي القيم نفسها في Secrets.')

    with st.form('news_check'):
        query = st.text_area(
            'اكتبي الخبر أو الادعاء أو الموضوع:',
            placeholder='مثلًا: هل صدر قرار جديد بشأن ...؟',
            height=120,
        )
        submitted = st.form_submit_button('تحقق / ابحث', type='primary', disabled=bool(missing))

    if submitted:
        if not query.strip():
            st.warning('الرجاء إدخال نص صحيح للبحث أو التحقق.')
        else:
            with st.spinner('جاري البحث وتحليل النتائج...'):
                try:
                    report = process_user_request(query.strip())
                except (RuntimeError, ValueError) as exc:
                    st.error(str(exc))
                except Exception:
                    st.error('حصل خطأ غير متوقع أثناء معالجة الطلب. راجعي سجل Terminal لمعرفة التفاصيل.')
                    # Log stack trace to the server instead of exposing internals in HTML.
                    import logging
                    logging.exception('Unhandled error while processing request')
                else:
                    st.subheader('النتيجة والتقرير')
                    st.markdown(report)  # Render links correctly; do not allow injected HTML.

    st.markdown('---')
    st.caption('نتائج البحث وتقييمات النموذج قابلة للخطأ، ويُنصح بمراجعة النص الأصلي لكل مصدر.')

with tab2:
    pass