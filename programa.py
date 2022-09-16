
import random

class Cuestionador:

    def __init__(self):

        self.questions=[
            "¿Qué es el ALMICANTARAT?"
            "¿Dónde se encuentra el Zenit?"
            "¿Cuántos órdenes exsisten en la taxonamia de sueles?"
        ]

        self.answers=[
            "Circulo imaginario en esfera celeste"
            "90 grados respecto al horizonte"
            12
        ]

def jugar(self):
    #generar un número aleatorio entre 0 y n-1 siendo n el
    # tamaño de la lista de pregunta
    n=len(self.questionns)
    number= random.randint(0, n-1)
    print(self.questions[number])

    #solicitar la respuesta al usuario
    respuesta=imput("¿Cuál es tu respuesta?")

    #verificar si la respuesta es correcta

    if respuesta== self.answers[number]:
        print("Eres genial!!")
    else:
        print("Deje de pensar que sus papás lo van a mantener toda la vida") 

