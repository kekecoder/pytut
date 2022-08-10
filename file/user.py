import json

username = input('What is your name?: ')
filename = 'username.json'
with open(filename, 'w') as file_obj:
    json.dump(username, file_obj)
    print("We'll remember you wen you come back " + username + "!" )