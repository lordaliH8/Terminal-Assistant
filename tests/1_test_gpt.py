from shellsensei.llm import GPT


model = GPT(model="gpt-3.5-turbo")
prompt = "Who are you?"

print(
    model.query(
        user_prompt=prompt,
    )
)
