import ast
from datetime import datetime
import platform
import distro
from shellsensei.llm import GPT
from shellsensei.sensei.prompts import decision_prompt


def get_os():
    os_name = platform.system()
    if os_name == "Linux":
        os_details = distro.linux_distribution(full_distribution_name=False)
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
        self.command_history = dict()
        self.question_history = dict()
    def add_command(self,command,response):
        self.command_history[command] = response

    def add_question(self,question,response):
        self.question_history[question] = response

    def generate_history(self,key,value,type):
        if type == "question":
            self.add_question(key,value)
        elif type == "command":
            self.add_command(key,value)

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
