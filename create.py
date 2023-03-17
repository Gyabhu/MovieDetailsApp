import os
import json
from authorized import authorized
filename = 'heros.json'

@authorized
def create():
    id = int(input("Enter your id: "))
    name = input("Enter your name: ")
    mission = input("Enter your mission: ")
    hero = dict(id = id,name =name,mission = mission)
    if os.path.exists(filename):
        with open(filename,'r') as fp:
            heros = json.load(fp)
    else:
        heros = []
    heros.append(hero)

    with open(filename,'w') as fp:
        json.dump(heros,fp, indent=2)

    cont = input(f"Congratulations {name} you are a Hero! Continue? (y/n) ")
    return True if cont.lower() =='y' else False
