class Person:
   
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

  
    def sayHello(self):
        print("Hello " + self.name + ", Nice to meet you")

    def ride(self):
        self.sayHello()
        if self.age > 10 and self.height > 100:
            print("Congrats " + self.name + ", you may ride a roller coaster")
        else:
            print("Sorry " + self.name + ", you may not ride a roller coaster")

james = Person("james", 10, 140)
rose = Person("rose", 12, 150)
dove = Person("dove", 12, 150)
diva = Person("diva", 8, 130)            

while True:
    name = input("Enter name : ")

    if name == "james":
        james.ride()
    elif name == "rose":
        rose.ride()
    elif name == "dove":
        dove.ride()
    elif name == "diva":
        diva.ride()
    else:
        print("Invalid input")

    ans = input("'y' to continue / 'n' to quit : ")
    if ans == "n":
        break