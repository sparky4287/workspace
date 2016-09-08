class Team:
	def __init__(self,name,members,initiative_order=0,active=True):
		self.name = name
		self.members = members
		self.initiative_order = initiative_order
		self.active = active

	### Accessors ###
	def getName(self):
		return self.name
	def getMembers(self):
		return self.members
	def getInitOrder(self):
		return self.initiative_order
	def getActive(self):
		return self.active

	def __repr__(self):
		return "\nTeam Name:\t\t" + self.getName().title() + \
			"\nInit Order:\t\t" + str(self.getInitOrder()) + \
			"\nActive:\t\t" + str(self.getActive())