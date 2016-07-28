""" Mech Construction """
class Mech(object):
    def __init__(self, _id, name, mass, endo_steel, power_plant, xl, walking_speed, running_speed, jump_jets, jump_distance, ferro_fibrous, armor_mass, armor_factor, heat_sinks, dbl_heat_sinks):
        self._id = _id
        self.name = name
        self.mass = mass
        self.endo_steel = endo_steel
        self.power_plant = power_plant
        self.xl = xl
        self.walking_speed = walking_speed
        self.running_speed = running_speed
        self.jump_jets = jump_jets
        self.jump_distance = jump_distance
        self.ferro_fibrous = ferro_fibrous
        self.armor_mass = armor_mass
        self.armor_factor = armor_factor
        self.heat_sinks = heat_sinks
        self.dbl_heat_sinks = dbl_heat_sinks

    def getName(self):
        return self.name

    def __str__(self):
        return "%s is %d tons" % (self.name, self.mass)