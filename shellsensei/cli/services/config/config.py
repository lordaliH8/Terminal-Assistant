# Imports
import getopt
from shellsensei.db import db
import os


# Show DataBase and Config File Location
def get_location():
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".shellsensei")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return config_dir


# Config Handler
def config_handler(argsList, currentArgs, values):
    # Switch Case on currentArgs Variable
    match currentArgs:
        case "init":
            if len(argsList) != 2:
                raise getopt.error("too many arguments")
            else:
                db.get_session(db_url=get_location())
        case "location":
            if len(argsList) != 2:
                raise getopt.error("too many arguments")
            else:
                print(get_location())
        case "rm" if len(values) == 1:
            db.clear_table(table_name=values[0], db_url=get_location())
            print(f"{values[0]} cleared!")
        case "reset":
            if len(argsList) != 2:
                raise getopt.error("too many arguments")
            db.reset(db_url=get_location())

    # Error Handling for "Too Many Arguments"
    if len(values) > 1:
        raise getopt.error("too many arguments")
    # Error Handling for "Wrong Arguments"
    elif currentArgs not in ("init", "location", "rm", "reset"):
        raise getopt.error("wrong argument")
