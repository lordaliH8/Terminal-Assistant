# Imports
import getopt


# Prompt Handler
def prompt_handler(currentArgs, values, sensei):
    if len(values) != 0:
        raise getopt.error("too many arguments")
    else:
        msg = currentArgs
        response = sensei.ask(msg)
        print(response)
        while True:
            if response["question"]:
                print(response["question"])
                user_answer = input(response["question"] + " ")
                print(user_answer)
                break
            elif response["command"]:
                print(response["command"])
                # service.execute(response["command"])
                break
            else:
                raise getopt.error("WTF")
