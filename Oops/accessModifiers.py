"""
Private : Private access modifiers are those variables or methods which could be
access only within the class, could not access outside of class but can be accessed
indirectly (obj._Employee__name)
"""
class Employee():
    def __init__(self):
        self.__name='nakul'
obj=Employee()
print(obj._Employee__name)


