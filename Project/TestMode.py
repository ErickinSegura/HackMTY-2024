# Correct usage of the Prompt class
from Model.prompter import Prompt

pr = Prompt()

prom = """{
    "comentarios": [
        "El producto llegó roto y nadie me dio solución. Muy decepcionante.",
        "La calidad es pésima, se siente muy frágil y mal hecho.",
        "No funciona como se describe, no cumple con lo que promete.",
        "Lo peor que he comprado en mucho tiempo, no lo recomiendo.",
        "El material parece barato y se dañó al poco tiempo de uso.",
        "El servicio de atención al cliente fue terrible, no me resolvieron nada.",
        "No me gustó, esperaba algo mucho mejor por el precio.",
        "Excelente producto, justo lo que necesitaba. Muy satisfecho.",
        "Funciona perfectamente, es muy fácil de usar y de buena calidad.",
        "La calidad es bastante buena y llegó antes de lo esperado. Muy feliz con mi compra."
    ]
}

4
"""

response = pr.prompt(prom, 3)

print(response)
