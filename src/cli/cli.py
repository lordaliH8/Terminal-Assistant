# Imports
import getopt
import sys
import src.cli.service

# Arguments - Remove 1st Argument from the List
argsList = sys.argv[1:]

# Short Options
shortopts = "hvm:"

# Long Options
longopts = ["help", "version", "msg=", "config=", "import="]

try:
    # Parsing Argument(s)
    opts, args = getopt.getopt(argsList, shortopts, longopts)

    # Checking Each Arguments
    for currentOpts, currentArgs in opts:

        # Help Handler
        if currentOpts in ("-h", "--help"):
            src.cli.service.show_help()

        # Version Handler
        if currentOpts in ("-v", "--version"):
            src.cli.service.show_version()

        # Message Handler
        if currentOpts in ("-m", "--msg"):
            msg = currentArgs
            src.cli.service.output(msg)

        # Config Handler
        if currentOpts in ("--config"):
            if currentArgs == "init":
                src.cli.service.init_db()

        # Import Handler
        if currentOpts in ("--import"):
            api_key = currentArgs
            src.cli.service.import_gpt_api_key(api_key)

except getopt.error as err:
    # Output Error, and Return with an Error Code
    print(str(err))
    print("please use sensei --help or sensei -h")
