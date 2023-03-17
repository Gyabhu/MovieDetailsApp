import json

filename = 'heros.json'

def update(id,key,value):
    with open(filename,'r') as fp:
        heros = json.load(fp)
    hero = list(filter(lambda x: x['id'] == id , heros)) # Checks if id is in the json
    hero = hero[0] # This variable contains the user selected data
    index_of_hero = heros.index(hero) # We find the index of user selected information
    change = heros[index_of_hero] # We select the index of the info we want to update
    change[key] = value # We update the value using key and value provided by the user

    with open(filename,'w') as fp:
        json.dump(heros,fp, indent=2)

    cont = input("Updated Sucessfully, Do you want to continue? Y/N: ")
    return True if cont.lower() =='y' else False