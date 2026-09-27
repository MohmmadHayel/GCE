"""Create an LLM client for the API provider that supplied the key."""
from functools import lru_cache
from langchain_openai import ChatOpenAI
from Data.config import get_secret


@lru_cache(maxsize=1)
def get_llm() -> ChatOpenAI:
    openrouter_key = get_secret('OPENROUTER_API_KEY')
    if openrouter_key:
        return ChatOpenAI(
            api_key=openrouter_key,
            base_url='https://openrouter.ai/api/v1',
            model=get_secret('OPENROUTER_MODEL') or 'openrouter/free',
            temperature=0,
        )

    openai_key = get_secret('OPENAI_API_KEY')
    if openai_key:
        return ChatOpenAI(
            api_key=openai_key,
            model=get_secret('OPENAI_MODEL') or 'gpt-4o-mini',
            temperature=0,
        )

    raise RuntimeError(
        'مفتاح نموذج الذكاء الاصطناعي غير موجود. ضعي OPENROUTER_API_KEY '
        'أو OPENAI_API_KEY في ملف .env أو في Streamlit Secrets.'
    )
