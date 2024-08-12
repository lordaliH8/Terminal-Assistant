# Imports
import argparse
import getopt


# Global Variables
app_name = "shellsensei"
app_version = "0.1"


# Show Help
def show_help(argsList):
    if len(argsList) != 1:
        raise getopt.error("too many arguments")
    else:
        description = f"{app_name} - AI Terminal Assistant"
        usage = (
            "sensei <OPTIONS> [ARGS] [NUMS]\n"
            + " " * 7
            + "sensei <OPTIONS> [ARGS] [TABLES]"
        )

        # Initialize Parser
        parser = argparse.ArgumentParser(
            prog=app_name, description=description, usage=usage
        )

        # Help Handler
        help_handler(parser)
        # Print Help
        parser.print_help()


# Help Handler
def help_handler(parser):
    # Add Arguments
    parser.add_argument(
        "-v", "--version", action="help", help="Print version info and exit"
    )
    parser.add_argument(
        "-m <PROMPT>",
        action="help",
        help="Getting the Prompt Message to do the Desired Task",
    )
    parser.add_argument(
        "--config init",
        action="help",
        help="Init DataBase and Config File",
    )
    parser.add_argument(
        "--config location",
        action="help",
        help="Show DataBase and Config File Location",
    )
    parser.add_argument(
        "--config rm <TABLE>",
        action="help",
        help="Delete All Rows from <commands/prompts> Table",
    )
    parser.add_argument(
        "--config reset",
        action="help",
        help="Reset All Data",
    )
    parser.add_argument(
        "--insert <API_KEY>",
        action="help",
        help="Insert your GPT API Key",
    )
    parser.add_argument(
        "--show <TABLE> [NUM]",
        action="help",
        help="Show Last [NUM] Command from <commands/prompts> Table",
    )
    parser.add_argument(
        "--remove",
        action="help",
        help="Remove GPT API Key",
    )
