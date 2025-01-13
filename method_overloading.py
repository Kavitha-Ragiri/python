#method over loading

class demo:
    def add(self,*args):
        total=0
        for i in args:
            total+=i 
        return total
    
obj=demo()
print(obj.add(2,3))
print(obj.add(24,56,76,45))
print(obj.add(9,6,8,4,3,65,78,34))