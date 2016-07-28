import simplejson as json
from mechs import Mech

file_dir = "mechdata.json"
valid = True
found = False

with open(file_dir) as data_file:
    data = json.load(data_file)

for item in data['mechs']:
    print(item['name'])

while valid:
    newPlayerMech = input("Choose Mech: ")
    newPlayerMech = newPlayerMech.lower()
    for result in data['mechs']:
        if result['name'] == newPlayerMech:
            playerMech = Mech(
                result['id'],
                result['name'],
                result['mass'],
                result['endo_steel'],
                result['power_plant'],
                result['xl'],
                result['walking_speed'],
                result['running_speed'],
                result['jump_jets'],
                result['jump_distance'],
                result['ferro_fibrous'],
                result['armor_mass'],
                result['armor_factor'],
                result['heat_sinks'],
                result['dbl_heat_sinks'])
            print("Mech construction successful. You chose: %s" % playerMech.getName())
            found = True
            valid = False
    if found is not True:
        print("Mech not available. Please choose a Mech from the models available.")
