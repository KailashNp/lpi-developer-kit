## Repository Link

https://github.com/KailashNp/lpi-developer-kit

# Level 3 — Security Audit Report  
Name: Kailash Narayana Prasad  

---

## Objective  
To identify, analyze, and document security vulnerabilities in the intentionally vulnerable API (`examples/vulnerable-api.py`) and propose fixes following OWASP standards.

---

## Methodology  

- Ran the vulnerable API locally using Flask  
- Observed terminal logs and debug output  
- Inspected the source code to identify vulnerabilities  
- Identified endpoints using `@app.route`  
- Tested endpoints using browser with different inputs  
- Tried malicious inputs like SQL injection, XSS, and command injection  
- Observed responses and analyzed behavior  

---

## Vulnerabilities Identified  

---

### 1. Command Injection (CRITICAL)

**Endpoint:** `/api/run`

**Issue:**  
User input is directly executed in the system shell:

```python
subprocess.check_output(cmd, shell=True)
```

**Test:**  
http://127.0.0.1:5001/api/run?cmd=whoami  

**Impact:**  
- Full system command execution  
- Remote Code Execution (RCE)  
- Complete system compromise  

**OWASP Category:**  
A03: Injection  

**Fix:**  
- Remove `shell=True`  
- Validate and whitelist commands  
- Use safer subprocess methods  

---

### 2. SQL Injection  

**Endpoint:** `/api/query`

**Issue:**  
User input is inserted into SQL query using string formatting:

```python
db.execute(f"INSERT INTO queries (query, user_ip) VALUES ('{q}', '{user_ip}')")
```

**Test:**  
http://127.0.0.1:5001/api/query?q=' OR 1=1 --  

**Impact:**  
- Database manipulation  
- Data corruption  

**OWASP Category:**  
A03: Injection  

**Fix:**  
Use parameterized queries:

```python
db.execute("INSERT INTO queries (query, user_ip) VALUES (?, ?)", (q, user_ip))
```

---

### 3. Sensitive Data Exposure (CRITICAL)

**Endpoint:** `/api/query`

**Issue:**  
Debug mode exposes sensitive information:
- API key  
- Environment variables  
- Server path  

**Test:**  
http://127.0.0.1:5001/api/query?q=test  

**Impact:**  
- Credential leakage  
- Exposure of internal system details  

**OWASP Category:**  
A02: Sensitive Data Exposure  

**Fix:**  
- Disable debug mode in production  
- Remove sensitive data from responses  

---

### 4. Hardcoded Credentials  

**Issue:**  
Sensitive credentials stored directly in code:

```python
API_KEY = "sk-lifeatlas-dev-2026-secret-key"
ADMIN_PASSWORD = "admin123"
```

**Impact:**  
- Anyone with code access can retrieve secrets  

**OWASP Category:**  
A02: Sensitive Data Exposure  

**Fix:**  
- Use environment variables  

---

### 5. Broken Authentication  

**Endpoint:** `/api/admin`

**Issue:**  
- Plain text password comparison  
- No hashing  
- No rate limiting  

**Test:**  
http://127.0.0.1:5001/api/admin?password=admin123  

**Impact:**  
- Easy brute-force attack  
- Unauthorized admin access  

**OWASP Category:**  
A07: Identification and Authentication Failures  

**Fix:**  
- Hash passwords  
- Implement proper authentication (JWT/session)  

---

### 6. Cross-Site Scripting (XSS)

**Endpoint:** `/api/user/<user_id>`

**Issue:**  
User input is directly rendered in HTML:

```python
request.args.get('name')
```

**Test:**  
http://127.0.0.1:5001/api/user/1?name=<script>alert(1)</script>  

**Impact:**  
- Script execution in browser  
- Session hijacking  

**OWASP Category:**  
A03: Injection (XSS)  

**Fix:**  
- Escape user input  
- Use safe templating  

---

### 7. Debug Mode Enabled  

**Issue:**  
Application runs in debug mode:

```python
DEBUG_MODE = True
```

**Impact:**  
- Stack traces exposed  
- Potential remote code execution  

**OWASP Category:**  
A05: Security Misconfiguration  

**Fix:**  
- Disable debug mode in production  

---

### 8. Public Exposure (0.0.0.0)

**Issue:**  
Server runs on:

```python
app.run(host="0.0.0.0")
```

**Impact:**  
- Accessible to entire network  

**OWASP Category:**  
A05: Security Misconfiguration  

**Fix:**  

```python
app.run(host="127.0.0.1")
```

---

## Summary  

The API contains multiple critical vulnerabilities including command injection, SQL injection, sensitive data exposure, and insecure authentication. These issues can lead to full system compromise if not fixed. Proper validation, secure coding practices, and configuration management are required to secure the system.

---

## LPI Sandbox Audit (from Level 2 learnings)

- Input validation is inconsistent across tools  
- Some errors are internally logged but still marked as PASS  
- Type validation is missing in multiple places  
- Error handling and reporting can be improved  

---

## LPI Tool Usage

During my testing and analysis, I interacted with multiple LPI tools to understand system behavior and outputs.

### Tools Used

1. **query_knowledge**
   - Input: "digital twin security"
   - Output: Returned structured knowledge about digital twin systems and their risks  
   - Use: Helped understand domain-specific context for vulnerabilities  

2. **get_case_studies**
   - Input: "smart buildings"
   - Output: Provided real-world examples of digital twin applications  
   - Use: Used to connect vulnerabilities with real-world impact scenarios  

3. **get_insights**
   - Input: {"scenario": "personal health digital twin", "tier": "free"}  
   - Output: Generated insights related to digital twin usage in healthcare  
   - Use: Helped analyze potential risks in sensitive domains  

### Summary

These tools helped me:
- Understand real-world applications of digital twins  
- Map vulnerabilities to real-world scenarios  
- Analyze system-level impact  

---

## Conclusion  

The vulnerable API demonstrates how improper input handling, insecure configurations, and lack of validation can lead to critical security issues. Addressing these vulnerabilities is essential for building secure and reliable systems.