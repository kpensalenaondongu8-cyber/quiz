import json
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

with open("resource.json", "r")as file:
    data = json.load(file)

def resource_invet(id, name, category, available_unit):
    found = False
    
    for item in data:
        if item['id'] == id:
            found = True  
            break         
            
    if found:
        print("Id already exists")
        return data
    else:    
        new_resource = {
                "id": id,
                "name": name,
                "category": category,
                "total": available_unit,
                "available": available_unit
            }
    data.append(new_resource)
    with open("resource.json", "w") as file:
          json.dump(data, file, indent=4)
    return("item added succesfully")
    
 



def borrow(fellow_id, resource_id, quantity):
    # 1. Load fresh data from the file
    with open("resource.json", "r") as file:
        data = json.load(file)

    # 2. Find the resource
    matched = None
    for item in data:
        if item['id'] == resource_id:
            matched = item
            break  

    if not matched:
        return "Resource ID does not exist."
    
    if quantity <= 0 or quantity > matched["available"]:
        return f"Too many or low order. Reduce the quantity. We only have {matched['available']} units of '{matched['name']}' now."

    if fellow_id not in fellows:
        return "Fellow ID does not exist."

    matched['available'] -= quantity
    
    with open("resource.json", "w") as file:
        json.dump(data, file, indent=4)

    return f"User at ID {fellow_id} borrowed {quantity} units of '{matched['name']}"