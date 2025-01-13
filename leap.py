year=int(input("enter a year: "))

if year%4==0 and year%400==0:
    print(f"given {year} is a leap year")
else:
    print(f"given {year} is not a leap year") 