# A simple function
def greet(name):
    return "Hello " + name


# (a) Assign function to another variable
new_greet = greet

print(new_greet("Rahul"))


# (b) Pass function as an argument
def execute_function(func, name):
    print(func(name))


execute_function(greet, "Sita")


# (c) Return a function from another function
def create_greeting():
    def message(name):
        return "Welcome " + name

    return message


greeting_function = create_greeting()
print(greeting_function("Amit"))
