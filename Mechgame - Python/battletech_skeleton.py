import effectsLib as elib

class Team:
	def __init__(self, name, members, initiative_order=0, active=True):
		self.name = name
		self.members = members
		self.initiative_order = initiative_order
		self.active = active

turn_order = {}
t1 = Team('t1', {1:'a',2:'b',3:'c',4:'d'})
t2 = Team('t2', {1:'e',2:'f',3:'g',4:'h'})
total_number_of_units = len(t1.members) + len(t2.members)

while True:
	# Turn Begin
	print("\n...BEGIN TURN...")

	# Initiative Phase
	print("\n...INITIATIVE PHASE...")

	while t1.initiative_order == t2.initiative_order:
		t1.initiative_order = elib.roll2D6()
		# print(t1.initiative_order)
		t2.initiative_order = elib.roll2D6()
		# print(t2.initiative_order)

	if t1.initiative_order < t2.initiative_order:
		turn_order = {1:t1, 2:t2}
	else:
		turn_order = {1:t2, 2:t1}

	print("Turn order:")
	print("1) {} (Rolled a {})".format(turn_order[1].name, turn_order[1].initiative_order))
	print("2) {} (Rolled a {})".format(turn_order[2].name, turn_order[2].initiative_order))

	a = tuple(turn_order[1].members.items())
	b = tuple(turn_order[2].members.items())
	unit_order = []
	count = 0

	while total_number_of_units > 0:
		unit_order.append(a[count])
		unit_order.append(b[count])
		count += 1
		total_number_of_units -= len(turn_order)

	# print(unit_order)

	# Movement Phase
	print("\n...MOVEMENT PHASE...")
	for _id, item in unit_order:
		print("{} moves!".format(item))

	# Weapon Attack Phase
	print("\n...WEAPON ATTACK PHASE...")
	for _id, item in unit_order:
		print("{} fires!".format(item))

	# Turn End
	print("\n...END TURN...")

	# Check Victory Conditions
	print("\n...CHECK VICTORY CONDITIONS...")

	break