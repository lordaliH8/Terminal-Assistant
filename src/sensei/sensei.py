from datetime import datetime


class Sensei:

    def __init__(self, sensei_id: str):
        self.sensei_id = sensei_id
        self.created_at = datetime.now()

    def initial_decision(self, query: str) -> dict:
        # TODO: Fill
        pass

    def ask(self, query: str) -> dict:
        # TODO: 1. Run a command or ask a question
        # response = self.initial_decision(query)
        # command, question = respons['command'], respons['question']
        pass


