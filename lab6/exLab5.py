
import math 

#ex1
class Shape:
    def areea(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,raza):
        self.raza=raza

    def areea(self):
        return self.raza**2 *math.pi
    
    def perimeter(self):
        return self.raza*2*math.pi
    
class Rectangle(Shape):
    def __init__(self,latime,lungime):
        self.lungime=lungime
        self.latime=latime
    
    def areea(self):
        return self.lungime*self.latime
    
    def perimeter(self):
        return 2*self.latime+2*self.lungime
    
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def areea(self):
        p=(self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
    
    def perimeter(self):
        return self.a+self.b+self.c
    
c=Circle(6)
#print(c.areea(),c.perimeter())

r=Rectangle(6,5)
#print(r.areea(),r.perimeter())

t=Triangle(5,6,7)
#print(t.areea(),t.perimeter())

#ex2
class Account:
    def __init__(self,idCont,balanta=0):
        self.idCont=idCont
        self.balanta=balanta

    def deposit(self,valoare):
        self.balanta+=valoare
        print(self.balanta)

    def withdrawal(self,valoare):
        if valoare<self.balanta and valoare>0:
            self.balanta-=valoare
            print(self.balanta)

    def interest(self):
        pass

class SavingAccount(Account):
    def __init__(self, idCont, balanta=0,rata=0.05):
        super().__init__(idCont, balanta)
        self.rata=rata
    
    def interest(self):
        valTot=self.rata *self.balanta+self.balanta
        self.valTot=valTot
        print("aveti o valoare tot de platit de:",self.valTot)

class CheckingAccount(Account):
    def __init__(self, idCont, balanta=0,limita=200):
        super().__init__(idCont, balanta)
        self.limita=limita

    def withdrawal(self, valoare):
        if valoare<self.limita:
            super().withdrawal(valoare)

savings_account = SavingAccount(1, 1000, 0.03)
#savings_account.deposit(500)
#savings_account.interest()
#savings_account.withdrawal(200)

checking_account = CheckingAccount(2, 500, 200)
#checking_account.deposit(300)
#checking_account.withdrawal(700)

#ex3
class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def mileage(self):
        pass

    def towing_capacity(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def mileage(self):
        return (2023-self.year)*10000
    
    def towing_capacity(self):
        return 750
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def mileage(self):
        return (2023-self.year)*5000
    
    def towing_capacity(self):
        return 0
    
class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def mileage(self):
        return (2023-self.year)*20000
    
    def towing_capacity(self):
        return 2000

car = Car("Toyota", "1", 2022)
motorcycle = Motorcycle("Harley-Davidson", "2", 2021)
truck = Truck("Renault", "3", 2023)

#print(car.mileage(),car.towing_capacity())
#print(motorcycle.mileage(),motorcycle.towing_capacity())
#print(truck.mileage(),truck.towing_capacity())

#ex4
class Employee:
    def __init__(self,nume):
        self.nume=nume
        self.salariu=0

    def rol(self):
        pass

class Manager(Employee):
    def __init__(self,nume):
        super().__init__(nume)
        self.salariu=5000

    def rol(self):
        return "Manager"
    
class Engineer(Employee):
    def __init__(self,nume):
        super().__init__(nume)
        self.salariu=6000

    def rol(self):
        return "Engineer"
    
class Salesperson(Employee):
    def __init__(self,nume):
        super().__init__(nume)
        self.salariu=4000

    def rol(self):
        return "Salesperson"
    
manager=Manager("Andrei")
engineer=Engineer("Ion")
salesperson=Salesperson("Andreea")

#print(manager.salariu,manager.rol())
#print(engineer.salariu,engineer.rol())
#print(salesperson.salariu,salesperson.rol())

#ex5
class Animal:
    def __init__(self,name):
        self.name=name
    
    def getClass(self):
        pass

class Mammal(Animal):
    def __init__(self, name,legs):
        super().__init__(name)
        self.legs=legs

    def getClass(self):
        return "Mammal"
    
class Bird(Animal):
    def __init__(self, name,nocturn):
        super().__init__(name)
        self.nocturn=nocturn
    
    def getClass(self):
        return "Bird"
    
class Fish(Animal):
    def __init__(self, name,pradator):
        super().__init__(name)
        self.pradator=pradator

    def getClass(self):
        return "Fish"
    
m=Mammal("Cangur",2)
b=Bird("Privighetoare",False)
f=Fish("Somon",False)

#print(m.getClass(),m.name,m.legs)
#print(b.getClass(),b.name,b.nocturn)
#print(f.getClass(),f.name,f.pradator)

#ex6:

class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."

    def display_info(self):
        status = "checked out" if self.checked_out else "available"
        return f"{self.title} by {self.author} (ID: {self.item_id}) - Status: {status}"


class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def display_info(self):
        return f"{super().display_info()} - {self.num_pages} pages"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.duration = duration

    def display_info(self):
        return f"{super().display_info()} - Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, item_id):
        super().__init__(title, "", item_id) 

    def display_info(self):
        return f"{super().display_info()}"


book = Book("Book1", "Matei", "B1", 224)
dvd = DVD("DVD1", "Andrei", "D1", 148)
magazine = Magazine("Magazine1" , "M1")

print(book.display_info())
print(book.check_out())
print(book.return_item())

print(dvd.display_info())
print(dvd.check_out())

print(magazine.display_info())

