# Imports
import getopt
from shellsensei.db import db


# Show Handler
def show_handler(currentArgs, values):
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
