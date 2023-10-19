""" 
Inheritance. Create several classes that demonstrate the inheritance. Add the code execution to see that it works.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_yourself(self):
        print("Hello!")


class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def introduce_yourself(self):
        print("Hello! My name is {} and I am a {}.".format(self.name, self.job_title))


employee = Employee("Piotr Rokita", 12, "Software Engineer")

employee.introduce_yourself()
