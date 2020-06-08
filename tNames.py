#Clase para generar nombres para ocupar espacios de valores temporales, se genera uno diferente
# cada que se utiliza el metodo next(), tambien incorpora una funcion para empezar desde 0
# ya que la utilidad de esta clase recaer en que pueda ser reutilizable

class tnames:
    def __init__(self):
        self.counter = 0
        self.name = "t"
    
    def next(self):
        self.counter += 1
        return self.name + str(self.counter)
    
    def reset(self):
        self.counter = 0