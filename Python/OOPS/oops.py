# define a class

class Person:
    pass

# call class
person1 = Person()
person2 = Person()

# both of them gives different memeory location because they are different objects in memory.
print(id(person1))
print(id(person2))

a = 3
print(type(a)) 
# reference to <class 'int'>  

print(type(person1)) # reference to <class '__main__.Person'>  (custom type)

class Phone:
    def __init__(self,name,mail,country,wifi_name,language):
        #logic,values that we want default to be set when object is created
        # name
        # mail
        # country
        # wifi_name
        # language
        # print(id(self)) # reference to the object created in memory
        self.name = name
        self.mail = mail
        self.country = country
        self.wifi_name = wifi_name
        self.language = language
        # print(language)
    def download_app_from_app_store(self,app_name):
        self.app_name = app_name # you can also set new attributes to the object using self. no need to define in __init__ method. but it is not a good practice to do so.
        print(f"Downloading {self.app_name} from app store for user {self.name}")

    def user_info(self):
        print(f"User Info: Name: {self.name}, Mail: {self.mail}, Country: {self.country}, Wifi Name: {self.wifi_name}, Language: {self.language}")

phone1 = Phone("iPhone 14","john@example.com","USA","HomeWiFi",["English", "Telugu"])


# class --> object --> calls __init_ method automatically when object is created.
# self id(self) and object reference is same, so we can use self to access the object attributes and methods.
phone1.download_app_from_app_store("Instagram")

phone1.user_info()

# function inside the class is called as method 
# variables inside the class are called attributes or instance variables.


# 4 pillars of OOPS

# inheritance, polymorphism, encapsulation, abstraction(optional)

# needed for like its standard, maintainability, scale.

#Inheritance
# inherit traits from parent class to child class. (reusability of code)
# use inheritance when we have a is-a relationship between classes. (Dog is an Animal, Cat is an Animal) (tightly coupled classes)
# use composition when we have a has-a relationship between classes. (Car has an Engine, Car has a Wheel) (loosely coupled classes)
class Dog:
    def __init__(self,name,age,legs):
        self.name = name
        self.age = age
        self.legs = legs

    def bark(self):
        print(f"{self.name} is barking")
    def how_many_legs(self):
        print(f"{self.name} has {self.legs} legs")

class Cat:
    def __init__(self,name,age,legs):
        self.name = name
        self.age = age
        self.legs = legs

    def meow(self):
        print(f"{self.name} is meowing")
    def how_many_legs(self):
        print(f"{self.name} has {self.legs} legs")

# same exact method present in both classes, but different implementation.

# solution

class Animal:
    def __init__(self,legs):
        self.legs = legs

    def how_many_legs(self):
        print(f"{self.name} has {self.legs} legs")
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def __init__(self,name,legs):
        self.name = name
        super().__init__(legs) # calling parent class constructor to set legs attribute
    def bark(self):
        print(f"{self.name} is barking")
class Cat(Animal):
    def __init__(self,name,legs):
        self.name = name
        super().__init__(legs) # calling parent class constructor to set legs attribute
    def meow(self):
        print(f"{self.name} is meowing")

dog1 = Dog("Tommy",4)
dog1.how_many_legs()


# multiple inheritance
# class can inherit from multiple classes. (diamond problem)
# class c inherits from class a and b, both a and b have same method name, which method will be called when we call c.method()?
class Engine:
    def start(self):
        print("Engine started")

class Electronics:
    def start(self):
        print("Electronics turned on")

class Tesla(Engine,Electronics):
    def start(self):
        # super().start() # calling parent class method
        # print("Tesla started")
        pass
smart_car = Tesla()
smart_car.start() # which start method will be called? (Engine or Electronics)  (it will call the method from the first parent class mentioned in the class definition, which is Engine in this case.)

print(Tesla.__mro__) # method resolution order, shows the order in which classes are searched for a method.
# (<class '__main__.Tesla'>, <class '__main__.Engine'>, <class '__main__.Electronics'>, <class 'object'>)

# multi level inheritance a -> b -> c
class A:
    def method_a(self):
        print("Method A from class A")

class B(A):
    def method_b(self):
        print("Method B from class B")

class C(B):
    def method_c(self):
        print("Method C from class C")

#hierarchical inheritance a -> b, a -> c
class A:
    def method_a(self):
        print("Method A from class A")

class B(A):
    def method_b(self):
        print("Method B from class B")

class C(A):
    def method_c(self):
        print("Method C from class C")




# Abstraction part-1
# hiding complexity 
# hide the implementation details and show only the functionality to the user. (user should not know how the functionality is implemented, but should know how to use it.)
# we can achieve abstraction using abstract classes and interfaces.


# Encapsulation
#java
#data hiding, restricting access to the internal state of an object and only allowing access through methods. (private variables and methods)
#python
# code readability, maintainability
# using encapsulation python only implements naming convention to achieve encapsulation, but it is not a strict enforcement. (we can still access private variables and methods using name mangling)

# self.name = public variable
# self._name = protected variable (should not be accessed outside the class, but can be accessed by subclasses)
# self.__name = private variable (should not be accessed outside the class, but can be
# accessed by subclasses using name mangling)
# class_object._ClassName__private_variable_name
# car1._Car__current_gps_coordinates



class Car:
    def __init__(self,brand):
        self.brand = brand #public variable
        self.ac_voltage = 12 #protected variable
        self.__current_gps_coordinates = (0,0) #private variable    

    def tell_brand(self):
        print(f"Car brand is {self.brand}")
    def run_ac(self):
        if self.check_ac():
            print(f"AC is running at {self.ac_voltage} volts")
    def check_ac(self):
        if self.ac_voltage > 12:
            return False
        else:
            return True
    def access_gps_coordinates(self,password):
        if password == "secret":
            print(f"Current GPS coordinates are {self.__current_gps_coordinates}")
        else:
            print("Access denied")


# Polymorphism
# same method name but different implementation in different classes. (method overloading and method overriding)


#polymorphic function - doesn't care about the type of object, it can work with any object that has the required method.
# it only cares about the method name and its implementation. (duck typing) exists


class Paypal:
    def process_payment(self,amount):
        print(f"Processing payment of {amount} using Paypal")
class Gpay:
    def process_payment(self,amount):
        print(f"Processing payment of {amount} using Gpay")
class CreditCard:
    def process_payment(self,amount):
        print(f"Processing payment of {amount} using Credit Card")

def execute_payment(payment_gateway,amount):
    payment_gateway.process_payment(amount)


# Abstarction part-2
# when you are inheriting the blueprint of a class you need to write the logic for the methods in the child class. (abstract class and abstract methods)

from abc import ABC, abstractmethod
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self,message):
        pass
    @abstractmethod
    def read_notification(self):
        pass
    def add_notification(self):
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self,message):
        return f"Sending email notification: {message}"
    def read_notification(self):
        return "Reading email notification" 



