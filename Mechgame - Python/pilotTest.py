import pickle as p

data = {
	'pilots': {
		1: {
			'id': 1,
			'name': 'Tykus Raines',
			'rank': 4,
			'pSkill': 1,
			'gSkill': 2,
			'description': 'After honorably serving in the reknowned Davion Heavy Guard as a Lieutenant First Class for 3 years, Tykus resigned his commission after a skirmish left him with a damaged left cornea.'
		},
		2: {
			'id': 2,
			'name': 'Melitus Foyd',
			'rank': 4,
			'pSkill': 2,
			'gSkill': 1,
			'description': ''
		},
		3: {
			'id': 3,
			'name': 'Cailan Derrikson',
			'rank': 3,
			'pSkill': 2,
			'gSkill': 2,
			'description': ''
		},
		4: {
			'id': 4,
			'name': 'Darius Price',
			'rank': 3,
			'pSkill': 2,
			'gSkill': 2,
			'description': ''
		},
		5: {
			'id': 5,
			'name': 'Akari Tagawa',
			'rank': 2,
			'pSkill': 2,
			'gSkill': 3,
			'description': ''
		},
		6: {
			'id': 6,
			'name': 'Teke Sun-Liang',
			'rank': 2,
			'pSkill': 3,
			'gSkill': 2,
			'description': ''
		},
		7: {
			'id': 7,
			'name': 'Wilhelm Von Richter',
			'rank': 1,
			'pSkill': 3,
			'gSkill': 3,
			'description': ''
		},
		8: {
			'id': 8,
			'name': 'Elemy Holt',
			'rank': 1,
			'pSkill': 3,
			'gSkill': 3,
			'description': ''
		}
	},
	'ranks': {
		1: 'Rookie',
		2: 'Regular',
		3: 'Veteran',
		4: 'Elite'
	}
}

with open('pilots.pickle', 'wb') as w:
	p.dump(data, w, p.HIGHEST_PROTOCOL)
	
# with open('pilots.pickle', 'rb') as r:
# 	p_data = p.load(r)

# pilot_data	= p_data['pilots']
# ranks 		= p_data['ranks']
		
# pilot_list = []
# limit = 8
# while limit > 0:
# 	for key, value in pilot_data.items():
# 		print("{})".format(key))
# 		print("Name:     {} ({})".format(value['name'], ranks[value['rank']]))
# 		print("Piloting: {}".format(value['pSkill']))
# 		print("Gunnery:  {}".format(value['gSkill']))
# 	pilot_choice = int(input("Choose pilot: "))
# 	pilot_list.append(pilot_data[pilot_choice])
# 	limit -= pilot_data[pilot_choice]['rank']
# 	del pilot_data[pilot_choice]
# 	for key, value in list(pilot_data.items()):
# 		if value['rank'] > limit:
# 			del pilot_data[key]
# 	print(pilot_list)
# 	print(pilot_data)