import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

# Load environment variables from .env file
load_dotenv()

# Path to your CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "sample.csv")
csv_path = os.path.abspath(csv_path)

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Create the CSV agent
agent = create_csv_agent(llm, csv_path, verbose=True)

# Run chatbot loop
print("\n💬 Chat with your CSV (type 'exit' to quit)\n")
while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    response = agent.run(query)
    print("Bot:", response, "\n")
