# Imports
import getopt
import sys
from shellsensei.db import db
from shellsensei.cli.services import config


# Insert Handler
def insert_handler(currentArgs, values):
    if len(values) != 0:
        raise getopt.error("too many arguments")
    else:
        api_key = currentArgs
        check = db.check_if_api_key_exists(folder=config.get_location())
        if check:
            user_answer = input(
                "API Key Exists - Want to Replace this API Key with the Old One? [y/n] "
            )
            while True:
                match user_answer:
                    case "y" | "Y":
                        db.clean_gpt_table(folder=config.get_location())
                        db.import_gpt_api_key(
                            folder=config.get_location(), api_key=api_key
                        )
                        break
                    case "n" | "N":
                        sys.exit()
                    case _:
                        user_answer = input("Please Answer with Y or N: [y/n] ")
        else:
            db.import_gpt_api_key(folder=config.get_location(), api_key=api_key)
