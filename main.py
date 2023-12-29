import re

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setname(self,name1):
        if re.search('\d',name1) is not None:
            print("Ім'я повинно бути без цифр")
        else:
            self.__name = name1

    def setage(self,age1):
        if age1 > 120 or age1 < 0:
            print("Вік повинен бути в діапазоні від 0 до 120 років")
        else:
            self.__age = age1

    def say(self):
        print(f"Я {self.__name}, мені {self.__age} років")


misha = Person("Misha", 28)
misha.setname("Misha Sa4han")
misha.setage(290)
misha.say()
