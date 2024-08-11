import os
import datetime
from shellsensei.db import (
    get_session,
    write_gpt,
    write_command,
    write_prompt,
    read_gpt,
    read_command,
    read_prompt,
    clear_table,
)


def get_location():
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".shellsensei")
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return config_dir


db_location = get_location()
print(f"DB is at {db_location}")

# Create/connect
get_session(db_url=db_location)


clear_table(table_name="gpt", db_url=db_location)

# Add data to tables
write_gpt("api_key_113", 0.02, db_location)
write_prompt("Hello", "Hi there!", datetime.datetime.now(), db_location)
write_command("greet", "Hello!", datetime.datetime.now(), db_location)


# read data from tables
print("Prompt table:")
prompts = read_prompt(db_location)
print(prompts[0])

print("Command table:")
commands = read_command(db_location)
print(commands[0])

print("GPT table:")
gpt_user = read_gpt(api_key="api_key_113", db_url=db_location)
print(gpt_user)


# Clear the tables
for table in ("gpt", "command", "prompt"):
    clear_table(table, db_location)
