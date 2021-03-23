# your code here
print("Hello World")

##function YouTube Tutorial
def greet(first_name,last_name):
    print(f"Hello {first_name} {last_name}")
    print("Yessss!")


greet("Sil", "Montes")

#Tyoes of functions 
# 1.Functions that perform a task. The one above performs a task
# 2.Functions that return a value The following returns a calculates and returns a value

def get_greeting(name):
    return f"Hi {name}!"

#as the functions returns something, we can store the result in a variable and do whatever we what with it
greeting=get_greeting("Sil")
print(greeting)

# Keyword arguments

def increment(number,by):
    return number + by

#in here, by is the keyword argument and allows us to understand better what it is doing as an argument
print(increment(2,by=1))

#Default Arguments: this makes the parameter optional IMPORTANT: the default or optional parameters must be the last ones
def increment2(number,by=1): #if the second parameter is not suply, 1 will be used
    return number + by

print(increment2(2))
print(increment2(2,5)) #the second argument can also be modified

# *args
