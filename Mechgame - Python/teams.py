class Team:
	def __init__(self,name,members,initiative_order=0,active=True):
		self.name = name
		self.members = members
		self.initiative_order = initiative_order
		self.active = active