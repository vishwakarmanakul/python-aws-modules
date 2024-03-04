class person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f'Employee name is {self.name} and occupation is {self.occupation}')

a= person('nakul','python developer')
a.info()
