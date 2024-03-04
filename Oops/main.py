class Object:
    def __init__(self,name,age):
        self.name= name
        self.age= age
        self.address='indore'
obj= Object('nakul',25)
print(obj.__dict__)

