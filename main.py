from graph.graph_builder import build_graph

def process_single_turn(compiled_graph, user_message, state=None):
    # Initialize state if it's the first turn
    if state is None:
        state = {
            "messages": [user_message],
            "current_agent": "unknown",
            "waiting_for_user": False
        }
    else:
        # Add the new user message and reset waiting_for_user flag
        state["messages"].append(user_message)
        state["waiting_for_user"] = False
    
    # Process the message
    new_state = compiled_graph.invoke(state)
    return new_state

if __name__ == "__main__":
    # Build and compile the graph
    graph = build_graph()
    compiled_graph = graph.compile()
    
    # Simulate a conversation
    state = process_single_turn(compiled_graph, "Hi, how much does this cost?")
    
    print("User: Hi, how much does this cost?")
    print(f"Bot: {state['messages'][-1]}")
    
    # Continue the conversation with a second turn
    state = process_single_turn(compiled_graph, "I need a refund for my purchase", state)
    
    print("User: I need a refund for my purchase")
    print(f"Bot: {state['messages'][-1]}")
