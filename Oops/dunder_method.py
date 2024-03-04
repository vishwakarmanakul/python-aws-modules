class Employee:
    def __init__(self):
        self.str_='nakul'

    def __len__(self):
        c = 0
        for i in self.str_:
            c += 1
        return c

    def __add__(self, a,b):
        return a+b
e=Employee()
