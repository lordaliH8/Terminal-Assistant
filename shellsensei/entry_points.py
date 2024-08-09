# Imports
import getopt
import sys


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
                    from shellsensei.cli.services.help import help
                    help.show_help(argsList)

                # Version Handler
                case "-v" | "--version":
                    from shellsensei.cli.services.version import version
                    version.show_version(argsList)

                # Prompt Handler
                case "-m" :
                    from shellsensei.cli.services.prompt import prompt
                    prompt.prompt_handler(currentArgs, values)

                # Config Handler
                case "--config":
                    from shellsensei.cli.services.config import config
                    config.config_handler(argsList, currentArgs, values)

                # Insert Handler
                case "--insert":
                    from shellsensei.cli.services.insert import insert
                    insert.insert_handler(currentArgs, values)

                # Show Handler
                case "--show":
                    from shellsensei.cli.services.show import show
                    show.show_handler(currentArgs, values)

                # Remove Handler
                case "--remove":
                    from shellsensei.cli.services.remove import remove
                    remove.remove_handler(argsList)
    except getopt.error as err:
        # Output Error, and Return with an Error Code
        print(str(err))
        print("please use sensei --help or sensei -h")
    except ValueError as ve:
        # ValueError
        print("invalid value, please enter int number -", str(ve))
        print("please use sensei --help or sensei -h")
