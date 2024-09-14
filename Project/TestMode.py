# Correct usage of the Prompt class
from Model.prompter import Prompt

pr = Prompt()

response = pr.prompt("What is your name?", 1)

print(response)
