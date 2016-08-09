import simplejson as json
from mechs import Mech

mech_file_dir = "mechdata.json"
weapons_file_dir = "weapons.json"
valid = True
found = False

with open(mech_file_dir) as mech_file:
    mdata = json.load(mech_file)

for item in mdata['mechs']:
    print(item['name'])

while valid:
    newPlayerMech = input("\nChoose Mech: ")
    newPlayerMech = newPlayerMech.upper()
    for result in mdata['mechs']:
        if result['name'] == newPlayerMech:
            playerMech = Mech(
                result['_id'],
                result['model'],
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
                result['dbl_heat_sinks'],
                result['w_and_e'])
            print("\n...Mech construction successful...")
            wIDs = playerMech.getWandE()
            with open(weapons_file_dir) as weapon_file:
                wdata = json.load(weapon_file)
            for key,value in wdata.items():
                for item in value:
                    if item['_id'] is 8:
                        print(item)
            for key, val in wIDs.items():
                if val:
                    for item in val:
                        print(key,item)
            found = True
            valid = False
    if found is not True:
        print("Mech not available. Please choose a Mech from the models available.")
