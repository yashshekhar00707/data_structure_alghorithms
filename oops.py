import csv


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self):
        self.age = age

d1 = Dog("Tim", 10)
print(d1.get_age())

# ******************************************

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 1 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/ len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.students[0].name)
print(course.students[1].age)
print(course.get_average_grade())

# *************************************
# Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I am.")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def speak(self):
        print("Meow")
    def show(self):
        print(f"My name is {self.name} and I am {self.age} years old and I am {self.color}.")

class Dog(Pet):
    def speak(self):
        print("bark")

class Fish(Pet):
    pass

p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 34, "Brown")
c.show() # This will give the output for show method which is defined in the Pet class as it
# inherits all the methods of Pet class
d = Dog("Jill", 25)
d.show()
p.speak() # This will give the output for the method defined in the Pet class as its instance is for Pet class
c.speak() # This will give the output for the method defined in the Cat class because if 2 methods are defined
# with same name in both parent class and child class the preference is given to the method of child class
d.speak()
f = Fish("Bubbles", 10)
f.speak()

# ***********************************************

# Decorators use
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())  # This will return 2 because class methods
# (Person.add_person()) is adding 1 each time we are creating an instance

# **************************************************

# STATIC METHOD

class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

print(Math.add5(10))
print(Math.add10(10))

# ************************************************

class SoftwareEngineer:

    # class attribute
    alis = "Keyboard Magician" # This is a class attribute and will be applicable to both class
                               # and all the instances for this class

    def __init__(self, name, age, level, salary): #this is called d_under method and its not required to call this method
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    def __str__(self):
        print(f"name = {self.name}, age = {self.age}, level = {self.level}")

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    @staticmethod # using this decorator, the defined function is not tied to any specific instance and can be applied
    def entry_salary(age): # to both the instance and class but we cannot access the self attributes in here
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        else:
            return 9000


se1 = SoftwareEngineer("Rahul", 20, "Junior", 5000)
se2 = SoftwareEngineer("Mohan", 25, "Senior", 8000)
se3 = SoftwareEngineer("Mohan", 25, "Junior", 9000)
se1.code()
se2.code()
se1.code_in_language("Python")
se2.code_in_language("C++")

print(se2 == se3)
# Topics covered
# instance method(self)
# can take the arguments and return values
# special "dunder" method (__str__ and __eq__)
# @staticmethod which are called decorators

# ********************************************************

# Inheritance
# The child class inherits all the attributes and functions from the parent class

class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")


class SofwareEngineer(Employee):

    def __init__(self, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging...")

    def work(self):
        print(f"{self.name} is coding in Python...")

class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing...")

    def work(self):
        print(f"{self.name} is designing something...")

se1 = SofwareEngineer("Naman", 23, 6000, "Junior")
print(se1.name, se1.age)
se1.work()
print(se1.level)
d1 = Designer("Raksha", 24, 5000)
print(d1.name, d1.age)
d1.work()
se1.debug()
d1.draw()

# If we define a function/method in the child class with the same name as defined in the parent class, this is called
# overriding and the method/function defined inside the child class will be given preference. If we define a method
# or function in the child class with new name, this is called extend. This new method or function is defined inside the
# child class and is specific to the child class itself.

# POLYMORPHISM

employees = [SofwareEngineer("Jacob", 23, 6000, "Junior"),
             SofwareEngineer("Minion", 23, 6000, "Junior"),
             Designer("Joshua", 24, 5000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

#**************************************************************

# Encapsulation

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_bugs_solved = 0

    def code(self):
        self._num_bugs_solved += 1

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

se5 = SoftwareEngineer("Max", 25)
print(se5.age, se5.name)

for i in range(70):
    se5.code()
se5.set_salary(5000)
print(se5.get_salary())


# Pythonic way of performing above action

class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    @salary.deleter
    def salary(self):
        del self._salary


se = SoftwareEngineer()

se.salary = 6000
print(se.salary)

# ******************************************************

import csv
class Item:

    pay_rate = 0.8  # this is a class attribute and we are  setting this to 0.8 as we are giving 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to receive arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0 " # by this we are restricting the value to be +ve integer,
        assert quantity >= 0 , f"Quantity {quantity} is not greater than or equal to 0 "  # if  the user enters negative integer it will throw assertion error

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_price(self):
        total = self.price * self.quantity
        return total

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):  # This is a magic method to names of instances
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod # using this the method will not take the instance as default argument unlike with above written methods
    def is_integer(num):
        # we will count out the floats with point zero
        # eg 10.0, 5.0 will be considered as integers
        if isinstance(num, float):
            # count out the floats with point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(item1.calculate_price())
# print(item2.calculate_price())

# print(Item.pay_rate)
# print(Item.__dict__)  # This will return all the attributes for class level
# print(item1.__dict__)  # This will return all the attributes for the instance level

# item1.apply_discount()
# print(item1.price)
#
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.all)
# Item.instantiate_from_csv()
# print(Item.all)
print(Item.is_integer(10.3))