# HOW I DID IT  

Name: Kailash Narayana Prasad  

---

## Level 2 — QA & Security Testing  

### What I Did  

For Level 2, I focused on testing the LPI sandbox using the provided test client. I modified the `test-client.ts` file and experimented with different types of inputs to understand how the system behaves under unusual conditions.

I tested:
- Normal inputs (valid queries)
- Very long strings (stress testing)
- Special characters
- SQL-like inputs (e.g., `' OR 1=1 --`)
- Empty and null values
- Incorrect data types (numbers instead of strings)

---

### Problems I Faced  

- Initially, I was unsure how to run the test client and had issues with the TypeScript setup  
- I didn’t know where to execute the test script  
- Some errors were confusing because the system showed `[PASS]` even when internal errors occurred  
- I also faced formatting issues while preparing `level2.md`, especially with code blocks  

---

### How I Solved Them  

- Built and ran the project using `npm run build` and `npm run test-client`  
- Carefully observed terminal outputs to understand system behavior  
- Identified that some tools were not validating input types properly  
- Fixed formatting issues in the markdown file so the bot could correctly parse the output  

---

### What I Learned  

- Importance of proper input validation  
- How systems can silently fail while appearing to work  
- How to debug issues by analyzing logs and outputs  
- The importance of correct formatting for automated evaluation systems  

---

## Level 3 — Security Audit  

### What I Did  

For Level 3, I analyzed the intentionally vulnerable API provided in `examples/vulnerable-api.py`.

I:
- Installed Flask and ran the API locally  
- Observed terminal output, including debug mode and exposed API key  
- Opened the API in a browser and tested endpoints  
- Initially tried incorrect endpoints like `/user`, which helped me realize I needed to inspect the source code  
- Opened the Python file and identified all available routes using `@app.route`  
- Tested each endpoint with both normal and malicious inputs  

---

### Testing Approach  

I tested the API using:

- Normal queries to understand expected behavior  
- SQL injection attempts  
- XSS payloads  
- Command injection inputs  
- Invalid data types  
- Manual inspection of responses and debug output  

---

### Vulnerabilities I Identified  

- Command Injection (`/api/run`)  
- SQL Injection (`/api/query`)  
- Sensitive Data Exposure (debug info, API key, environment variables)  
- Hardcoded credentials (API key and admin password)  
- Broken authentication (`/api/admin`)  
- Cross-Site Scripting (XSS) (`/api/user/<id>`)  
- Debug mode enabled  
- Public exposure via `0.0.0.0`  

---

### Problems I Faced  

- Initially tested wrong endpoints and kept getting 404 errors  
- Didn’t realize endpoints had `/api/...` prefix  
- Confusion about whether I should fix the code or just report issues  
- Python setup issue (`python3` not recognized on Windows)  

---

### How I Solved Them  

- Read the source code to identify correct endpoints  
- Switched from `python3` to `python`  
- Understood that the goal is to analyze vulnerabilities, not fix them  
- Tested inputs step-by-step and observed responses carefully  

---

### What I Learned  

- How real-world APIs can be vulnerable to injection attacks  
- Importance of input validation and sanitization  
- How debug mode can expose critical system information  
- Basics of OWASP vulnerability categories  
- How to approach security testing systematically instead of guessing  

---

## Final Reflection  

Through this internship process, I learned how to think like both a developer and a security tester. Instead of just writing code, I learned how to break systems, analyze their behavior, and understand the importance of secure design.

This experience helped me improve my debugging skills, attention to detail, and understanding of real-world security risks.