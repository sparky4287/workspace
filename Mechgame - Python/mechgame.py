import simplejson as json
from mechs import Mech
from weapons import Weapon
import bt_functions as btf

mech_file_dir = "mechdata.json"
weapons_file_dir = "weaponsdata.json"
valid = True
count = 0

with open(mech_file_dir) as mech_file:
    mdata = json.load(mech_file)
with open(weapons_file_dir) as weapon_file:
    wdata = json.load(weapon_file)

menu_choices = {'1','2','3','4'}

menu_choice = input("This would be the initial menu choice. Choose the option to pick Mechs until a 300 ton limit is reached, which is (1): \n")

while valid:
    if menu_choice in menu_choices:
        if menu_choice == '1':
            allottedTonnage = 100
            playerTeam = {}
            playerDesignation = 1

            while allottedTonnage > 0:

                found = False
                playerMech = 'playerMech_' + str(playerDesignation)
                print(playerMech)

                for item in mdata['mechs']:
                    print("{:12} {} tons".format(item['name'], item['mass']))

                newPlayerMech = input("\nChoose Mech: ")
                newPlayerMech = newPlayerMech.upper()
                for result in mdata['mechs']:
                    if result['name'] == newPlayerMech and result['mass'] <= allottedTonnage:
                        playerTeam[playerMech] = Mech(
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
                        wIDs = playerTeam[playerMech].getWandE()
                        # btf.printDict(wIDs)
                        newWeapons = btf.objectifyByID(wIDs,wdata)
                        # btf.printDict(newWeapons)
                        playerTeam[playerMech].setWandE(newWeapons)
                        count = 1
                        for key, value in playerTeam[playerMech].getWandE().items():
                            for item in value:
                                print("{}) {}".format(count,item.getName()))
                                count+=1

                        allottedTonnage = allottedTonnage - playerTeam[playerMech].getMass()
                        playerDesignation += 1
                        print(allottedTonnage)
                        found = True
                        # valid = False
                    else:
                        """
                            TODO: Loops to much...
                        """
                        found = True
                        print("This Mech is too big to fit into your allotted tonnage. Please try again.")
                if found is not True:
                    print("Mech not available. Please choose a Mech from the models available.")
            valid = False
        else:
            pass
    else:
        pass

print(playerTeam.items())