import json
filename = 'heros.json'

def read(id):
    with open(filename,'r') as fp:
        heros = json.load(fp)

    read_data = list(filter(lambda x: x['id'] == id, heros))
    print(read_data)

    cont = input(f"Do you wish to view more? Continue? (y/n) ")
    return True if cont.lower() =='y' else False
