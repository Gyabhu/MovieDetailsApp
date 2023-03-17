import json


def ask_pwd():
    password = input("Set New Pass: ")
    new_pass = dict(password = password)

    with open("SavedPass.json",'w') as fp:
        json.dump(new_pass,fp)
    print(f'Password set Sucessfully!')

