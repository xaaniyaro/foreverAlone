class tnames:
    def __init__(self):
        self.counter = 0
        self.name = "t"
    
    def next(self):
        self.counter += 1
        return self.name + str(self.counter)
    
    def reset(self):
        self.counter = 0