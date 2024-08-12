import os
from sqlalchemy import create_engine, Column, String, Float, Date, desc, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class GPT(Base):
    __tablename__ = "gpt"
    api_key = Column(String, primary_key=True)
    cost = Column(Float)

    def __repr__(self):
        return f"GPT(api_key={self.api_key}, cost={self.cost})"


class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    input = Column(String)
    output = Column(String)
    date = Column(Date)

    def __repr__(self):
        return f"Prompt(id={self.id}, input={self.input}, output={self.output}, date={self.date})"


class Command(Base):
    __tablename__ = "commands"
    id = Column(Integer, primary_key=True, autoincrement=True)
    command = Column(String)
    output = Column(String)
    date = Column(Date)

    def __repr__(self):
        return f"Command(id={self.id}, command={self.command}, output={self.output}, date={self.date})"


def get_session(db_url: str):
    if not os.path.exists(db_url):
        os.makedirs(db_url)
    db_file_path = os.path.join(db_url, "shellsensei.sqlite")
    engine = create_engine(f"sqlite:///{db_file_path}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def write_gpt(api_key, cost, db_url: str):
    session = get_session(db_url)
    new_gpt = GPT(api_key=api_key, cost=cost)
    session.add(new_gpt)
    session.commit()
    session.close()


def read_gpt(api_key, db_url: str):
    session = get_session(db_url)
    gpt = session.query(GPT).filter_by(api_key=api_key).first()
    session.close()
    return gpt


def update_gpt(api_key, new_cost, db_url: str):
    session = get_session(db_url)
    gpt = session.query(GPT).filter_by(api_key=api_key).first()
    if gpt:
        gpt.cost = new_cost
        session.commit()
    session.close()


def write_prompt(input_text, output_text, date, db_url: str):
    session = get_session(db_url)
    new_prompt = Prompt(input=input_text, output=output_text, date=date)
    session.add(new_prompt)
    session.commit()
    session.close()


def read_prompt(db_url: str, k: int = 1):
    session = get_session(db_url)
    prompts = session.query(Prompt).order_by(desc(Prompt.date)).limit(k).all()
    session.close()
    return prompts


def write_command(command_text, output_text, date, db_url: str):
    session = get_session(db_url)
    new_command = Command(command=command_text, output=output_text, date=date)
    session.add(new_command)
    session.commit()
    session.close()


def read_command(db_url: str, k: int = 1):
    session = get_session(db_url)
    commands = session.query(Command).order_by(desc(Command.date)).limit(k).all()
    session.close()
    return commands


def clear_table(table_name, db_url: str):
    session = get_session(db_url)
    table_class = Base.metadata.tables.get(table_name)
    if table_class is not None:
        session.query(table_class).delete()
        session.commit()
    session.close()


def check_gpt(db_url: str):
    session = get_session(db_url)
    gpt = session.query(GPT).first()
    session.close()
    if gpt is not None:
        return True
    else:
        return False
