# class House():
#     """rfveeevf"""
#     def __init__(self,street,number,floor):
#         self.street = street
#         self.number = number
#         self.floor = floor
#     def check_build(self):
#         print("Dom nomer", self.number,"na ulise",self.street,"uje dostroen")
#
# House1 = House("Moscow",20,9)
# House2 = House("Toktogul",18,12)
# # print(House1.street)
# print(House1.check_build())

class Human():
    """характеристика 3 обьектов"""
    def __init__(self,name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def check(self):
        if self.height < 165:
            print(self.name ,"small")
        elif self.height < 170:
            print(self.name, "middle")
        elif self.height < 185:
            print(self.name, "big")

Human1 = Human(input(), 34,166)
Human2 = Human("Jack", 40,180)
Human3 = Human("Begi",23,160)

# print(Human1.name,Human2.name)
# print(Human3.name ,Human3.age,Human3.height)
# print(Human1.check(),Human2.check(),Human3.check())

print(Human1.name,Human1.age)
print(Human1.check())

class Car():
    """cars """
    def __init__(self):
        self.age = age
        self.volume = volume
        self.

