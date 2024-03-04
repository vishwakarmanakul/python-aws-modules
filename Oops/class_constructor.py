class Company:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split('-')[0], string.split('-')[1])

string='nakul-12000'
a=Company.fromStr(string)
print(a.name)
print(a.salary)