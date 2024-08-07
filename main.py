# Imports
import getopt
import sys
from shellsensei.cli import service
from shellsensei.db import db
from shellsensei.sensei import Sensei

sensei = Sensei(sensei_id="test")


if __name__ == "__main__":

    # Arguments - Remove 1st Argument from the List
    argsList = sys.argv[1:]

    # Short Options
    shortopts = "hvm:"

    # Long Options
    longopts = ["help", "version", "msg=", "config=", "import=", "show=", "remove"]

    try:
        # Parsing Argument(s)
        opts, values = getopt.getopt(argsList, shortopts, longopts)

        # Checking Each Arguments
        for currentOpts, currentArgs in opts:

            # Switch Case currentOpts Variable
            match currentOpts:

                # Help Handler
                case "-h" | "--help":
                    if len(argsList) != 1:
                        raise getopt.error("too many arguments")
                    else:
                        service.show_help()

                # Version Handler
                case "-v" | "--version":
                    if len(argsList) != 1:
                        raise getopt.error("too many arguments")
                    else:
                        service.show_version()

                # Message Handler
                case "-m" | "--msg":
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
                                break
                            else:
                                raise getopt.error("WTF")

                # Config Handler
                case "--config":
                    # Switch Case on currentArgs Variable
                    match currentArgs:
                        case "init":
                            if len(argsList) != 2:
                                raise getopt.error("too many arguments")
                            else:
                                db.init()
                        case "location":
                            if len(argsList) != 2:
                                raise getopt.error("too many arguments")
                            else:
                                service.show_location()
                        case "rm" if values[0] == "cmd" and len(values) == 1:
                            db.clean_cmd_table()
                        case "rm" if values[0] == "prompt" and len(values) == 1:
                            print("dadas")
                            db.clean_prompt_table()
                        case "reset":
                            if len(argsList) != 2:
                                raise getopt.error("too many arguments")
                            db.reset()
                    # Error Handling for "Too Many Arguments"
                    if len(values) > 1:
                        raise getopt.error("too many arguments")
                    # Error Handling for "Wrong Arguments"
                    elif currentArgs not in ("init", "location", "rm", "reset"):
                        raise getopt.error("wrong argument")

                # Import Handler
                case "--import":
                    if len(values) != 0:
                        raise getopt.error("too many arguments")
                    else:
                        api_key = currentArgs
                        check = db.check_if_api_key_exists()
                        if check:
                            user_answer = input(
                                "API Key Exists - Want to Replace this API Key with the Old One? [y/n] "
                            )
                            while True:
                                match user_answer:
                                    case "y" | "Y":
                                        db.clean_gpt_table()
                                        db.import_gpt_api_key(api_key)
                                        break
                                    case "n" | "N":
                                        sys.exit()
                                    case _:
                                        user_answer = input(
                                            "Please Answer with Y or N: [y/n] "
                                        )
                        else:
                            db.import_gpt_api_key(api_key)

                # Show Handler
                case "--show":
                    # Switch Case on currentArgs Variable
                    match currentArgs:
                        # CMD
                        case "cmd" if len(values) == 0:
                            limit = 1
                            db.show_cmd_table(limit)
                        case "cmd" if len(values) == 1:
                            limit = int(values[0])
                            db.show_cmd_table(limit)
                        # Prompt
                        case "prompt" if len(values) == 0:
                            limit = 1
                            db.show_prompt_table(limit)
                        case "prompt" if len(values) == 1:
                            limit = int(values[0])
                            db.show_prompt_table(limit)
                    # Error Handling for "Too Many Arguments"
                    if len(values) > 1:
                        raise getopt.error("too many arguments")
                    # Error Handling for "Wrong Arguments"
                    elif currentArgs not in ("cmd", "prompt"):
                        raise getopt.error("wrong argument")

                # Remove Handler
                case "--remove":
                    if len(argsList) != 1:
                        raise getopt.error("too many arguments")
                    else:
                        user_answer = input(
                            "Are you Sure you want to Delete your GPT API Key? [y/n] "
                        )
                        while True:
                            match user_answer:
                                case "y" | "Y":
                                    db.clean_gpt_table()
                                    break
                                case "n" | "N":
                                    sys.exit()
                                case _:
                                    user_answer = input(
                                        "Please Answer with Y or N: [y/n] "
                                    )
    except getopt.error as err:
        # Output Error, and Return with an Error Code
        print(str(err))
        print("please use sensei --help or sensei -h")
    except ValueError as ve:
        # ValueError
        print("invalid value, please enter int number -", str(ve))
        print("please use sensei --help or sensei -h")
