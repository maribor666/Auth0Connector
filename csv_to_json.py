import csv
import json

csv_file = open('./Samples/query_data_1.csv')
jsonfile = open('Samples/Auth0AMSamples_1.json', mode='w')

fieldnames = csv_file.readline().split(',')
# print(fieldnames)
reader = csv.DictReader(csv_file, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(',\n')
