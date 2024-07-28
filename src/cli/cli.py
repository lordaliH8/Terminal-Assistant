# Imports
import getopt
import sys
import src.cli.service

# Arguments - Remove 1st Argument from the List
argsList = sys.argv[1:]

# Short Options
shortopts = "hvm:"

# Long Options
longopts = ["help", "version", "msg=", "config="]

try:
    # Parsing Argument(s)
    args, values = getopt.getopt(argsList, shortopts, longopts)

    # Checking Each Arguments
    for currentArgs, currentValue in args:

        # Help Handler
        if currentArgs in ("-h", "--help"):
            src.cli.service.show_help()

        # Version Handler
        if currentArgs in ("-v", "--version"):
            src.cli.service.show_version()

        # Message Handler
        if currentArgs in ("-m", "--msg"):
            msg = currentValue
            src.cli.service.output(msg)

        # Config Handler
        if currentArgs in ("--config"):
            if currentValue == "init":
                src.cli.service.init_db()

except getopt.error as err:
    # Output Error, and Return with an Error Code
    print(str(err))
    print("please use sensei --help or sensei -h")
