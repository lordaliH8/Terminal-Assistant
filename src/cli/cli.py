# Imports
import getopt
import sys
import src.cli.service
import src.db.db

# Arguments - Remove 1st Argument from the List
argsList = sys.argv[1:]

# Short Options
shortopts = "hvm:"

# Long Options
longopts = ["help", "version", "msg=", "config=", "import=", "show="]

try:
    # Parsing Argument(s)
    opts, values = getopt.getopt(argsList, shortopts, longopts)

    # Checking Each Arguments
    for currentOpts, currentArgs in opts:

        # Switch Case currentOpts Variable
        match currentOpts:

            # Help Handler
            case "-h" | "--help":
                if len(argsList) != 1:
                    raise getopt.error("too many arguments")
                else:
                    src.cli.service.show_help()

            # Version Handler
            case "-v" | "--version":
                if len(argsList) != 1:
                    raise getopt.error("too many arguments")
                else:
                    src.cli.service.show_version()

            # Message Handler
            case "-m" | "--msg":
                msg = currentArgs
                src.cli.service.output(msg)

            # Config Handler
            case "--config":
                # Switch Case on currentArgs Variable
                match currentArgs:
                    case "init":
                        if len(argsList) != 2:
                            raise getopt.error("too many arguments")
                        else:
                            src.db.db.init()
                    case "location":
                        if len(argsList) != 2:
                            raise getopt.error("too many arguments")
                        else:
                            src.cli.service.show_location()
                    case "rm" if values[0] == "cmd" and len(values) == 1:
                        src.db.db.clean_cmd_table()
                    case "rm" if values[0] == "prompt" and len(values) == 1:
                        print("dadas")
                        src.db.db.clean_prompt_table()
                    case "reset":
                        if len(argsList) != 2:
                            raise getopt.error("too many arguments")
                        src.db.db.reset()
                # Error Handling for "Too Many Arguments"
                if len(values) > 1:
                    raise getopt.error("too many arguments")
                # Error Handling for "Wrong Arguments"
                elif currentArgs not in ("init", "location", "rm", "reset"):
                    raise getopt.error("wrong argument")

            # Import Handler
            case "--import":
                if len(values) != 0:
                    raise getopt.error("too many arguments")
                else:
                    api_key = currentArgs
                    src.db.db.import_gpt_api_key(api_key)

            # Show Handler
            case "--show":
                # Switch Case on currentArgs Variable
                match currentArgs:
                    # CMD
                    case "cmd" if len(values) == 0:
                        limit = 1
                        src.db.db.show_cmd_table(limit)
                    case "cmd" if len(values) == 1:
                        limit = int(values[0])
                        src.db.db.show_cmd_table(limit)
                    # Prompt
                    case "prompt" if len(values) == 0:
                        limit = 1
                        src.db.db.show_prompt_table(limit)
                    case "prompt" if len(values) == 1:
                        limit = int(values[0])
                        src.db.db.show_prompt_table(limit)
                # Error Handling for "Too Many Arguments"
                if len(values) > 1:
                    raise getopt.error("too many arguments")
                # Error Handling for "Wrong Arguments"
                elif currentArgs not in ("cmd", "prompt"):
                    raise getopt.error("wrong argument")
except getopt.error as err:
    # Output Error, and Return with an Error Code
    print(str(err))
    print("please use sensei --help or sensei -h")
except ValueError as ve:
    # ValueError
    print("invalid value, please enter int number -", str(ve))
    print("please use sensei --help or sensei -h")
