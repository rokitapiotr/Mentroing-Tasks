"""
Encapsulation. Create simple examples of how we can use this paradigm.
"""


class Secret:
    def __init__(self):
        self._protected_attribute = "This is a protected attribute"
        self.__private_attribute = "This is a private attribute"

    def access_attributes(self):
        print("Protected attribute:", self._protected_attribute)
        print("Private attribute:", self.__private_attribute)

    def change_private_attribute(self, new_value):
        self.__private_attribute = new_value


obj = Secret()

obj.access_attributes()

print("Attempt to access from outside:")
print("Protected attribute from outside:", obj._protected_attribute)  # Accessible from outside

# Change the private attribute using a method
obj.change_private_attribute("New value for the private attribute")
print("Private attribute after change:", obj.__private_attribute)  # Accessible from outside
