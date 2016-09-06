import effectsLib as elib
import team_create as tc
import pprint

pp = pprint.PrettyPrinter()
turn_order = {}

# Team Creation
print("\n...CREATE TEAM 1...")
t1 = tc.create_team('t1',8)

pp.pprint(t1)
pp.pprint(t1.members)
pp.pprint(t1.members[1]['pilot'])
pp.pprint(t1.members[1]['mech'])

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

	a = turn_order[1].members
	b = turn_order[2].members

	unit_order = []
	count = 0

	while total_number_of_units > 0:
		decrement = 0
		try:
			if a[count]:
				unit_order.append(a[count])
				decrement += 1
		except IndexError:
			print("A end of list")
		try:
			if b[count]:
				unit_order.append(b[count])
				decrement += 1
		except IndexError:
			print("B end of list")
		count += 1
		total_number_of_units -= decrement

	# Movement Phase
	print("\n...MOVEMENT PHASE...")
	for item in unit_order:
		print("{} moves!".format(item.name))

	# Weapon Attack Phase
	print("\n...WEAPON ATTACK PHASE...")
	for item in unit_order:
		print("{} fires!".format(item.name))

	# Turn End
	print("\n...END TURN...")

	# Check Victory Conditions
	print("\n...CHECK VICTORY CONDITIONS...")

	break