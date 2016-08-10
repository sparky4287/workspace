from weapons import Weapon

def objectifyByID(dictionary, data):
	for key,val in dictionary.items():
		for item in val:
			for result in data['weapons']:
				if result['_id'] == item:
					dictionary[key].append(
						Weapon(
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
		tempLen = int(len(val)/2)
		val.reverse()
		while tempLen < len(val):
			val.pop()
	return dictionary
	
def printDict(dictionary):
	for key,val in dictionary.items():
		print(key,val)