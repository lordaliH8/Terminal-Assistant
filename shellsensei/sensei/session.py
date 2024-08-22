from shellsensei.sensei import Sensei
from shellsensei.llm import GPT


class Session(Sensei):

    def __init__(self, sensei_id: str):
        super().__init__(sensei_id)
        # TODO: 0. Read API KEY from DB - Raise error if not existing
        # self.model = GPT(OPENAI_API_KEY="")

    # TODO: 1. Fill this
    def starting_command(self, command: str):
        """
        This function is for handling the initial command coming from the user
        It will decide to run a command or ask a question
        :param command: -m "command"
        :return: ?
        """
        # self.initial_decision()
        raise NotImplemented()

    # TODO: 2. Fill this
    def question_response(self):
        """
        This function is for when user has answered a question
        Here we should provide the history to the model and ask it to decide on asking a question or running a command
        :return: ?
        """
        raise NotImplemented()

    # TODO: 3. Fill this
    def command_response_no_output(self):
        """
        This function is for when GPT has executed a command, and does not need/want to see the output
        We should provide history and ask it to decide on asking a question or running a command
        :return:
        """
        raise NotImplemented()

    # TODO: 4. Fill this
    def command_response_with_output(self):
        """
        This function is for when GPT has executed a command, and wants to see the output
        We should provide history and ask it to decide on asking a question or running a command
        :return:
        """
        raise NotImplemented()

    # TODO: 5. Fill this
    def command_response_with_error(self):
        """
        This function is for when GPT has executed a command and that command has raised an error
        We should provide history and ask it to decide on asking a question or running a command
        :return:
        """
        raise NotImplemented()
