
def emobilisruby(name, age, gender):
    print(f"Student name is:{name}, {age}, {gender}")

emobilisruby("Steve", 20, "male")

def reg(name, country, email):
    print(f"Thankyou for registering. Welcome {name} from {country}. You shall receive updated through {email}")

reg("Steve","Kenya","stevetele@gmail.com")

def calc():
    num=int(input("Enter a first number: "))
    num2=int(input("Enter a second number: "))
    print(f"The sum of {num} and {num2} is {num+num2} while the product is {num*num2} and quotient is {num//num2}")

calc()

def bmi():
    weight=int(input("Add your weight in Kg: "))
    height=int(input("Add your height in ft:"))
    num3=float(2.5)
    print(f"Your Body Mass Index 'BMI' is {weight//height*(num3)}")

bmi()





