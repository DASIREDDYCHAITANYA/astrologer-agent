# 🌌 Astrologer Agent

Astrologer Agent is an AI-powered astrology chatbot built using **Flask** and the **Groq LLM API**.  
It takes user queries and generates accurate astrological predictions using **LLaMA-3.3-70B** via Groq.

---

## 🚀 Features
- ✨ Ask astrology-related questions
- 🤖 Powered by **Groq LLM** (LLaMA 3.3-70B Versatile)
- 🌐 Simple Flask-based web UI
- 🔐 Secure API key handling using `.env`

---

## 🛠️ Installation

### **1. Clone the repository**
```bash



git clone https://github.com/DASIREDDYCHAITANYA/astrologer-agent.git
cd astrologer-agent
```
### Project structure
```bash
astrologer-agent/
├── app.py              # Flask application
├── llm.py              # Handles Groq LLM requests
├── templates/
│   └── index.html      # Frontend UI
├── static/             # CSS, JS, images (if any)
├── requirements.txt    # Project dependencies
├── .env                # Store your Groq API key here
└── README.md           # Project documentation
