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
                _id=result['_id'],
                model=result['model'],
                name=result['name'],
                mass=result['mass'],
                endo_steel=result['endo_steel'],
                power_plant=result['power_plant'],
                xl=result['xl'],
                walking_speed=result['walking_speed'],
                running_speed=result['running_speed'],
                jump_jets=result['jump_jets'],
                jump_distance=result['jump_distance'],
                ferro_fibrous=result['ferro_fibrous'],
                armor_mass=result['armor_mass'],
                armor_factor=result['armor_factor'],
                heat_sinks=result['heat_sinks'],
                dbl_heat_sinks=result['dbl_heat_sinks'],
                w_and_e=result['w_and_e'])
            print("\n...Base Mech construction successful...")

            print("\n...Beginning weapon and equipment construction...")
            wIDs = playerMech.getWandE()
            # btf.printDict(wIDs)
            newWeapons = btf.objectifyByID(wIDs,wdata)
            # btf.printDict(newWeapons)
            playerMech.setWandE(newWeapons)
            count = 1
            for key, value in playerMech.getWandE().items():
                for item in value:
                    print("{}) {}".format(count,item.getName()))
                    count+=1
            found = True
            valid = False
    if found is not True:
        print("Mech not available. Please choose a Mech from the models available.")
