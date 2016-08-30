import random as r
import pickle as p

def roll1D6():
	return r.randrange(6)+1


def roll2D6():
	return r.randrange(12)+1
	
def numMH(num, roll=roll2D6()):

	with open('mhTable.pickle', 'rb') as data_file:
		options = p.load(data_file)
	
	if num in options:
		keys = sorted(options[num])
		print("Roll:  {}".format(roll))
		for item in keys:
			if roll <= item:
				return options[num][item]
	else:
		print("Invalid number. Please try again.")
		
def heMod(he):

	with open('heTable.pickle', 'rb') as data_file:
		options = p.load(data_file)
	
	heModList = []
	keys = sorted(options)
	print(keys)
	
	for item in keys:
		if he >= item:
			heModList.append(options[item])
	print("Heat Effect Modifiers:")
	
	# print(heModList)
	
	for item in heModList:
		print("{}".format(item))