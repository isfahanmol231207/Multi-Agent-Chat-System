# Simple Multi‑Agent Chat System

## 📌 Overview

This project implements a **minimal Multi‑Agent Chat System** for the *Knowledge Representation and Reasoning (KRR) – Assignment 03*. The system demonstrates how a **Coordinator (Manager) Agent** orchestrates multiple specialized agents to collaboratively answer user queries, maintain memory, and adapt based on prior interactions.

The system is console‑based and focuses on **agent coordination, structured memory, and traceable reasoning**, rather than high‑accuracy NLP.

---

## 🧠 System Architecture

**Agents Involved:**

1. **Coordinator (Manager) Agent**

   * Receives user queries
   * Performs basic complexity analysis
   * Decomposes tasks and routes them to worker agents
   * Merges results and produces the final response
   * Handles fallback and memory retrieval

2. **ResearchAgent**

   * Simulates information retrieval using a mock knowledge base
   * Returns basic factual content with confidence

3. **AnalysisAgent**

   * Performs comparison, reasoning, and summarization on research data
   * Produces synthesized insights

4. **MemoryAgent**

   * Stores structured findings (topic, content, agent, timestamp, confidence)
   * Retrieves prior knowledge to avoid redundant work

```
User Query
   ↓
Coordinator (Planner)
   ↓
┌───────────────┬───────────────┬───────────────┐
│ ResearchAgent │ AnalysisAgent │  MemoryAgent  │
└───────────────┴───────────────┴───────────────┘
```

---

## 🗂️ Project Structure

```
Multi-Agent Chat System/
│
├── agents/
│   ├── coordinator.py
│   ├── research_agent.py
│   ├── analysis_agent.py
│   └── memory_agent.py
│
├── outputs/
│   ├── simple_query.txt
│   ├── complex_query.txt
│   ├── multi_step.txt
│   ├── collaborative.txt
│   └── memory_test.txt
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How the System Works

1. User query is passed to the **Coordinator**
2. Coordinator performs **keyword‑based planning**
3. Tasks are routed to agents in sequence:

   * Research → Analysis → Memory Storage
4. Results are merged and returned
5. Findings are stored in memory for future reuse

All agent calls and decisions are printed to the console for **traceability**.

---

## 🧪 Test Scenarios (Required)

The following assignment‑required scenarios are implemented and executed automatically:

1. **Simple Query**
   `What are the main types of neural networks?`

2. **Complex Query**
   `Research transformer architectures, analyze their computational efficiency, and summarize key trade‑offs.`

3. **Multi‑Step Query**
   `Find recent papers on reinforcement learning, analyze their methodologies, and identify common challenges.`

4. **Collaborative Query**
   `Compare two machine‑learning approaches and recommend which is better for our use case.`

5. **Memory Test**
   `What did we discuss about neural networks earlier?`

Each scenario’s console trace is saved in the **outputs/** directory.

---

## 🧠 Memory Design

The memory system stores **structured records**, including:

* Topic
* Content
* Agent name
* Confidence score
* Timestamp

Memory retrieval uses **keyword matching** to demonstrate context awareness and reuse of prior knowledge.

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the System

```bash
python main.py
```

All test scenarios will execute automatically and generate output files.

---

## 📦 Outputs Folder Requirement

The `outputs/` directory contains saved console traces for all required scenarios, as mandated by the assignment instructions.

---

## 🛠️ Technologies Used

* Python 3.10
* Object‑Oriented Programming
* Rule‑based task decomposition
* Structured in‑memory storage

---




