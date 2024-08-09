import ast
from datetime import datetime
import platform
import distro
from shellsensei.llm import GPT
from shellsensei.sensei.prompts import decision_prompt


def get_os():
    os_name = platform.system()
    if os_name == "Linux":
        distro_name , os_version = distro.name(),distro.version()
        return f"{os_name} ({distro_name} {os_version})"
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
        self.task = str()
        self.command_history = dict()
        self.question_history = dict()
        self.scenario = str()

    def get_elapsed_time(self):
        elapsed = datetime.now() - self.created_at
        seconds = int(elapsed.total_seconds())
        milliseconds = int(elapsed.microseconds / 1000)
        microseconds = elapsed.microseconds % 1000
        return f"{seconds}:{milliseconds:03d}:{microseconds:03d}"  # Format as second:millisecond:microsecond

    def add_command(self, command, response):
        elapsed_time = self.get_elapsed_time()
        self.command_history[elapsed_time] = [command, response]

    def add_question(self, question, response):
        elapsed_time = self.get_elapsed_time()
        self.question_history[elapsed_time] = [question, response]

    def generate_history(self, key, value, type):
        if type == "question":
            self.add_question(key, value)
        elif type == "command":
            self.add_command(key, value)

    def generate_chat_scenario(self,command_history, question_history):
        combined_history = {**command_history, **question_history}

        if not combined_history:
            return f"(user):{self.task}\n(TA): This will be your response (command | question)"

        sorted_keys = sorted(combined_history.keys())
        scenario_lines = []
        scenario_lines.append(f"(user): {self.task}")

        for key in sorted_keys:
            ta_text, user_text = combined_history[key]
            scenario_lines.append(f"(TA): {ta_text}")
            scenario_lines.append(f"(user): {user_text}")

        scenario_lines.append("(TA): This will be your response (command | question)")

        scenario_text = "\n".join(scenario_lines)

        return scenario_text


    def initial_decision(self) -> dict:
        # TODO: Fill
        query = decision_prompt.format(OS=get_os(), task=self.task ,chat_scenario = self.scenario)
        print("%"* 60)
        print(query)
        print("%" * 60)
        response = self.model.query(user_prompt=query)
        response = ast.literal_eval(response)
        return response

    def ask(self) -> dict:
        # 1. Run a command or ask a question
        response = self.initial_decision()
        return response
