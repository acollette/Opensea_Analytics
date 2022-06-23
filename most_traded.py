import json
f = open('data.json')

data= json.load(f)

def contains(list, filter):
    for x in list:
        if filter(x):
            return True
    return False

class Collections(object): 
    def __init__(self, id, name, image, contract_address, quantity, price): 
        self.id = id
        self.name = name 
        self.image = image
        self.contract_address = contract_address
        self.quantity = quantity
        self.price = price

collection_list = []

## Step 1: We create a list of unique values of the collections
id = 0
for i in data['sales']:
    collection_name = i["collection_name"]
    image = i["asset_img_url"]
    contract = i["event_contract_address"]
    
    if contains(collection_list, lambda x: x.name == collection_name)  :
        pass
    else:
        collection_list.append(Collections(id, collection_name, image, contract, 0,0 ))


##image = i["asset_img_url"]
##contract = i["event_contract_address"]
##quantity = i["event_quantity"]
##price = i["event_total_price"]
##collection_list.append(collections(collection_name, image, contract, quantity, price)
 
print(collection_list)

collection_list_object = collection_list


## Step 2: We loop over the unique collection objects and will sum up values
for i in collection_list_object:

    for y in data["sales"]:
        if y["collection_name"] == i.name:
            i.quantity += float(y["event_quantity"])
            i.price += float(y["event_total_price"])

collection_list_object.sort(key=lambda x: x.quantity, reverse = True)

for i in collection_list_object:
    id +=1
    i.id = id



with open ("most_traded_data.json", "w") as f:
    json.dump(collection_list_object, f, indent=4, default=vars)

