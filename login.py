import json

def login(number, password):
   
   with open("users.json", "r")as file:
       data = json.load(file)
       
        