# Imports
import subprocess
import sys
import getopt
from datetime import datetime
from shellsensei.cli.services.config import config
from shellsensei.sensei import Sensei
from shellsensei.db import db

sensei = Sensei(sensei_id="test")


# Prompt Handler
def prompt_handler(currentArgs, values):
    if len(values) != 0:
        raise getopt.error("too many arguments")
    else:
        sensei.task = currentArgs
        response = sensei.ask()
        print(response)
        while True:
            # Question
            if response["question"]:
                response_type = "question"
                user_answer = input(response["question"] + " ")
                sensei.generate_history(
                    key=response["question"], value=user_answer, type=response_type
                )
                print("question history ~>", sensei.question_history)
                response = sensei.question()
            # Command
            elif response["command"]:
                response_type = "command"
                sensei.generate_history(
                    key=response["command"], value="OK", type=response_type
                )
                print("command history ~>", sensei.command_history)
                # output = execute(response["command"])
                db.write_command(
                    command_text=response["command"],
                    output_text="OK",
                    date=datetime.now(),
                    db_url=config.get_location(),
                )
                user_answer = input("You want to Ask another Request? [y/n] ")
                while True:
                    match user_answer:
                        case "y" | "Y":
                            sensei.question_history.clear()
                            sensei.command_history.clear()
                            sensei.task = input("Your Prompt ~> ")
                            response = sensei.ask()
                            break
                        case "n" | "N":
                            sys.exit()
                        case _:
                            user_answer = input("Please Answer with Y or N: [y/n] ")
            else:
                raise getopt.error("WTF")


# Execute Shell Command and Get Output
def execute(command):
    output = subprocess.getoutput(command)
    return output
