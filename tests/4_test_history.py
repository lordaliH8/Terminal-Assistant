from shellsensei.sensei import Sensei

sensei = Sensei(sensei_id="test")
print(sensei.created_at)

sensei.task = "delete container"
sensei.scenario =sensei.generate_chat_scenario(sensei.question_history,sensei.command_history)

response = sensei.ask()

res =("""Command 'docker' not found, but can be installed with:
sudo snap install docker         # version 24.0.5, or
sudo apt  install docker.io      # version 24.0.5-0ubuntu1
sudo apt  install podman-docker  # version 4.9.3+ds1-1ubuntu0.1
See 'snap info docker' for additional versions.
""")

if response.get("command"):
    sensei.generate_history(response.get("command") , res, type="command")
if response.get("question"):
    sensei.generate_history(response.get("question") , res, type="question")

sensei.scenario = sensei.generate_chat_scenario(sensei.command_history,sensei.question_history)

response =sensei.ask()

print(response)


