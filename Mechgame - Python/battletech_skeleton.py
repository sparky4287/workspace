import effectsLib as elib
import team_create as tc
import pprint

pp = pprint.PrettyPrinter()
turn_order = {}

# Team Creation
print("\n...CREATE TEAM 1...")
t1 = tc.create_team('t1',8)

# pp.pprint(t1)
# pp.pprint(t1.members)
# pp.pprint(t1.members[1]['pilot'])
# pp.pprint(t1.members[1]['mech'])

print("\n...CREATE TEAM 2...")
t2 = tc.create_team('t2',8)

total_number_of_units = len(t1.members) + len(t2.members)

while True:
	# Turn Begin
	print("\n...BEGIN TURN...")

	# Initiative Phase
	print("\n...INITIATIVE PHASE...")

	while t1.initiative_order == t2.initiative_order:
		t1.initiative_order = elib.roll2D6()
		t2.initiative_order = elib.roll2D6()

	if t1.initiative_order < t2.initiative_order:
		turn_order = {1:t1, 2:t2}
	else:
		turn_order = {1:t2, 2:t1}

	print("Turn order:")
	print("1) {} (Rolled a {})".format(turn_order[1].name, turn_order[1].initiative_order))
	print("2) {} (Rolled a {})".format(turn_order[2].name, turn_order[2].initiative_order))

	turn_active = turn_order[1]

	# Movement Phase
	print("\n...MOVEMENT PHASE...")

	total_number_of_units = len(t1.members) + len(t2.members)

	keep_active = 0
	while total_number_of_units > 0:
		print("{}'s move turn!".format(turn_active.name))
		print("Choose unit to move:")
		for key, item in turn_active.members.items():
			if item['active'] == True:
				print("{}) {} ({}) - {}".format(key, item['mech'].name, item['pilot'].name, item['active']))
		move_choice = input()
		print("{}'s {} moves!".format(turn_active.members[int(move_choice)]['pilot'].name, turn_active.members[int(move_choice)]['mech'].name))
		turn_active.members[int(move_choice)]['active'] = False
		total_number_of_units -= 1

		# Active unit check
		for k, v in turn_active.members.items():
			if v['active'] == True:
				keep_active += 1
		if keep_active == 0:
			turn_active.active = False
		keep_active = 0

		if turn_active == turn_order[1]:
			print(turn_order[2].active)
			if turn_order[2].active is not False:
				turn_active = turn_order[2]
		else:
			print(turn_order[1].active)
			if turn_order[1].active is not False:
				turn_active = turn_order[1]

	# Weapon Attack Phase
	print("\n...WEAPON ATTACK PHASE...")

	total_number_of_units = len(t1.members) + len(t2.members)
	pp.pprint(t1)
	pp.pprint(t2)

	t1.active = True
	t2.active = True
	for k,v in t1.members.items():
		v['active'] = True
	for k,v in t2.members.items():
		v['active'] = True

	while total_number_of_units > 0:
		print("{}'s weapon fire turn!".format(turn_active.name))
		print("Choose unit to fire weapons:")
		for key, item in turn_active.members.items():
			if item['active'] == True:
				print("{}) {} ({}) - {}".format(key, item['mech'].name, item['pilot'].name, item['active']))
		move_choice = input()
		print("{}'s {} fires!".format(turn_active.members[int(move_choice)]['pilot'].name, turn_active.members[int(move_choice)]['mech'].name))
		turn_active.members[int(move_choice)]['active'] = False
		total_number_of_units -= 1

		# Active unit check
		for k, v in turn_active.members.items():
			if v['active'] == True:
				keep_active += 1
		if keep_active == 0:
			turn_active.active = False
		keep_active = 0

		if turn_active == turn_order[1]:
			print(turn_order[2].active)
			if turn_order[2].active is not False:
				turn_active = turn_order[2]
		else:
			print(turn_order[1].active)
			if turn_order[1].active is not False:
				turn_active = turn_order[1]

	# Turn End
	print("\n...END TURN...")

	# Check Victory Conditions
	print("\n...CHECK VICTORY CONDITIONS...")

	break