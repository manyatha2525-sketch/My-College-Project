import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API key not found!")
    exit()

model = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    google_api_key=api_key
)

prompt = ChatPromptTemplate.from_template(
    "You are a helpful Python tutor. Answer this question in simple language:\n{question}"
)

chain = prompt | model

print("====================================")
print("   PYTHON DOUBT SOLVER CHATBOT")
print("====================================")
print("Type 'exit' to stop.\n")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question.strip():
        print("Please enter a question.")
        continue

    try: 
        response = chain.invoke({"question": question})

        if isinstance(response.content, list):
            answer = "\n".join(
                block["text"]
                for block in response.content
                if block.get("type") == "text"
            )
        else:
            answer = response.content

        print("\nAI:", answer)

    except Exception as e:
        print("\nError:", e)
        print()