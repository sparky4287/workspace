import simplejson as json

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

with open('pilots.json', 'wb') as pilots_file:
    json.dump(data, pilots_file)