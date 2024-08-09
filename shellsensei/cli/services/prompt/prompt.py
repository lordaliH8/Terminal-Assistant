# Imports
import os
import sys
import getopt
from shellsensei.sensei import Sensei

sensei = Sensei(sensei_id="test")


# Prompt Handler
def prompt_handler(currentArgs, values):
    if len(values) != 0:
        raise getopt.error("too many arguments")
    else:
        msg = currentArgs
        response = sensei.ask(msg)
        print(response)
        while True:
            # Question
            if response["question"]:
                print(response["question"])
                response_type = "question"
                user_answer = input(response["question"] + " ")
                print(user_answer)
                sensei.generate_history(
                    key=response["question"], value=user_answer, type=response_type
                )
                print("question history ~>", sensei.question_history)
                break
            # Command
            elif response["command"]:
                response_type = "command"
                print(response["command"])
                sensei.generate_history(
                    key=response["command"], value="OK", type=response_type
                )
                print("command history ~>", sensei.command_history)
                # execute(response["command"])
                user_answer = input("You want to Ask another Request? [y/n] ")
                while True:
                    match user_answer:
                        case "y" | "Y":
                            user_prompt = input("Your Request ~> ")
                            response = sensei.ask(user_prompt)
                            break
                        case "n" | "N":
                            sys.exit()
                        case _:
                            user_answer = input("Please Answer with Y or N: [y/n] ")
            else:
                raise getopt.error("WTF")


# Execute Shell Command
def execute(command):
    os.system(command)
