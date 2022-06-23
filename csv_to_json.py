
import json
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"sales":[]}
    for row in reader:
        data["sales"].append({"collection_name":row[0], "asset_url":row[1],"asset_img_url":row[2], "event_contract_address":row[3], "event_quantity":row[4], "event_total_price":row[5]})

with open ("data.json", "w") as f:
    json.dump(data, f, indent=4)
