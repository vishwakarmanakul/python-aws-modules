class Employee:
    emp_pf_account= 0

    def __init__(self,numbers):
        self.numbers=numbers

    def show(self):
        print(f'comapany strenght is {self.emp_pf_account}')

    @classmethod
    def changeCompany(cls, new_account):
        cls.emp_pf_account+= new_account

account_objects=[]
n=10
while n:
    id=input('Enter id:')
    emp= Employee(id)
    account_objects.append(emp)
    Employee.changeCompany(1)
    if len(account_objects)>=4:
        emp.show()
    n-=1