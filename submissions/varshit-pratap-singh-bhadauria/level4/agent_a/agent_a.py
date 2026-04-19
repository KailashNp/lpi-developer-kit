import sys
import json
import os
import subprocess

AGENT_B_PATH = os.path.join(os.path.dirname(__file__), "..", "agent_b", "agent_b.py")
AGENT_B_CARD = os.path.join(os.path.dirname(__file__), "..", "agent_b", ".well-known", "agent.json")

# Security Measure 1: Basic Prompt Injection patterns
INJECTION_PATTERNS = ["ignore all previous", "system prompt", "bypass", "you are now"]

def validate_input(user_input):
    # Security Measure 2: Input Length limit for DoS mitigation
    if len(user_input) > 500:
        raise ValueError("Security Violation: Input exceeds maximum allowed length.")
    
    # Security Measure 1 Check
    lower_input = user_input.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in lower_input:
            raise ValueError(f"Security Violation: Potential prompt injection detected ({pattern}).")
            
    return user_input

def discover_agent_b():
    # A2A Discovery Mechanism
    if not os.path.exists(AGENT_B_CARD):
        raise FileNotFoundError("Agent B A2A discovery card not found.")
    
    with open(AGENT_B_CARD, "r") as f:
        card = json.load(f)
    print(f"[*] Discovered Agent: {card.get('name')}")
    print(f"    Skills: {', '.join(card.get('skills', []))}")
    return card

def communicate_with_agent_b(user_query):
    # Create structured A2A payload
    payload = {
        "version": "1.0",
        "sender": "Agent A",
        "intent": "query_lpi_knowledge",
        "data": {
            "query": user_query
        }
    }
    
    print("[*] Sending structured request to Agent B...")
    # Using subprocess as a secure channel to Agent B over standard I/O
    process = subprocess.Popen(
        ["python", AGENT_B_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    stdout_data, stderr_data = process.communicate(input=json.dumps(payload))
    
    if process.returncode != 0:
        print(f"[!] Agent B Error: {stderr_data}")
        sys.exit(1)
        
    return json.loads(stdout_data)

def main():
    if len(sys.argv) < 2:
        print("Usage: python agent_a.py <query>")
        sys.exit(1)
        
    raw_input = " ".join(sys.argv[1:])
    
    print("--- Coordinator Agent (Agent A) ---")
    try:
        sanitized_input = validate_input(raw_input)
        print("[+] Input validation passed.")
    except Exception as e:
        print(f"[!] {e}")
        sys.exit(1)
        
    try:
        discover_agent_b()
        result = communicate_with_agent_b(sanitized_input)
        
        # Combine results into final explainable answer
        print("\n--- Final Output ---")
        print(f"Combined Answer: {result.get('answer')}")
        print(f"Explainability (Tools Used): {', '.join(result.get('provenance', []))}")
        
    except Exception as e:
        print(f"[!] Orchestration Error: {e}")

if __name__ == "__main__":
    main()
