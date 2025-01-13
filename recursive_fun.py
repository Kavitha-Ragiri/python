

#Recursive function

def fact(a):
    if a==1:
        return 1
    else:
        return a*fact(a-1)
number=int(input("Enter a number:"))
print(fact(number))

   