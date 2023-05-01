# pip install openai
import os
import openai
#pegar aqui lo del env
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-0301",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)