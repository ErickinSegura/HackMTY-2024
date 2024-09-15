# Correct usage of the Prompt class
from Model.prompter import Prompt

pr = Prompt()

prom = "El producto llegó en perfectas condiciones y mucho antes de lo esperado. La calidad de los materiales es muy buena, aunque el precio es un poco alto para lo que ofrece."

response = pr.prompt(prom, 2)

list = eval(response)

print(list[0][0])
