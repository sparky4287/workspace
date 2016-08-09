import simplejson as json
from mechs import Mech
from weapons import Weapon

mech_file_dir = "mechdata.json"
wande_file_dir = "weapons.json"
valid = True
found = False
count = 0
weapons = [8,8,15]

with open(mech_file_dir) as mech_file:
	mdata = json.load(mech_file)
with open(wande_file_dir) as wande_file:
	wdata = json.load(wande_file)

while count < len(weapons):
	# for item in wdata['weapons']:
	# 	print("{}.\t{}".format(item['_id'],item['name'].upper()))
	# choice = input("\nChoose weapon:")
	# print(choice)
	for result in wdata['weapons']:
		if result['_id'] == weapons[count]:
			weapons.append(Weapon(
                result['_id'],
                result['name'],
                result['mass'],
                result['wtype'],
                result['criticals'],
                result['heat'],
                result['damage'],
                result['ammo_mult'],
                result['min_r'],
                result['short_r'],
                result['med_r'],
                result['long_r'],
                result['extreme_r']))
			# weapons.remove(weapons[count])
	count = count + 1

for item in weapons:
	print(item)
