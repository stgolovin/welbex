import csv
import json



data_dict = dict()

cities_list = list()
states_list = list()
zips_list = list()
latitudes_list = list()
longitudes_list = list()

with open('uszips.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:        
        cities_list.append(row[3])
        states_list.append(row[5])
        zips_list.append(row[0])
        latitudes_list.append(row[1])
        longitudes_list.append(row[2])

cities_list = cities_list[1:]
states_list = states_list[1:]
zips_list = zips_list[1:]
latitudes_list = latitudes_list[1:]
longitudes_list = longitudes_list[1:]



# for item in cities_list:
#     data_dict['cities'] = item


# data_dict['cities'] = cities_list
# data_dict['states'] = states_list
# data_dict['zips'] = zips_list
# data_dict['latitudes'] = latitudes_list
# data_dict['longitudes'] = longitudes_list

# with open('data.json', 'w') as file:
#     json.dump(data_dict, file)


# открыть json как объект python
# with open('data.json', 'r') as file:
#     data = json.load(file)

# data_dict['model'] = 'cargo.location'
# data_dict['pk'] = 'pk'


for zip in zips_list:
    str(zip)

data = []


for i in range(len(cities_list)):
    item = {
        "model": "cargo.location",
        "pk": i+1,
        "fields": {
            "city": cities_list[i],
            "state": states_list[i],
            "zip": zips_list[i],
            "latitude": latitudes_list[i],
            "longitude": longitudes_list[i],
        }
    }
    data.append(item)

json_data = json.dumps(data)

# with open('json_file.json', 'w') as f:
#     f.write(json_data)



# def save_to_db(cities_list):
#     for item in cities_list:
#         object = Location(city=item)
#         object.save()

# save_to_db(cities_list)


# for obj in cities_list:
#     obj = Location(city=location[0], longitude=location[1])
#     obj.save()

# for city, state in cities_list, states_list:
#     print(city)
#     print(state)

