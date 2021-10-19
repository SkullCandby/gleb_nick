import os
from random import randint
class Shablon:
    def __init__(self,filename):
        self.params = {}
        f = open(filename, 'r', encoding="UTF-8")
        lines = f.readlines()
        for line in lines:
            l = line.split()
            self.params[l[0]] = l[1:]
        f.close()

class Roddom:
    def gen(self, shablon, filename):
        creations = {}
        f = open(filename, 'r', encoding="UTF-8")
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            creations[line] = {}
            for param, value in shablon.params.items():
                if len(value) == 1:
                    creations[line][param] = int(value[0])
                if len(value) == 2:
                    creations[line][param] = int(randint(int(value[0]),int(value[1])))
                print(param, creations[line][param])
            #    self.creations[line.strip()] = shablon.params.copy()
        f.close()
        return creations


roddom = Roddom()
shablons = {}
bodies = {}

for root, dirs, files in os.walk("./SHABLONS"):
    for filename in files:
        shablons[filename] = Shablon("SHABLONS/"+filename)
        if  os.path.exists("OBJECTS/"+filename):
           bodies[filename] = roddom.gen(shablons[filename], "OBJECTS/"+filename)




print(bodies)
for type,list in bodies.items():
    print(type,':')
    for item,data in list.items():
        print(item, '->' ,data)
    print()

f = open("f.txt",'w')
f.write("%s"%bodies)
f.close()