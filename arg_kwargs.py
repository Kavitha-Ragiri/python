def name(*arg):
    print(arg)
    for i in arg:
        print(i)
name(1,3,4)
name(23,34,56,78,45)

def details(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
details(name="nani", age=24)
details(salary=2000, gender="male",dept="IT")

