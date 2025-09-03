# LangChain CSV Chatbot

A beginner-friendly project that demonstrates how to use LangChain and OpenAI's GPT models to chat with CSV files. This project supports both Command Line and Web (Streamlit) interfaces.

## 🔍 Use Case

This demo shows how LangChain can help you interact with structured data like CSVs using natural language. You can ask questions like:
- "What is the average salary in the Sales department?"
- "List all employees from New York."
- "Which department has the highest average age?"

---

## 📁 Project Structure

langchain-csv-chatbot/
│
├── cli/
│ └── chat_csv.py # CLI-based chatbot
│
├── web/
│ └── app.py # Streamlit UI for CSV chatbot
│
├── data/
│ └── sample.csv # Sample CSV file to test
│
├── .env # API Key file (contains OpenAI key)
├── requirements.txt # Dependencies
├── README.md
└── .gitignore


---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JohnDBSDSN/langchain-csv-chatbot.git
cd langchain-csv-chatbot


**2. Create and activate a virtual environment**
python -m venv .venv
.venv\Scripts\activate  # For Windows

**3. Install dependencies**

pip install -r requirements.txt

**4. Configure your API Key**
Create a .env file in the root directory with the following:
OPENAI_API_KEY=your_openai_api_key_here

💻 **Run the Chatbot**
**Option 1: CLI Interface**

python cli/chat_csv.py

Drag a CSV into the data/ folder and change the path in chat_csv.py if needed.
Then ask: What is the total sales in April?

**Option 2: Streamlit Web Interface**

streamlit run web/app.py

Visit: http://localhost:8501
Upload your CSV and start chatting.

**📌 Key Technologies:**
LangChain: Framework for building LLM-powered apps
OpenAI GPT-4o: For natural language understanding
Pandas: For CSV parsing
Streamlit: For no-code friendly web UI

**⚡ How is LangChain Different?**

While many AI tools can "summarize" or "respond," LangChain:
- Connects external data (like CSVs) dynamically
- Supports agent-based execution (reasoning steps)
- Integrates multiple tools (e.g., Python REPL) under the hood
This gives developers more control, context-awareness, and reasoning capabilities compared to black-box AI tools.

**🧪 Tested On**
Python 3.12
LangChain 0.1.14
OpenAI SDK 1.104.2
Streamlit 1.49.1
Tested: ✅ September 03, 2025
