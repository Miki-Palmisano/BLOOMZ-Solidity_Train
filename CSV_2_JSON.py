import csv
import json

csv_file = './dataset.csv'
json_file = './dataset2.json'

data = []

with open(csv_file, 'r') as file:
    csv_data = csv.DictReader(file)
    for row in csv_data:
        data.append(row)

with open(json_file, 'w') as file:
    json.dump(data, file, indent=4)