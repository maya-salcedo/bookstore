#class - blueprint

class Account:

    def __init__(self, filepath): # init are constructor; special method
        self.filepath=filepath      # Example of instance variable; it is inside the method
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

    #Subclass, so there is no need to copy and paste the functions in class Account(base class) and make another class
    #Inheritance
class Checking(Account):
    """This class generates checking account object""" #example of doc string
    type = "checking"   #Example of Class variable, declared outside of method, shared by all instances in class
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee
tina_checking = Checking("tina.txt", 1) #example of object instance; instantiation of class
tina_checking.transfer(30)
tina_checking.commit() # .commit is an example of attributes
print(tina_checking.balance)
print(tina_checking.type)

chris_checking = Checking("chris.txt", 1) #example of object instance
chris_checking.transfer(60)
chris_checking.commit()
print(chris_checking.balance)
print(chris_checking.type)
print(chris_checking.__doc__)