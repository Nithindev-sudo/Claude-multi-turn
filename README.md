# Claude Multi-Turn Conversation Agent

This repository documents my journey of building a **multi-turn conversational AI agent** using the **Anthropic Claude API**.

## 🚀  Progress (Step 1) completed ✅

# Claude Multi-Turn Conversation Agent

This repository documents my journey of building a **multi-turn conversational AI agent** using the **Anthropic Claude API**.

## 🚀 Current Progress (Step 2)

The project has now progressed beyond simple request-response interactions and supports **multi-turn conversations** by maintaining conversation history and sending it back to Claude with each API call.

### ✅ Implemented

* Connected to the Anthropic Claude API.
* Loaded the API key securely using a `.env` file.
* Sent user messages to Claude.
* Received and displayed Claude's responses.
* Created reusable helper functions for managing messages.
* Implemented conversation history storage.
* Enabled context-aware multi-turn conversations.
* Built a terminal-based interactive chatbot.
* Established the foundation for future agent development.

## 📂 Current Project Structure

```text
.
├── .github
│   └── workflows
│       └── claude.yml
├── agent.py          # Demonstrates how multi-turn conversations work
├── MultiTurn.py      # Interactive terminal chatbot with conversation memory
├── .env              # Stores the Anthropic API key (not committed)
├── .gitignore
└── README.md
```

## 🛠 Technologies Used

* Python
* Anthropic Python SDK
* python-dotenv

## 🔍 What Has Been Built So Far

### agent.py

This file demonstrates the core concept behind multi-turn conversations.

It:

* Creates and stores conversation history.
* Sends the entire message history to Claude.
* Preserves context between user interactions.
* Demonstrates how Claude can answer follow-up questions using previous responses.

Example:

User: What is 2 + 3?

Claude: Five

User: What will be the answer if we add 7 more to the sum you have given previously?

Claude: Twelve

### MultiTurn.py

This file implements a simple terminal chatbot.

Features:

* Continuous chat loop.
* Conversation memory.
* Context-aware responses.
* Input validation for empty messages.
* Reusable helper functions for message management.

## 🎯 Roadmap

This repository will gradually evolve into a fully functional AI agent. Planned milestones include:

* [x] Connect to Claude API
* [x] Generate a response from a user prompt
* [x] Maintain conversation history
* [x] Implement multi-turn conversations
* [x] Create reusable conversation/session management
* [ ] Improve error handling
* [ ] Add conversation reset functionality
* [ ] Persist chat history to files or databases
* [ ] Add streaming responses
* [ ] Add tool calling support
* [ ] Integrate MCP (Model Context Protocol)
* [ ] Build more advanced agent capabilities
* [ ] Explore memory and context management

## 💡 Purpose

The goal of this project is not just to build an AI chatbot, but to understand how modern AI agents work internally—from simple API calls to persistent conversations, tool use, memory management, and intelligent workflows.

Each commit represents a new learning milestone, making it easy to follow the project's evolution over time.

## 📈 Current Status

**Phase 1 — Claude API Integration:** ✅ Completed

**Phase 2 — Multi-Turn Conversation Memory:** ✅ Completed

**Phase 3 — Interactive Chat Interface:** 🔄 In Progress

**Phase 4 — Advanced Agent Features:** To be done 

---

**The project now supports context-aware multi-turn conversations and serves as the foundation for building more advanced AI agent capabilities in future updates.**

