import os
from groq import Groq


def main():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Please set your GROQ_API_KEY environment variable.")
        return

    client = Groq(api_key=api_key)

    print("Groq Chat CLI. Type 'quit' to exit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
        )

        answer = response.choices[0].message.content
        print(f"Assistant: {answer}\n")


if __name__ == "__main__":
    main()
