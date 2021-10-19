import os
import random


class Shablon:
    def __init__(self, filename):
        self.params = {}
        f = open(filename, 'r', encoding="UTF-8")
        lines = f.readlines()
        for line in lines:
            l = line.split()
            self.params[l[0]] = random.randint(int(l[1]), int(l[2]))
        f.close()


class Roddom:
    def gen(self, filename1, name):
        self.creations = {}
        shablon = Shablon(filename1)
        self.creations[name] = shablon.params.copy()
        return self.creations


class Biom:
    def __init__(self, filename):
        self.params = {}


class Hood:
    def __init__(self, rod):
        self.bioms = os.listdir("BIOMS/")
        self.params = {}
        objects = []
        self.roddom = rod
        print(*self.bioms)
        self.path1 = input("Ввыберите биом из заданных ")
        while self.path1 not in self.bioms:
            self.path1 = input(f"Введите один из доступных биомов {' '.join(self.bioms)} ")
        for i in range(len(self.bioms)):
            f = open("BIOMS/" + self.path1, 'r', encoding="UTF-8")
            lines = f.readlines()
            for line in lines:
                objects.append(line.split()[0])
                objects = set(objects)
                objects = list(objects)
        print(objects)
        self.path2 = []
        self.path4 = []
        self.path3 = input("Что там будет? ").split()
        for i in range(0,len(self.path3)):
          if self.path3[i] in objects:
            self.path2.append(self.path3[i])

        print("OAOAOAOЗ",self.path2)
        print("-->", self.path4)
    def info(self):
        for items,values in self.params.items():
            print(items,values)




    def create(self):
        print(self.path1, self.path2, self.path2, "HDWAUOHDWUHDOUDAHWOHDWLUHD")
        print(self.params)
        for i in range(len(self.path3)):
            try:
                print(self.roddom.gen("SHABLONS/" + self.path3[i], self.path3[i]))
                self.params[self.path3[i]] = (self.roddom.gen("SHABLONS/" + self.path3[i], self.path3[i]))
            except KeyError:
                print(self.params)

        f = open('HOODS/' + input("В какой район хотите поместить"), 'w', encoding='UTF-8')
        f.write(str(self.params))
        f.close()
roddom = Roddom()
hood = Hood(roddom)
hood.create()
hood.info()

"""cheloveki = roddom.gen("SHABLONS/Tree", 'OBJECTS/Tree')
kapybara = roddom.gen("SHABLONS/kapybara", "OBJECTS/kapybara")"""

files_shablon = os.listdir("SHABLONS/")
files_objects = os.listdir("OBJECTS/")

arr = []
"""for i in range(len(files_objects)):
    if files_objects[i] in files_shablon:
        arr.append(roddom.gen("SHABLONS/" + files_objects[i], "OBJECTS/" + files_objects[i]))"""

"""for i in range(len(arr)):
    for body, params in arr[i].items():
        print(body, params)"""
