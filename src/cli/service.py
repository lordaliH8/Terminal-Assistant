# Imports
import argparse

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
        "--config <API-KEY>",
        action="help",
        help="Override a GPT API Key Value",
    )

    # Print Help
    parser.print_help()


def show_version():
    print(f"{app_name} version {app_version}")


def output(msg):
    print(msg)
