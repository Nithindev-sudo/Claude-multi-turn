# Claude Multi-Turn Conversation Agent

This repository documents my journey of building a **multi-turn conversational AI agent** using the **Anthropic Claude API**. Starting from basic API integration, the project gradually evolves into a production-style AI agent by implementing conversation memory, prompt engineering, streaming responses, evaluation workflows, and tool use.

---

# 🚀 Current Progress (Step 3)

The project has evolved beyond simple request-response interactions into a **context-aware conversational AI agent** with configurable model behavior and real-time streaming.

## ✅ Implemented

- Connected to the Anthropic Claude API.
- Loaded API credentials securely using `.env`.
- Built reusable helper functions for message management.
- Implemented conversation history for multi-turn interactions.
- Created an interactive terminal chatbot.
- Added configurable **System Prompts**.
- Added configurable **Temperature** settings.
- Refactored API calls using dynamic parameter dictionaries.
- Implemented **Event Streaming** using the Anthropic SDK.
- Captured streamed responses for future storage or processing.

---

# 📂 Current Project Structure

```text
.
├── .github
│   └── workflows
│       └── claude.yml
├── agent.py
├── MultiTurn.py
├── EventStreaming.py
├── .env
├── .gitignore
└── README.md
```

---

# 🛠 Technologies Used

- Python
- Anthropic Python SDK
- python-dotenv

---

# 📖 Project Modules

## 📌 agent.py

Introduces the basics of working with the Anthropic Messages API.

### Features

- API authentication
- Sending prompts
- Receiving responses
- Conversation history
- Multi-turn context

---

## 💬 MultiTurn.py

Implements an interactive terminal chatbot.

### Features

- Continuous chat loop
- Conversation memory
- Input validation
- Dynamic system prompts
- Configurable temperature
- Reusable chat functions

### System Prompt Example

```python
system_prompt="You are a director of big movies giving advice."
```

Instead of hardcoding the prompt, the project dynamically adds the system prompt only when provided.

### Temperature

The chatbot supports configurable temperature values.

| Temperature | Typical Use Cases |
|-------------|-------------------|
| 0.0 – 0.3 | Factual responses, coding, data extraction |
| 0.4 – 0.7 | Summarization, education, problem solving |
| 0.8 – 1.0 | Brainstorming, creative writing, marketing |

---

## ⚡ EventStreaming.py

Demonstrates Anthropic's streaming API.

Instead of waiting for the entire response, Claude streams text token-by-token.

### Features

- Real-time response streaming
- Cleaner streaming using `stream.text_stream`
- Access to raw streaming events
- Collecting the final generated response

```python
answer = stream.get_final_message()
```

The final message can later be stored in databases or conversation history.

---

# 📚 Concepts Learned

## Prompt Engineering

- ✅ Being clear and direct
- ✅ Being specific
- ⏳ XML prompt structuring
- ⏳ Few-shot prompting
- ⏳ Prompt engineering exercises

---

## System Prompts

Implemented dynamic system prompts to control Claude's personality and behavior without changing application logic.

---

## Temperature

Learned how temperature influences response creativity.

- Low Temperature → deterministic
- Medium Temperature → balanced
- High Temperature → creative

---

## Event Streaming

Implemented streaming responses to improve user experience and reduce perceived latency.

---

# 📈 Learning Progress

## Prompt Evaluation (Currently Learning)

Learning how to evaluate prompt quality using structured evaluation workflows.

### Evaluation Workflow

1. Draft a prompt
2. Create an evaluation dataset
3. Generate responses with Claude
4. Grade the outputs
5. Improve the prompt and repeat

This iterative workflow helps improve prompt quality using measurable evaluation criteria.

---

## Evaluation Criteria

Understanding how prompts should be evaluated using:

### Format

- Correct output format
- No unnecessary explanations

### Valid Syntax

- Valid Python
- Valid JSON
- Valid Regular Expressions

### Task Following

- Correctly follows user instructions
- Produces accurate outputs

---

## Prompt Graders

Learning different grading approaches.

### Code Grader

Used for automatically checking:

- Output length
- Syntax validation
- Required keywords
- Readability

### Model Grader

Uses an LLM to evaluate:

- Response quality
- Instruction following
- Completeness
- Helpfulness
- Safety

### Human Grader

Manual evaluation of:

- Relevance
- Conciseness
- Comprehensiveness
- Overall response quality

---

# 🔜 Upcoming Topics

The following Anthropic concepts will be implemented in future commits.

## Prompt Engineering

- [ ] XML Prompt Structure
- [ ] Few-shot Prompting
- [ ] Prompt Evaluation Framework

## Tool Use

- [ ] Tool Functions
- [ ] Tool Schemas
- [ ] Handling Message Blocks
- [ ] Sending Tool Results
- [ ] Multi-turn Tool Conversations
- [ ] Multiple Tool Calling
- [ ] Fine-Grained Tool Calling
- [ ] Text Editing Tool
- [ ] Web Search Tool

---

## Tool Use Workflow

Upcoming implementations will follow Anthropic's Tool Use pattern:

```
User
   │
   ▼
Our Server ─────────► Claude
        ▲              │
        │              ▼
 Execute Tool ◄──── Tool Request
        │
        ▼
Return Tool Result
        │
        ▼
Claude generates final response
```

This enables Claude to request external information, execute tools through the application, and generate an augmented final response.

---

# 🎯 Roadmap

### Completed

- [x] Claude API Integration
- [x] Secure API Key Management
- [x] Multi-turn Conversations
- [x] Conversation History
- [x] Interactive CLI Chatbot
- [x] System Prompts
- [x] Temperature Control
- [x] Event Streaming

### In Progress

- [ ] Prompt Evaluation
- [ ] Code Graders
- [ ] Model Graders

### Planned

- [ ] Tool Calling
- [ ] MCP (Model Context Protocol)
- [ ] Multiple Tools
- [ ] Memory Management
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Persistent Conversation Storage
- [ ] Advanced AI Agent Workflows

---

# 💡 Purpose

The objective of this repository is to learn how modern AI agents are built—from simple API calls to advanced conversational systems with memory, prompt engineering, evaluation workflows, streaming, and external tool integration.

Each commit represents a new learning milestone, making it easy to follow the project's evolution over time.

---

# 📊 Current Status

| Phase | Status |
|--------|--------|
| Claude API Integration | ✅ Completed |
| Multi-turn Conversation Memory | ✅ Completed |
| Interactive Chatbot | ✅ Completed |
| System Prompt Engineering | ✅ Completed |
| Temperature Control | ✅ Completed |
| Event Streaming | ✅ Completed |
| Prompt Evaluation | 🔄 Learning |
| Tool Use | ⏳ Upcoming |
| Advanced Agent Development | 🔄 In Progress |

---

> **Current Milestone:** The project now supports **context-aware conversations**, **dynamic system prompts**, **temperature-controlled responses**, and **real-time event streaming**. The next phase focuses on **prompt evaluation**, **grading strategies**, and **tool use**, laying the foundation for building production-ready AI agents.
