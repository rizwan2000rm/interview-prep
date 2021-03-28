# The members of a class that are declared public are easily accessible from any part of the program.
# All data members and member functions of a class are public by default.

# program to illustrate public access modifier in a class
class Geek:

    # constructor
    def __init__(self, name, age):

        # public data mambers
        self.geekName = name
        self.geekAge = age

    # public memeber function
    def displayAge(self):

        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("Rizwan", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.displayAge()
