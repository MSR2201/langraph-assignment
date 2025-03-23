from langgraph.graph import StateGraph
from agents.agent_sales import sales_agent
from agents.agent_support import support_agent
from agents.agent_manager import route_to_agent
from utils.memory_store import Memory
from typing import TypedDict, Annotated, List, Literal

# Define message reducer
def message_reducer(existing_messages: List[str], new_messages: List[str]) -> List[str]:
    return existing_messages + new_messages

# Define the state schema
class State(TypedDict):
    messages: Annotated[List[str], message_reducer]
    current_agent: Literal["sales", "support", "unknown"]
    waiting_for_user: bool

def build_graph():
    memory = Memory()
    
    # Initialize the graph with a state schema
    graph = StateGraph(State)

    # Define the router node
    def router(state):
        message = state["messages"][-1] if state["messages"] else ""
        # Apply routing logic to determine agent
        message_lower = message.lower()
        if any(term in message_lower for term in ["price", "cost", "how much"]):
            agent = "sales"
        elif "refund" in message_lower:
            agent = "support"
        else:
            agent = "unknown"
        
        return {"current_agent": agent}

    # Define the agent nodes
    def sales_node(state):
        message = state["messages"][-1] if state["messages"] else ""
        response = sales_agent(message, memory)
        return {"messages": [response], "waiting_for_user": True}
    
    def support_node(state):
        message = state["messages"][-1] if state["messages"] else ""
        response = support_agent(message, memory)
        return {"messages": [response], "waiting_for_user": True}
    
    def unknown_node(state):
        return {"messages": ["Sorry, I couldn't understand your request."], "waiting_for_user": True}

    # Add nodes to the graph
    graph.add_node("router", router)
    graph.add_node("sales", sales_node)
    graph.add_node("support", support_node)
    graph.add_node("unknown", unknown_node)
    
    # Define the entry point
    graph.set_entry_point("router")
    
    # Define conditional edges with proper end condition
    def route_condition(state):
        # Check if we should end the conversation turn
        if state.get("waiting_for_user", False):
            return "END"  # Special value to end execution
        else:
            return state["current_agent"]
            
    graph.add_conditional_edges("router", route_condition)
    
    # Add edges from agent nodes back to router
    graph.add_edge("sales", "router")
    graph.add_edge("support", "router")
    graph.add_edge("unknown", "router")
    
    return graph
