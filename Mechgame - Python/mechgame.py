import simplejson as json
from mechs import Mech

def displayMech(Mech):
    print ("\n*******************************")
    print ("***       Mech Stats        ***")
    print ("*******************************")
    print("Type:\t\t%s %s" % (playerMech.getModel(), playerMech.getName().title()))
    print("Mass:\t\t%d" % playerMech.getMass())
    # Can be refactored?
    if playerMech.getEndoSteel() == True:
        print("Chassis:\tEndo Steel")
    else:
        print("Chassis:\tStandard")
    # Can be refactored?
    if playerMech.getXL() == True:
        print("Power Plant:\t%d (XL)" % playerMech.getPowerPlant())
    else:
        print("Power Plant:\t%d (Standard)" % playerMech.getPowerPlant())
    print("Walking Speed:\t%d" % playerMech.getWalkingSpeed())
    print("Running Speed:\t%d" % playerMech.getRunningSpeed())
    print("Jump Jets:\t%d" % playerMech.getJumpJets())
    print("Jump Distance:\t%d" % playerMech.getJumpDistance())
    # Can be refactored?
    if playerMech.getFerroFibrous() == True:
        print("Armor:\t\tFerro Fibrous")
    else:
        print("Armor:\t\tStandard")
    print("Armor Mass:\t%.1f tons" % playerMech.getArmorMass())
    print("Armor Factor:\t%d" % playerMech.getArmorFactor())
    # Can be refactored?
    if playerMech.getDblHeatSinks() == True:
        print("Heat Sinks:\t%d(%d)" % (playerMech.getHeatSinks(), playerMech.getHeatSinks()*2))
    else:
        print("Heat Sinks:\t%d" % playerMech.getHeatSinks())

file_dir = "mechdata.json"
valid = True
found = False

with open(file_dir) as data_file:
    data = json.load(data_file)

for item in data['mechs']:
    print(item['name'].title())

while valid:
    newPlayerMech = input("\nChoose Mech: ")
    newPlayerMech = newPlayerMech.lower()
    for result in data['mechs']:
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
                result['dbl_heat_sinks'])
            print("\n...Mech construction successful...")
            print(playerMech)
            found = True
            valid = False
    if found is not True:
        print("Mech not available. Please choose a Mech from the models available.")
