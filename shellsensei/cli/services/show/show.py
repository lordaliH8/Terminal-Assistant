# Imports
import getopt
from shellsensei.db import db
from shellsensei.cli.services import config


# Show Handler
def show_handler(currentArgs, values):
    # Switch Case on currentArgs Variable
    match currentArgs:
        # Command
        case "command" if len(values) == 0:
            command = db.read_command(db_url=config.get_location())
            print(command)
        case "command" if len(values) == 1:
            limit = int(values[0])
            commands = db.read_command(db_url=config.get_location(), k=limit)
            print(commands)
        # Prompt
        case "prompt" if len(values) == 0:
            prompt = db.read_prompt(db_url=config.get_location())
            print(prompt)
        case "prompt" if len(values) == 1:
            limit = int(values[0])
            prompts = db.read_prompt(db_url=config.get_location(), k=limit)
            print(prompts)
    # Error Handling for "Too Many Arguments"
    if len(values) > 1:
        raise getopt.error("too many arguments")
    # Error Handling for "Wrong Arguments"
    elif currentArgs not in ("command", "prompt"):
        raise getopt.error("wrong argument")
