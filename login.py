import json

def login(number, password):
   
   with open("users.json", "r")as file:
       data = json.load(file)
    
       for all_data in data:
        
            if all_data['Number'] == number and all_data['Password'] == password:
                return True
            
       print("Invalid number or password")
       return False        
                        