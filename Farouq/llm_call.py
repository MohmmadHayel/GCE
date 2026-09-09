from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
api_key="API",
base_url="https://openrouter.ai/api/v1",
model="openrouter/free",
temperature=0.8
)