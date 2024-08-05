import ast
from datetime import datetime
import platform

from llm import GPT
from sensei.prompts import decision_prompt


def get_os():
    os_name = platform.system()
    if os_name == "Linux":
        os_details = platform.linux_distribution()
        return f"{os_name} ({os_details[0]} {os_details[1]})"
    elif os_name == "Darwin":
        return "macOS"
    elif os_name == "Windows":
        return f"{os_name} ({platform.release()})"
    else:
        return "Unknown"


class Sensei:

    def __init__(self, sensei_id: str):
        self.sensei_id = sensei_id
        self.created_at = datetime.now()
        self.model = GPT()

    def initial_decision(self, query: str) -> dict:
        # TODO: Fill
        query = decision_prompt.format(OS=get_os(), task=query)
        response = self.model.query(user_prompt=query)
        response = ast.literal_eval(response)
        return response

    def ask(self, query: str) -> dict:
        # 1. Run a command or ask a question
        response = self.initial_decision(query)
        return response
