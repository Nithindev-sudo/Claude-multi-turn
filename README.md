# Claude Multi-Turn Conversation Agent


Hi I'm Nithin
This repository documents my journey of building a **multi-turn conversational AI agent** using the **Anthropic Claude API**.

## 🚀 Current Progress (Step 3)

The project has evolved from a simple API integration into a **context-aware conversational AI agent** with configurable model behavior and real-time response streaming.

### ✅ Implemented

- Connected to the Anthropic Claude API.
- Loaded the API key securely using a `.env` file.
- Sent user messages to Claude.
- Received and displayed Claude's responses.
- Created reusable helper functions for managing messages.
- Implemented conversation history storage.
- Enabled context-aware multi-turn conversations.
- Built a terminal-based interactive chatbot.
- Added support for **System Prompts** to customize the assistant's behavior.
- Added configurable **Temperature** to control response creativity.
- Refactored API calls using a flexible parameter dictionary.
- Implemented **Event Streaming** for real-time response generation.
- Captured the complete streamed response for future storage or processing.
- Established the foundation for building advanced AI agents.

---

## 📂 Current Project Structure

```text
.
├── .github
│   └── workflows
│       └── claude.yml
├── agent.py              # Basic Anthropic API integration
├── MultiTurn.py          # Multi-turn chatbot with system prompts & temperature
├── EventStreaming.py     # Real-time streaming responses using Anthropic SDK
├── .env                  # Stores the Anthropic API key (not committed)
├── .gitignore
└── README.md
```

---

## 🛠 Technologies Used

- Python
- Anthropic Python SDK
- python-dotenv

---

# 🔍 What Has Been Built So Far

## 1️⃣ agent.py

Introduces the fundamentals of working with the Anthropic Messages API.

Features:

- API authentication
- Sending prompts
- Receiving responses
- Helper functions for messages
- Conversation history management

This file explains how Claude remembers previous interactions by sending the complete conversation history with every request.

---

## 2️⃣ MultiTurn.py

Implements an interactive terminal chatbot.

### Features

- Infinite chat loop
- Conversation memory
- Context-aware responses
- Empty input validation
- Reusable helper functions

### System Prompt Support

The chatbot can now control Claude's behavior using a **system prompt**.

Example:

```python
system_prompt="You are a director of big movies giving advice."
```

Instead of hardcoding the system prompt, the project dynamically adds it only when one is provided.

This makes the chat function reusable for different assistant personalities.

### Temperature Control

The chatbot also supports configurable temperature.

```python
temperature=1.0
```

Temperature controls the randomness of Claude's responses.

| Temperature | Use Case |
|-------------|----------|
| 0.0 – 0.3 | Factual answers, coding, data extraction |
| 0.4 – 0.7 | Summarization, education, problem solving |
| 0.8 – 1.0 | Brainstorming, creative writing, marketing |

---

## 3️⃣ EventStreaming.py

Demonstrates how to stream Claude's response in real time.

Instead of waiting for the entire response, Claude sends the output as small chunks.

Benefits include:

- Faster perceived response time
- Better user experience
- Real-time text generation

The project also demonstrates:

- Raw streaming events
- Extracting only the generated text
- Using `stream.text_stream`
- Collecting the final message using

```python
stream.get_final_message()
```

This can later be stored in a database or conversation history.

---

## 🎯 Roadmap

This repository will gradually evolve into a fully functional AI agent.

### Completed

- [x] Connect to Claude API
- [x] Generate a response from a user prompt
- [x] Maintain conversation history
- [x] Implement multi-turn conversations
- [x] Create reusable conversation/session management
- [x] Add configurable System Prompts
- [x] Add Temperature parameter
- [x] Implement response streaming

### Upcoming

- [ ] Improve error handling
- [ ] Conversation reset command
- [ ] Persist chat history
- [ ] Token usage tracking
- [ ] Tool Calling
- [ ] MCP (Model Context Protocol)
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Memory management
- [ ] Advanced AI agent workflows

---

## 💡 Purpose

The goal of this project is not just to build an AI chatbot, but to understand how modern AI agents work internally—from simple API calls to persistent conversations, configurable model behavior, response streaming, tool use, and intelligent workflows.

Each commit represents a new learning milestone, making it easy to follow the project's evolution over time.

---

# 📈 Current Status

| Phase | Status |
|--------|--------|
| Claude API Integration | ✅ Completed |
| Multi-Turn Conversation Memory | ✅ Completed |
| Interactive Chat Interface | ✅ Completed |
| System Prompt Engineering | ✅ Completed |
| Temperature Control | ✅ Completed |
| Event Streaming | ✅ Completed |
| Advanced Agent Features | 🔄 In Progress |

---

## 📚 Concepts Learned

During this project, the following Anthropic concepts have been implemented:

- Anthropic Messages API
- Multi-turn conversations
- Conversation history
- System Prompts
- Temperature parameter
- Event Streaming
- Dynamic parameter handling
- Terminal chatbot development

---

> **Current Milestone:** The project now supports **context-aware conversations**, **customizable assistant behavior using system prompts**, **temperature-controlled responses**, and **real-time streaming**, providing a strong foundation for building advanced AI agents with Tool Calling, MCP, and memory systems.
