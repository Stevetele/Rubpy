class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def onyesha(self):
        print(f"My name is {self.name} I'm {self.age} years and I'm a {self.gender}")

# obj inst
myobj=Person("Steve",20, "male")
myobj2=Person("Sandra",19,"female")
myobj.onyesha()