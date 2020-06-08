#Clase para implementar todas las operaciones basicas de una pila

class Stack:
    def __init__(self):
        self.items = []
        self.debug = True

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)