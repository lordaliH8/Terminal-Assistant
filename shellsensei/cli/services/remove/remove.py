# Imports
import getopt
import sys
from shellsensei.db import db
from shellsensei.cli.services import config


# Remove Handler
def remove_handler(argsList):
    if len(argsList) != 1:
        raise getopt.error("too many arguments")
    else:
        user_answer = input("Are you Sure you want to Delete your GPT API Key? [y/n] ")
        while True:
            match user_answer:
                case "y" | "Y":
                    db.clear_table(table_name="gpt", db_url=config.get_location())
                    break
                case "n" | "N":
                    sys.exit()
                case _:
                    user_answer = input("Please Answer with Y or N: [y/n] ")
