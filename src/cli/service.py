# Imports
import argparse
import src.db.db

# Global Variables
app_name = "shellsensei"
app_version = "0.1"


# Show Help
def show_help():
    description = f"{app_name} - AI Terminal Assistant"
    usage = "sensei <OPTIONS> [ARGS]"

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
        "--import <API_KEY>",
        action="help",
        help="Import your GPT API Key",
    )

    # Print Help
    parser.print_help()


# Show Version
def show_version():
    print(f"{app_name} version {app_version}")


# Initialize DataBase
def init_db():
    src.db.db.init()


# Import GPT API Key
def import_gpt_api_key(api_key):
    src.db.db.import_gpt_api_key(api_key)


def output(msg):
    print(msg)
