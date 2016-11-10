#comparing values with if
def comparison(x,y):
    if (x > y):
        return x
    elif(y > x):
        return y
    else:
        return "You got Danked"

print comparison(5,10)
print comparison(10,5)
print comparison(10,10)

#YOU CAN DO THE BLOCK IN ONE LINE WUUUT
def oneLineComparisons(x,y):
    toBPrinted = "x is less than y" if (x < y) else "x is greater than or equal to y"
    return toBPrinted

print oneLineComparisons(5,10)
print oneLineComparisons(10,10)

#Loop structures

#while loops
def whileLoop(x):
    while (x<10):
        print(x)
        x=x+1

whileLoop(6)

#for loops
def forLoop(x):
    for i in range (x,10):
        x=x+1
        print x

forLoop(6)

#Collections/Arrays with for loops
def arrayLooper(x):
    for i in x:
        print(i)

x = [1,2,3,4,5,6]
arrayLooper(x)

#using enumerate() to get the index
def enumerator(x):
    for i,d in enumerate(x):
        print i,d

y = ["hi", "wassup"]
enumerator(y)
