import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

while True:
    prompt = input("Enter Your Query (or type 'exit' to quit): ")
    
    if prompt.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an Ai assistant(LLM)"
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        # temperature=0.5
    )

    print("\nAssistant:", chat_completion.choices[0].message.content, "\n")