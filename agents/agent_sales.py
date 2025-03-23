def sales_agent(message, memory):
    if "price" in message.lower():
        return "Our product costs $49. Would you like to proceed?"
    return "Let me connect you to someone who can assist."
