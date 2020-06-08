# Clase para contener todas las operaciones necesarias para llevar un registro 
# de cuadruplos. Se inicializa el atributo items con una lista vacia
# y el contador con un 0 desde el modulo Parser.py

class Quadruple:
    
    def __init__(self, items, contador):
        self.items = items
        self.contador = contador

    #Genera una lista de cuatro campos en el que posiciona cada atributo donde debe ser
    # incrementa el contador, evita mucha repeticion de codigo
    def generate(self, label, lOpd, rOpd, result):
        newQuad = [label, lOpd, rOpd, result]
        self.items.append(newQuad)
        self.contador += 1

    #Funcion que recibe el indice a cambiar y modifica el contenido de ese indice
    # por el valor del otro parametro
    def fill(self, index, content):
        if self.items[index][3] == None:
            self.items[index][3] = content
        else:
            print("Wrong quadruple")