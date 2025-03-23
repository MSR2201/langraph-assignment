def route_to_agent(message):
    message_lower = message.lower()
    if any(term in message_lower for term in ["price", "cost", "how much"]):
        return "sales"
    elif "refund" in message_lower:
        return "support"
    return "unknown"
