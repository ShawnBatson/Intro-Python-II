from category import Category

# OOP Object Oriented Programming
# Objects (or Classes)
# Blueprints/Prototype
# holds data : attributes
# methods : functions

# instance of a class - Creating an instance of an object in your code

# PET BLUEPRINT CLASS
# name
# height
# gender
# species
# diet
# number of legs

# methods:
# feed_pet()
# play()


class Store:
    # attributes
    # name
    # categories (departments)

    # constructors =  the function that runs every time you create a new instance
    # self refers to the current instance of the Class (this in JS)

    # initialize the class
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    # str is used to make the class a string (printing)
    def __str__(self):
        output = f"Welcome to {self.name}!"
        i = 1
        for category in self.categories:
            output += f"\n {1}. {str(category.name)}"
            i = + 1
        return output

    def __repr__(self):
        # also returns a string
        # this is not as user friendly as STR
        # This is for helping developers debug
        return f"self.name = {self.name} ; self.categories = {self.categories}"


running_category = Category("Running", "All your running needs", [])
baseball_category = Category("Baseball", "Cardinals fans only", [])
basketball_category = Category("Basketball", "Indoor and outdoor products", [])
football_category = Category("Football", "The American Kind", [])


sports_store = Store("Gander Mountain", [
                     running_category, baseball_category, basketball_category, football_category])
produce_store = Store("Trader Joes", ["Dairy", "Meat", "Bread", "Produce"])

# print(sports_store)
# print(produce_store)
# print(sports_store.name)
# print(repr(sports_store))
# print(running_category)

#===================================================#

# MAIN INDEX.JS FILE AREA. IN HERE FOR LECTURE
choice = -1
# REPL <--- Read Evaluate Print Loop
print(sports_store)
print("Type 0 to quit")
# while choice != 0:
while True:
    # Read part
    choice = input("Please Choose a category (#): ")
    try:
        if (choice == "q"):
            break
        # evaluate
        choice = int(choice) - 1
        if choice >= 0 and choice < len(sports_store.categories):
            chosen_category = print(sports_store.categories[int(choice) - 1])
            # print
            print(chosen_category)
        else:
            print("The number is out of range")
    except ValueError:  # this is the error name given in terminal
        print("Please enter a valid number")
    finally:
