import json

with open("SavedPass.json",'r') as fp:
    password = json.load(fp)

def authorized(func):
    def inner(*args,**kwargs):
        pwd = input("Enter Password: ")
        if pwd == password:
            return func(*args,**kwargs)
        else:
            print("Not Authorised")
    return inner