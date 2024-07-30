# Create GPT Table
def create_gpt_table(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS gpt (
                api_key TEXT PRIMARY KEY,
                cost TEXT NOT NULL
            )
        """
    )


# Create Prompt Table
def create_prompt_table(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS prompt (
                user_prompt TEXT PRIMARY KEY,
                gpt_prompt TEXT NOT NULL,
                date DATETIME NOT NULL
            )
        """
    )


# Create CMD Table
def create_cmd_table(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS cmd (
                command TEXT PRIMARY KEY,
                result TEXT NOT NULL,
                date DATETIME NOT NULL
            )
        """
    )


# Insert into GPT Table
def insert_into_gpt_table(cursor, api_key, cost):
    cursor.execute(
        f"""
        INSERT INTO gpt(api_key, cost) values('{api_key}', '{cost}')
        """
    )


# Select GPT API Key from GPT Table
def select_from_gpt_table(cursor):
    return cursor.execute(
        f"""
        SELECT api_key from gpt
        """
    ).fetchone()


# Select * from CMD Table with Limit
def select_from_cmd_table(cursor, limit):
    return cursor.execute(
        f"""
        SELECT command, result FROM cmd ORDER BY date DESC LIMIT {limit}
        """
    ).fetchall()


# Select * from Prompt Table with Limit
def select_from_prompt_table(cursor, limit):
    return cursor.execute(
        f"""
        SELECT user_prompt, gpt_prompt FROM prompt ORDER BY date DESC LIMIT {limit}
        """
    ).fetchall()


# Delete All Rows from GPT Table
def delete_from_gpt_table(cursor):
    cursor.execute(
        f"""
        DELETE FROM gpt
        """
    )


# Delete All Rows from Prompt Table
def delete_from_prompt_table(cursor):
    cursor.execute(
        f"""
        DELETE FROM prompt
        """
    )


# Delete All Rows from CMD Table
def delete_from_cmd_table(cursor):
    cursor.execute(
        f"""
        DELETE FROM cmd
        """
    )
