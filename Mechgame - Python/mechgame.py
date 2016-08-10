import simplejson as json
from mechs import Mech
from weapons import Weapon
import bt_functions as btf

mech_file_dir = "mechdata.json"
weapons_file_dir = "weapons.json"
valid = True
found = False
count = 0

with open(mech_file_dir) as mech_file:
    mdata = json.load(mech_file)
with open(weapons_file_dir) as weapon_file:
    wdata = json.load(weapon_file)

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
            print("\n...Base Mech construction successful...")

            print("\n...Beginning weapon and equipment construction...")
            wIDs = playerMech.getWandE()
            btf.printDict(wIDs)
            newWeapons = btf.objectifyByID(wIDs,wdata)
            btf.printDict(newWeapons)

            found = True
            valid = False
    if found is not True:
        print("Mech not available. Please choose a Mech from the models available.")
