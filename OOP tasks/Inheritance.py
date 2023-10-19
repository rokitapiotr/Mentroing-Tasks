""" 
Inheritance. Create several classes that demonstrate the inheritance. Add the code execution to see that it works.
"""


class Person:
    def __init__(self, name):
        self.name = name

    def introduce_yourself(self):
        print("Hello!")


class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title

    def introduce_yourself(self):
        print("Hello! My name is {} and I am a {}.".format(self.name, self.job_title))


employee = Employee("Piotr Rokita", "Software Engineer")

employee.introduce_yourself()
