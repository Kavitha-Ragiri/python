x=int(input("enter x value"))
y=int(input("enter y value"))
z=int(input("enter z value"))

if x>y and x>z:
    print(f"x is greater:{x}")
elif y>x and y>z:
    print(f"y is greater:{y}")
else:
    print(f"z is greater:{z}")

