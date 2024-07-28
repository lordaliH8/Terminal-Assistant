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


# Create History Table
def create_history_table(cursor):
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS history (
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
