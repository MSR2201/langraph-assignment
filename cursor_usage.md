# Cursor Usage Summary

## How I used Cursor:

(Provide details on how you used Cursor AI to assist with debugging and refactoring.)

1. First I asked cursor to explain what's the code about then it explained me on how the code works and also gave me what are the minor issues that are present like the agent_manager routing and memory store key value error.
2. Then I asked it to quickly fix them so it changed those codes. 
3. Then i ran the main.py i immediately got error of the state_schema then i gave cursor to explain and fix the error so it changed the code of main and the graph_builder to quickly change the codes that are not working. After that i got error of graph.invoke and graph.run so i asked it to refer the langchain library and fix the code.
4. After that i got errors of the recursion_limit and branch did not return valid destination so i asked it to fix the issues then it fixed them then the bugs are fixed 



## AI Suggestions:

Accepted: the codes below are accepted according to AI suggestions

1.  if "price" in message.lower():
        return "sales"
2. def save(self, key, value):
        self.data[key] = value


Rejected
1. When it gave the graph.run or graph.invoke twice i rejected and then asked to fix it again  

Improved based on AI suggestions
graph_builder and main.py are improved using the AI suggestions on 3 iterations 

## Thoughts:

Cursor is a great tool for our development purpose if i didnt have cursor this task might take around 5 to 6 hours of internet surfing and then fixing the code by hand using this makes us faster and very efficient.
