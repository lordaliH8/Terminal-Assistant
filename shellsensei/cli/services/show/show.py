# Imports
import getopt
from shellsensei.db import db
from shellsensei.cli.services import config


# Show Handler
def show_handler(currentArgs, values):
    # Switch Case on currentArgs Variable
    match currentArgs:
        # CMD
        case "cmd" if len(values) == 0:
            limit = 1
            db.show_cmd_table(folder=config.get_location(), limit=limit)
        case "cmd" if len(values) == 1:
            limit = int(values[0])
            db.show_cmd_table(folder=config.get_location(), limit=limit)
        # Prompt
        case "prompt" if len(values) == 0:
            limit = 1
            db.show_prompt_table(folder=config.get_location(), limit=limit)
        case "prompt" if len(values) == 1:
            limit = int(values[0])
            db.show_prompt_table(folder=config.get_location(), limit=limit)
    # Error Handling for "Too Many Arguments"
    if len(values) > 1:
        raise getopt.error("too many arguments")
    # Error Handling for "Wrong Arguments"
    elif currentArgs not in ("cmd", "prompt"):
        raise getopt.error("wrong argument")
