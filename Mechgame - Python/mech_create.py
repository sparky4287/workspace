import simplejson as json
from mechs import Mech
from weapons import Weapon
import bt_functions as btf

def create_mech():

    # Load data from JSON files
    mech_file_dir = "mechdata.json"
    weapons_file_dir = "weapons.json"
    with open(mech_file_dir) as mech_file:
        mdata = json.load(mech_file)
    with open(weapons_file_dir) as weapon_file:
        wdata = json.load(weapon_file)

    # Set Mech validator
    found = False

    for item in mdata['mechs']:
        print("{:12} {} tons".format(item['name'], item['mass']))

    newPlayerMech = input("\nChoose Mech: ")
    newPlayerMech = newPlayerMech.upper()
    while not found:
        for result in mdata['mechs']:
            if result['name'] == newPlayerMech:
                # playerTeam[playerMech] = Mech(
                playerMech = Mech(
                    _id=result['_id'],
                    model=result['model'],
                    name=result['name'],
                    mass=result['mass'],
                    power_plant=result['power_plant'],
                    walking_speed=result['walking_speed'],
                    running_speed=result['running_speed'],
                    jump_jets=result['jump_jets'],
                    jump_distance=result['jump_distance'],
                    armor_mass=result['armor_mass'],
                    armor_factor=result['armor_factor'],
                    heat_sinks=result['heat_sinks'],
                    w_and_e=result['w_and_e'],
                    endo_steel=result['endo_steel'],
                    xl=result['xl'],
                    ferro_fibrous=result['ferro_fibrous'],
                    dbl_heat_sinks=result['dbl_heat_sinks'])
                print("\n...Base Mech construction successful...")

                print("\n...Beginning weapon and equipment construction...")
                wIDs = playerMech.getWandE()
                newWeapons = btf.objectifyByID(wIDs,wdata)
                playerMech.setWandE(newWeapons)
                # count = 1
                # for key, value in playerMech.getWandE().items():
                #     for item in value:
                #         print("{}) {}".format(count,item.getName()))
                #         count+=1
                found = True
        if found is not True:
            print("Mech not available. Please choose a Mech from the models available.")
    return playerMech