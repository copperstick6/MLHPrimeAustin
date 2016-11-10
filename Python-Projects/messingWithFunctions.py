def function1():
    print("I like turtles")
function1()

#print statement tries to print the return, but there is none, so it prints
#none
print function1()

#not invoking the function with the parenthesis prints the
#memory location of the object, as all functions are stored
#as an object wihin python
print function1

#functions can be stored as variables
x = function1
x()

#note that + in java is the same as , in python.
def function2(x,y):
    print x, " ", y

function2(3,4)
print function2(3,4)

#return functions
def cubed(x):
    return x*x*x

print cubed(3)
a = cubed(3)
print(a)
