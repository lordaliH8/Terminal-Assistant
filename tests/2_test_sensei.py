from src.sensei import Sensei


sensei = Sensei(sensei_id="test")
print(sensei.created_at)

print(sensei.ask(query="Shutdown all my docker containers which their name starts with M"))
