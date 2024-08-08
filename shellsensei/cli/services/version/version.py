# Imports
import getopt

# Global Variables
app_name = "shellsensei"
app_version = "0.1"


# Show Version
def show_version(argsList):
    if len(argsList) != 1:
        raise getopt.error("too many arguments")
    else:
        print(f"{app_name} version {app_version}")
