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
        # Check if GPT Table is Empty or Not
        row = db.read_gpt(db_url=config.get_location())
        if row is not None:
            user_answer = input(
                "API Key Exists - Want to Replace this API Key with the Old One? [y/n] "
            )
            while True:
                match user_answer:
                    case "y" | "Y":
                        db.clear_table(table_name="gpt", db_url=config.get_location())
                        db.write_gpt(
                            api_key=api_key,
                            cost=4.44,
                            db_url=config.get_location(),
                        )
                        break
                    case "n" | "N":
                        sys.exit()
                    case _:
                        user_answer = input("Please Answer with Y or N: [y/n] ")
        else:
            db.write_gpt(api_key=api_key, cost=4.44, db_url=config.get_location())
