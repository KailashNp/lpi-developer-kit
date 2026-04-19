# Level 3 Submission — Abhinav Chaudhary

## 🚀 Overview

I built a simple AI agent that simulates how an LPI agent works by analyzing a user query, selecting relevant tools, and combining their outputs into a structured response.

Instead of directly calling the MCP server, I designed lightweight tool functions to demonstrate the reasoning and orchestration logic of an agent.

---

## 🧠 Architecture

User Input → Query Analysis → Tool Selection → Tool Execution → Aggregation → Final Response

---

## ⚙️ LPI Tools Used (Simulated)

### 1. get_case_studies

* Purpose: Provide real-world examples
* Output: Returns a case-study style explanation of the query

### 2. query_knowledge

* Purpose: Provide conceptual understanding
* Output: Returns theoretical explanation based on LPI concepts

---

## 🔄 Agent Flow

1. User inputs a question
2. Agent analyzes keywords in query
3. Selects relevant tools dynamically
4. Calls each tool
5. Collects outputs
6. Combines into structured answer

---

## 💡 Design Decisions

* I ensured at least **2 tools are always used**, even for vague queries
* I separated **reasoning, answer, and sources** for explainability
* I avoided external dependencies to keep the agent simple and stable

---

## 🔧 What I Would Improve

* Integrate real MCP tool calls instead of simulated ones
* Improve tool selection using LLM instead of keyword matching
* Add memory/context handling for multi-turn queries

---

## 💻 Repository

https://github.com/abhinavchaudhary256-sudo/lpi-agent-abhinav

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python agent.py
```

---

## 📌 Example

**Input:** What is SMILE?

**Output:**

* Case Study: Real-world implementation of SMILE
* Knowledge: Explanation based on LPI methodology

---

## ✅ Checklist

* [x] Built custom agent
* [x] Uses multiple tools
* [x] Structured output
* [x] Explainability included
* [x] Separate repo created

Signed-off-by: Abhinav Chaudhary
