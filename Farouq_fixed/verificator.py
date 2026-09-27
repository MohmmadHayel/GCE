"""Compatibility entry point for direct verification calls."""
from router import handle_verify_intent


def verify_claim_with_sources(user_claim: str) -> str:
    return handle_verify_intent(user_claim)
