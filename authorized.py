import json

pass_file = 'SavedPass.json'

with open(pass_file,'r') as fp:
    password = json.load(fp)

def authorized(func):
    def inner(*args,**kwargs):
        pwd = input("Enter Password: ")
        if pwd == password['password']:
            return func(*args,**kwargs)
        else:
            print("Not Authorised")
    return inner