# Imports
import getopt
from shellsensei.db import db


# Show DataBase and Config File Location
def show_location():
    print("~/.local/share/shellsensei/")


# Config Handler
def config_handler(argsList, currentArgs, values):
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
                show_location()
        case "rm" if values[0] == "cmd" and len(values) == 1:
            db.clean_cmd_table()
        case "rm" if values[0] == "prompt" and len(values) == 1:
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
