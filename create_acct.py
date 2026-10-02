import json
def create_acct(name1, name2, name3, number, password):
      with open("users.json", "r")as file:
            data = json.load(file)

      user_details = [{
            "First_Name": name1,
            "Middle_Name": name2,
            "Last_Name": name3,
            "Number": number,
            "Password": password
      }]        
      data.append(user_details)

      with open("users.json", "w") as file:
            json.dump(data, file, indent=4)
