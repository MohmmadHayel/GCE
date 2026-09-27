"""Distinguish verification requests from general news searches."""
from langchain_core.messages import HumanMessage, SystemMessage
from llm_call import get_llm


def classify_user_intent(user_input: str) -> str:
    system = SystemMessage(content=(
        'Classify the user request for a news service into exactly one label: '
        'VERIFY if the user asks about the truth of a particular claim or rumor; '
        'SEARCH if the user asks for general news or topic updates. '
        'Reply with one word only: VERIFY or SEARCH.'
    ))
    response = get_llm().invoke([
        system, HumanMessage(content=f'User input: {user_input}')
    ])
    label = str(response.content).strip().upper()
    return 'VERIFY' if 'VERIFY' in label else 'SEARCH'
