# Claude Multi-Turn Conversation Agent

This repository documents my journey of building a **multi-turn conversational AI agent** using the **Anthropic Claude API**.

## 🚀 Current Progress (Step 1)

The project is currently in its initial stage.

### ✅ Implemented

* Connected to the Anthropic Claude API.
* Loaded the API key securely using a `.env` file.
* Sent a user message to Claude.
* Received and displayed the model's response.
* Established the basic request-response workflow that will serve as the foundation for future development.

## 📂 Current Project Structure

```text
.
├── agent.py          # Sends a prompt to Claude and prints the response
├── .env              # Stores the Anthropic API key (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## 🛠 Technologies Used

* Python
* Anthropic Python SDK
* python-dotenv

## 🎯 Roadmap

This repository will gradually evolve into a fully functional multi-turn AI agent. Planned milestones include:

* [x] Connect to Claude API
* [x] Generate a response from a user prompt
* [ ] Maintain conversation history
* [ ] Implement multi-turn conversations
* [ ] Create reusable conversation/session management
* [ ] Add tool calling support
* [ ] Integrate MCP (Model Context Protocol)
* [ ] Build more advanced agent capabilities
* [ ] Explore memory and context management

## 💡 Purpose

The goal of this project is not just to build an AI chatbot, but to understand how modern AI agents work internally—from simple API calls to persistent conversations, tool use, and intelligent workflows.

Each commit will represent a new learning milestone, making it easy to follow the project's evolution over time.

---

**This is the first commit of the project. More features, improvements, and experiments will be added in future updates.**
