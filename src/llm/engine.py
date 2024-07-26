import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from src.db.localDB import db
class engine(db):
    def __init__(self,username,password,apiKey):
        self.name = username
        self.password = password
        os.environ["OPENAI_API_KEY"] = apiKey
        database = db(username, password, apiKey)
        if not database.login_user():
            database.register_user()
        key = database.getUserKey()
        self.openai_api_key = key
        self.model = ChatOpenAI(model="gpt-4")
        self.parser = StrOutputParser()
    def run(self,command):
        json_template = {
            "command1",
            "command2",
            "etc"
        }
        command_prompt = (
            "Consider this command: {command}. "
            "Return instructions for executing this command in a JSON format. "
            "Ensure all instructions are runnable on a Linux machine. "
            "ensure that the output will be json dictionary with only commands in a row "
        )
        instruction = ChatPromptTemplate.from_messages(
            [("system", command_prompt), ("user", "{command}")]
        )
        instruction_chain = instruction | self.model |self.parser
        result = instruction_chain.invoke({"command",command})
        return result

    def pipeline(self,command):
        return self.run(command)


if __name__ == '__main__':
    engine = engine("ali","lordali","sk-None-gJTEr0Oa0ePvh8YUIdnKT3BlbkFJ3vasNiBN9TjgbTZ6wn7Y")
    op = engine.pipeline("install mini conda")
    print(op)
