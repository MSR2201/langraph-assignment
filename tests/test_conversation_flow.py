import sys
import os
import pytest
from unittest.mock import patch

# Add the project root to path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from graph.graph_builder import build_graph
from utils.memory_store import Memory
from agents.agent_manager import route_to_agent

def process_message(compiled_graph, message, state=None):
    """Helper function to process a single message through the graph"""
    if state is None:
        state = {
            "messages": [message],
            "current_agent": "unknown",
            "waiting_for_user": False
        }
    else:
        state["messages"].append(message)
        state["waiting_for_user"] = False
    
    # Process the message and return the new state
    return compiled_graph.invoke(state)

def test_conversation_flow():
    """Test that the conversation flows correctly between agents"""
    # Build and compile the graph
    graph = build_graph()
    compiled_graph = graph.compile()
    
    # Test sales agent flow
    state = process_message(compiled_graph, "What is the price of your product?")
    assert "$49" in state["messages"][-1].lower()
    assert state["current_agent"] == "sales"
    assert state["waiting_for_user"] == True
    
    # Test support agent flow
    state = process_message(compiled_graph, "I need a refund", state)
    assert "refund" in state["messages"][-1].lower()
    assert "order id" in state["messages"][-1].lower()
    assert state["current_agent"] == "support"
    assert state["waiting_for_user"] == True
    
    # Test unknown route
    state = process_message(compiled_graph, "Tell me about the weather", state)
    assert "couldn't understand" in state["messages"][-1].lower()
    assert state["current_agent"] == "unknown"
    assert state["waiting_for_user"] == True

def test_memory_persistence():
    """Test that memory persists across turns"""
    memory = Memory()
    
    # Store information in memory
    memory.save("user_id", "12345")
    memory.save("purchase_date", "2023-05-15")
    
    # Retrieve and verify information
    assert memory.load("user_id") == "12345"
    assert memory.load("purchase_date") == "2023-05-15"
    assert memory.load("nonexistent_key") == ""  # Default return for missing keys

def test_agent_routing():
    """Test the agent routing logic"""
    assert route_to_agent("What is the price?") == "sales"
    assert route_to_agent("How much does it cost?") == "sales"
    assert route_to_agent("I need a refund please") == "support"
    assert route_to_agent("Hello there") == "unknown" 