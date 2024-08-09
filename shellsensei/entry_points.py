# Imports
import getopt
import sys
from shellsensei.cli.services import prompt, version, show, insert, help, remove, config


# Main Function
def main() -> None:
    # Arguments - Remove 1st Argument from the List
    argsList = sys.argv[1:]

    # Short Options
    shortopts = "hvm:"

    # Long Options
    longopts = ["help", "version", "config=", "insert=", "show=", "remove"]

    try:
        # Parsing Argument(s)
        opts, values = getopt.getopt(argsList, shortopts, longopts)

        # Checking Each Arguments
        for currentOpts, currentArgs in opts:

            # Switch Case currentOpts Variable
            match currentOpts:

                # Help Handler
                case "-h" | "--help":
                    help.show_help(argsList)

                # Version Handler
                case "-v" | "--version":
                    version.show_version(argsList)

                # Prompt Handler
                case "-m":
                    prompt.prompt_handler(currentArgs, values)

                # Config Handler
                case "--config":
                    config.config_handler(argsList, currentArgs, values)

                # Insert Handler
                case "--insert":
                    insert.insert_handler(currentArgs, values)

                # Show Handler
                case "--show":
                    show.show_handler(currentArgs, values)

                # Remove Handler
                case "--remove":
                    remove.remove_handler(argsList)

    except getopt.error as err:
        # Output Error, and Return with an Error Code
        print(str(err))
        print("please use sensei --help or sensei -h")
    except ValueError as ve:
        # ValueError
        print("invalid value, please enter int number -", str(ve))
        print("please use sensei --help or sensei -h")
