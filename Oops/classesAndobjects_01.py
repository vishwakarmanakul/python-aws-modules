class person:
    name='nakul'
    designation='python developer'
    networth=10
    def info(self):
        print(f'employee name is {self.name} and desination is {self.designation}')
a=person()
b=person()
b.name='sunil'
b.designation='accountant'
a.info()
b.info()