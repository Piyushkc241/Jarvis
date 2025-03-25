from openai import OpenAI

client=OpenAI(

    # needs to buy this api for further working and same as news api
    api_key=""
    ,
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