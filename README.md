# 🤖 Groq LLM CLI Chatbot

A simple and powerful **command-line chatbot** built with the [Groq API](https://console.groq.com/) using the **LLaMA 3.3–70B Versatile model**. This project allows you to have real-time, intelligent conversations with a large language model directly from your terminal.

---

## 📌 Features

* ⚡ Powered by `llama-3.3-70b-versatile` from Groq
* 🧠 Context-aware assistant replies
* 🔐 Loads API key securely from `.env`
* 💬 Continuous chat loop via terminal
* 🛠 Minimal and extendable code structure

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/groq-cli-chatbot.git
cd groq-cli-chatbot
```

### 2. Install dependencies

```bash
pip install groq python-dotenv
```

### 3. Set up your `.env` file

Create a `.env` file in the root directory and add your [Groq API key](https://console.groq.com/):

```
GROQ_API_KEY=your_groq_api_key_here
```

### 4. Run the chatbot

```bash
python chatbot.py
```

---

## 💾 Project Structure

```
groq-cli-chatbot/
│
├── chatbot.py          # Main chatbot script
├── .env                # API key (not committed)
├── README.md           # Project documentation
└── requirements.txt    # Optional: dependencies list
```

---

## 🧠 Example Conversation

```
Enter Your Query (or type 'exit' to quit): What is the capital of Japan?
Assistant: The capital of Japan is Tokyo.

Enter Your Query (or type 'exit' to quit): exit
Goodbye!
```

---

## 📄 License

This project is proprietary and confidential. All rights reserved.

```
© 2025 HUSSAIN ALI. This code may not be copied, modified, distributed, or used without explicit permission.
```

---

## 📬 Contact

For questions or collaboration requests:

* 📧 Email: [choudaryhussainali@outlook.com](mailto:choudaryhussainali@outlook.com)
* 🌐 GitHub: [choudaryhussainali](https://github.com/choudaryhussainali)

---

> ✨ Built using [Groq](https://groq.com) and the blazing-fast LLaMA models
