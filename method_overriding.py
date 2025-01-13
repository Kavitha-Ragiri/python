class father:
    def sleep(self):
        print("sleep at 10:00PM to 6AM")
    def eat(self):
        print("eat healthy food")
class son(father):
    def sleep(self):
        print("sleep at 11:00PM to 8AM")
    

obj=son()
obj.sleep()
obj.eat()