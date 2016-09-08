import simplejson as json
import teams
import pilots
import mech_create

def create_team(tname,limit):
	with open('pilots.json', 'rb') as r:
		data = json.load(r)

	pdata = data['pilots']
	ranks = data['ranks']

	keys = pdata.keys()
	sorted_keys = sorted(keys)
	member_dict = {}
	count = 0

	while limit > 0:
		count += 1
		for item in sorted_keys:
			p_item = pdata[item]
			print("{})".format(item))
			print("Name:        {} ({})".format(p_item['name'], ranks[str(p_item['rank'])]))
			print("Piloting:    {}".format(p_item['pSkill']))
			print("Gunnery:     {}".format(p_item['gSkill']))
			print("Description: {}".format(p_item['description']))
		pilot_choice = input("Choose pilot: ")
		pilot = pilots.Pilot(
			pdata[pilot_choice]['name'],
			pdata[pilot_choice]['rank'],
			pdata[pilot_choice]['pSkill'],
			pdata[pilot_choice]['gSkill'],
			pdata[pilot_choice]['description']
		)
		mech = mech_create.create_mech()
		member_dict.update({count: {'pilot': pilot, 'mech': mech, 'active': True}})
		# member_list.append(pilot)
		# print(member_dict)
		limit -= pilot.rank
		del pdata[pilot_choice]
		sorted_keys.remove(pilot_choice)
		for key, value in list(pdata.items()):
			if value['rank'] > limit:
				del pdata[key]
				sorted_keys.remove(key)

	team = teams.Team(tname, member_dict)
	return team
