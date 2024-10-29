class Fruits:
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"My favourite fruit is {self.name} its {self.shape} in shape and costs {self.price} shillings")
# create instance of a clas


myobject=Fruits(20,"oval","Banana")
myobject.display()

class