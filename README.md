# LangGraph Debugging Assignment

## 🎯 Objective

Fix bugs in a multi-agent conversational AI system using LangGraph. You are expected to use the Cursor AI code editor to debug and refactor the code.

## 📂 Task

1. Run the app and identify why the multi-agent system is not functioning as expected.
2. Fix:
   - Broken agent routing
   - Context memory retention
   - Incorrect graph execution
3. Refactor any redundant or unused code.
4. Add at least one unit test to demonstrate a fixed conversation flow.
5. Use Cursor's AI features for suggestions and include a short summary of how it helped (in `cursor_usage.md`).

## 🛠️ Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## 🐛 Fixed Issues

The following issues were fixed in the codebase:

1. **Agent Routing Bug**: Fixed the agent manager to correctly route messages containing "price", "cost", or "how much" to the sales agent, and messages containing "refund" to the support agent.

2. **Memory Store Bug**: Fixed the memory save functionality that was using a string literal "key" instead of the variable name.

3. **Graph Structure**: Updated the graph structure to:
   - Include proper state schema definitions
   - Fix routing between agents
   - Prevent infinite recursion with a waiting_for_user flag
   - Correctly maintain conversation context

4. **LangGraph API Usage**: Updated the code to properly compile the graph before invocation.

## 🧪 Running Tests

To verify that the conversation flow works correctly, run the unit tests:

```bash
# Run tests
pytest tests/test_conversation_flow.py -v
```

The tests validate:
- Routing to the correct agent based on message content
- Memory persistence across conversation turns
- Proper agent responses for different types of queries

## 📦 Submission

- Fix all bugs
- Commit with useful messages
- Push to GitHub and send the link

## 🧠 How It Works

The multi-agent system uses a state graph that routes messages to:
- Sales agent: for price/cost inquiries
- Support agent: for refund requests
- Unknown: for queries it doesn't understand

Each conversation turn follows this flow:
1. User message is added to state
2. Router determines which agent should handle it
3. Agent processes the message and provides a response
4. Graph execution pauses waiting for the next user input
5. Repeat with next user message





