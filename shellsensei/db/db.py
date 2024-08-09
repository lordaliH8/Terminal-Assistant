# Imports
import sqlite3
from shellsensei.db import utils
import os


# Init DataBase
def init(folder: str):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # GPT Table
    utils.create_gpt_table(cursor)
    # Prompt Table
    utils.create_prompt_table(cursor)
    # CMD Table
    utils.create_cmd_table(cursor)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Reset DataBase - Clean All Rows from All Tables
def reset(folder: str):
    clean_gpt_table(folder)
    clean_cmd_table(folder)
    clean_prompt_table(folder)


# Import GPT API Key
def import_gpt_api_key(folder: str, api_key):
    # Cost
    cost = "Felan Hichi"
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Insert into GPT Table
    utils.insert_into_gpt_table(cursor, api_key, cost)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Show CMD Table with Limit
def show_cmd_table(folder: str, limit):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Select * from CMD Table with Limit
    rows = utils.select_from_cmd_table(cursor, limit)
    print(rows)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Show Prompt Table with Limit
def show_prompt_table(folder: str, limit):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Select * from Prompt Table with Limit
    rows = utils.select_from_prompt_table(cursor, limit)
    print(rows)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Delete All Rows from GPT Table
def clean_gpt_table(folder: str):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Delete * from GPT Table
    utils.delete_from_gpt_table(cursor)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Delete All Rows from CMD Table
def clean_cmd_table(folder: str):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Delete * from CMD Table
    utils.delete_from_cmd_table(cursor)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Delete All Rows from Prompt Table
def clean_prompt_table(folder: str):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Delete * from Prompt Table
    utils.delete_from_prompt_table(cursor)

    # Commit and Close Connection
    connection.commit()
    connection.close()


# Check if API Key in GPT Table Exists
def check_if_api_key_exists(folder: str):
    # Create Connection
    connection = sqlite3.connect(database=os.path.join(folder, "shellsensei_db.db"))
    # Cursor
    cursor = connection.cursor()

    # Select GPT API Key from GPT Table
    row = utils.select_from_gpt_table(cursor)

    # Commit and Close Connection
    connection.commit()
    connection.close()

    if row is not None:
        return True
    else:
        return False
