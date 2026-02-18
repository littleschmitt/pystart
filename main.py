from groq import Groq

client = Groq(api_key='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')

while(True):
    answer = input("What can I do for you? ")

    if(answer == "Everything"):
        print("No, that's a lot of work.")
        break
    
    completion = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
          {
            "role": "user",
            "content": answer
          }
        ],
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        stream=False,
        stop=None
    )

    print(completion.choices[0].message.content)
    print()
