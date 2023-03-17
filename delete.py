import json
filename = 'heros.json'

def delete(id):
    with open(filename,'r') as fp:
            heros = json.load(fp)
    hero = list(filter(lambda x: x['id']==id,heros))
    hero = hero[0]
    heros.remove(hero)
    # index_of_hero = heros.index(hero)
    # heros.pop(index_of_hero)

    with open(filename,'w') as fp:
        json.dump(heros, fp, indent=2)

    cont = input("Sucessfully deleted, Continue? Y/N: ")
    return True if cont.lower()=='y' else False