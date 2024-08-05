from datetime import datetime

from llm import GPT


class Sensei:

    def __init__(self, sensei_id: str):
        self.sensei_id = sensei_id
        self.created_at = datetime.now()
        self.model = GPT()

    def initial_decision(self, query: str) -> dict:
        # TODO: Fill
        # self.model.query...
        pass

    def ask(self, query: str) -> dict:
        # TODO: 1. Run a command or ask a question
        # response = self.initial_decision(query)
        # command, question = respons['command'], respons['question']
        pass


