from shellsensei.sensei.prompts import decision_prompt
from shellsensei.llm.gpt import GPT
from shellsensei.sensei.sensei import get_os
import ast


model = GPT()
task = "Install NginX"

query = decision_prompt.format(OS=get_os(), task=task)

response = model.query(user_prompt=query)
response = ast.literal_eval(response)

print("-" * 60)
print(f"Query is:\n{query}")
print("-" * 60)

print(f"Model response is:\n{response}")
