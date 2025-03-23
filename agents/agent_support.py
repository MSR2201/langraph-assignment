def support_agent(message, memory):
    if "refund" in message.lower():
        return "I'm happy to help with your refund. Can you provide your order ID?"
    return "Let me connect you to someone who can assist."
