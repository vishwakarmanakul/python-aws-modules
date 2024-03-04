"""
Super keyword in python used to refer to the parent class, It is especially useful when a class
inherits from multiple parent classes and you want to call a method from one of the parent classes.
"""

# class ParentClass:
#     def parent_method(self):
#         print('This is parent method1')
#
# class ChildClass(ParentClass):
#     def parent_method(self):
#         print('harry')
#         super().parent_method()
#
#     def child_method(self):
#         print('This is child method of parent class')
#         super().parent_method()
#
# a=ChildClass()
# a.child_method()
# a.parent_method()

class Employee:
    def __init__(self,name, id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name, id, lang):
        super().__init__(name,id)
        self.lang=lang
a=Programmer('nakul',101,'python')
print(a.name, a.id,a.lang)
b=Employee('vikas',102)
print(b.name, b.id)