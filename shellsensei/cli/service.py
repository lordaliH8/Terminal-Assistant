# Imports
import argparse

# Global Variables
app_name = "shellsensei"
app_version = "0.1"


# Show Help
def show_help():
    description = f"{app_name} - AI Terminal Assistant"
    usage = "sensei <OPTIONS> [ARGS] [NUMS][TABLES]"

    # Initialize Parser
    parser = argparse.ArgumentParser(
        prog=app_name, description=description, usage=usage
    )

    # Add Arguments
    parser.add_argument(
        "-v", "--version", action="help", help="Print version info and exit"
    )
    parser.add_argument(
        "-m",
        "--msg <Message>",
        action="help",
        help="Getting the Message to do the Desired Task",
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
        help="Delete All Rows from <cmd/prompt> Table",
    )
    parser.add_argument(
        "--config reset",
        action="help",
        help="Reset All Data",
    )
    parser.add_argument(
        "--import <API_KEY>",
        action="help",
        help="Import your GPT API Key",
    )
    parser.add_argument(
        "--show <TABLE> [NUM]",
        action="help",
        help="Show Last [NUM] Command from <cmd/prompt> Table",
    )
    parser.add_argument(
        "--remove",
        action="help",
        help="Remove GPT API Key",
    )

    # Print Help
    parser.print_help()


# Show Version
def show_version():
    print(f"{app_name} version {app_version}")


# Show DataBase and Config File Location
def show_location():
    print("~/.local/share/shellsensei/")


def output(msg):
    print(msg)
