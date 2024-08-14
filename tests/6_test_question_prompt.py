from shellsensei.sensei.prompts import question_prompt
from shellsensei.llm.gpt import GPT
from shellsensei.sensei.sensei import get_os
import ast


model = GPT()
task = "remove one of my docker images"
question_history = {
    "0s": ["Which docker image do you want to remove?", "jenkins"],
    "2s": ["Are you sure you want to remove the docker image 'jenkins'? (yes/no)", "yes"],
}
"""
question_history = {
    "0s": ["What is the operating system?", "Ubuntu"],
    "5s": ["What task would you like to perform?", "Install Python"],
    "10s": ["Do you want to install a specific version of Python?", "Yes, Python 3.8"],
    "15s": ["Do you want to include pip?", "Yes"],
}
"""

query = question_prompt.format(
    OS=get_os(), task=task, question_history=question_history
)

response = model.query(user_prompt=query)
response = ast.literal_eval(response)

print("-" * 60)
print(f"Query is:\n{query}")
print("-" * 60)

print(f"Model response is:\n{response}")
