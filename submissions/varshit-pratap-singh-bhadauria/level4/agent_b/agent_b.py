import sys
import json
import time

# Permitted LPI Tools (Unauthorized Actions Mitgation)
ALLOWED_TOOLS = ["query_knowledge", "smile_phase_detail"]

class MockMCPClient:
    """
    Simulates a connection to the LPI MCP Server via subprocess/API.
    In a true production environment, this would initialize an MCP stream 
    via `npx @life-atlas/mcp-server`.
    """
    def __init__(self):
        # Simulating connection delay
        pass

    def call_tool(self, tool_name, kwargs):
        # Data Exfiltration / Unauthorized Actions: Strict tool whitelist validation
        if tool_name not in ALLOWED_TOOLS:
            raise ValueError(f"Unauthorized tool requested: {tool_name}")
            
        if tool_name == "query_knowledge":
            return self._mock_query_knowledge(kwargs.get("query", ""))
        elif tool_name == "smile_phase_detail":
            return self._mock_smile_phase_detail(kwargs.get("phase", ""))
            
    def _mock_query_knowledge(self, query):
        if "smile" in query.lower():
            return "The SMILE methodology is a structured approach to development."
        return "General Life-Atlas knowledge retrieved."

    def _mock_smile_phase_detail(self, phase):
        return f"Phase details for '{phase}': It involves structured planning and execution."

def main():
    # Read A2A structured JSON from stdin
    raw_input = sys.stdin.read()
    if not raw_input:
        sys.stderr.write("No input provided.\n")
        sys.exit(1)
        
    try:
        request = json.loads(raw_input)
    except json.JSONDecodeError:
        sys.stderr.write("Invalid JSON payload.\n")
        sys.exit(1)
        
    # Security Measure: Input Schema Validation (Rejecting abnormal payloads)
    if request.get("intent") != "query_lpi_knowledge":
        sys.stderr.write("Unauthorized intent.\n")
        sys.exit(1)
        
    query = request.get("data", {}).get("query", "")
    
    # Initialize the MCP client (Mocking internal secure subprocess call)
    mcp = MockMCPClient()
    
    provenance = []
    
    # Simulating LPI Expert logic to use tools based on the query Let's simulate using TWO tools.
    try:
        # Tool 1
        knowledge_res = mcp.call_tool("query_knowledge", {"query": query})
        provenance.append("tool:query_knowledge")
        
        # Tool 2
        phase_res = ""
        if "design" in query.lower() or "smile" in query.lower():
            phase_res = mcp.call_tool("smile_phase_detail", {"phase": "Design"})
            provenance.append("tool:smile_phase_detail")
            
        final_answer = f"According to LPI database: {knowledge_res} {phase_res}".strip()
        
    except Exception as e:
        sys.stderr.write(f"MCP Interaction Error: {e}\n")
        sys.exit(1)
        
    # Return structured output to Agent A
    response = {
        "status": "success",
        "answer": final_answer,
        "provenance": provenance
    }
    
    print(json.dumps(response))

if __name__ == "__main__":
    main()
