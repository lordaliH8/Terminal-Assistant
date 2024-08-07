from shellsensei.sensei import Sensei

sensei = Sensei(sensei_id="test")
print(sensei.created_at)

task = "install docker"
response = sensei.ask(task)
res =("command response")
if response.get("command"):
    sensei.generate_history(response.get("command") , res, type="command")

print("model response is : " , response)
print("command history content : " , sensei.command_history)

print("%" * 50)

task = "delete container"
response = sensei.ask(task)
res = "ubuntu:latest"
if response.get("question"):
    sensei.generate_history(response.get("question"), res, type="question")
print("model response is : " , response)
print("question history content : " , sensei.question_history)
