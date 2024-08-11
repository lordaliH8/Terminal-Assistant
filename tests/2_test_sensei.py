from shellsensei.sensei import Sensei


sensei = Sensei(sensei_id="test")
print(sensei.created_at)

print(
    sensei.ask(query="Shutdown all my docker containers which their name starts with M")
)

print("-" * 60)

print(sensei.ask(query="Pull the docker image for my house price prediction project"))

print("-" * 60)

print(sensei.ask(query="Pull the docker image"))
