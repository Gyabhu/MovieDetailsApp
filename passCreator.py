import json

password = input("Enter Password: ")

with open("SavedPass.json",'w') as fp:
    json.dump(password,fp)

