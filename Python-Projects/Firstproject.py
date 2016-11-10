#Working with local variables
a = 3
print(a)


def main():

    #Obligatory hello world stuff xD
    print("Hello World!")

    #working with variables
    #global declares the variable as a global variable
    global a
    a = 6
    b = 8
    print(a+b)

    #Working with String concatenation
    c = "Hello, wassup!"
    #this doesn't work because the compiler doesn't cast the int to a string
    #print(c+a)
    #instead, do this.
    print(c+" " + str(a))

    #note that the new line is the same as it is in jave \n
    #so,
    print(c + "\n" + str(a))

#checking if the variable has been modified
main()
print(a)

#messing with checking if this is executed as a program
#Calls the amin method!
if __name__ == "__main__":
    main()
