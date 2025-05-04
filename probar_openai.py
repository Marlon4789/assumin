from openai import OpenAI

client = OpenAI(
  api_key="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"  # Pega aquí tu clave válida (revocada la anterior)
)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "user", "content": "Write a haiku about AI"}
  ]
)

print(completion.choices[0].message.content)
