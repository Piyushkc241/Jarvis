from openai import OpenAI

client=OpenAI(

    # needs to buy this api for further working and same as news api
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and Google Cloud."},
        {
            "role": "user",
            "content": "What is coding"
        }
    ]
)

print(completion.choices[0].message.content)