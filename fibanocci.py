#fibonacci number using recursion

def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(7))


#fibonacci series
value =int(input("enter range:"))
num1 = 0
num2 = 1
next_number = num2  

for i in range(value):
    print(next_number,end=" ")
    num1 = num2
    num2=next_number
    next_number = num1 + num2
