# Imports
import sqlite3
import src.db.utils


# Init DataBase
def init():
    # Create Connection
    connection = sqlite3.connect(database="shellsensei_db.db")
    # Cursor
    cursor = connection.cursor()

    # GPT Table
    src.db.utils.create_gpt_table(cursor)
    # Prompt Table
    src.db.utils.create_prompt_table(cursor)
    # History Table
    src.db.utils.create_history_table(cursor)

    # Commit and Close Connection
    connection.commit()
    connection.close()
