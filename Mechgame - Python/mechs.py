""" Mech Construction """
class Mech(object):
    def __init__(self, _id, model, name, mass, endo_steel, power_plant, xl, walking_speed, running_speed, jump_jets, jump_distance, ferro_fibrous, armor_mass, armor_factor, heat_sinks, dbl_heat_sinks):
        self._id = _id
        self.model = model
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

    ### Mutators ###
    def setId(self, _id):
        self._id = _id
    def setModel(self, model):
        self.model = model
    def setName(self, name):
        self.name = name
    def setMass(self, mass):
        self.mass = mass
    def setEndoSteel(self, endo_steel):
        self.endo_steel = endo_steel
    def setPowerPlant(self, power_plant):
        self.power_plant = power_plant
    def setXL(self, xl):
        self.xl = xl
    def setWalkingSpeed(self, walking_speed):
        self.walking_speed = walking_speed
    def setRunningSpeed(self, running_speed):
        self.running_speed = running_speed
    def setJumpJets(self, jump_jets):
        self.jump_jets = jump_jets
    def setJumpDistance(self, jump_distance):
        self.jump_distance = jump_distance
    def setFerroFibrous(self, ferro_fibrous):
        self.ferro_fibrous = ferro_fibrous
    def setArmorMass(self, armor_mass):
        self.armor_mass = armor_mass
    def setArmorFactor(self, armor_factor):
        self.armor_factor = armor_factor
    def setHeatSinks(self, heat_sinks):
        self.heat_sinks = heat_sinks
    def setDblHeatSinks(self, dbl_heat_sinks):
        self.dbl_heat_sinks = dbl_heat_sinks

    ### Accessors ###
    def getId(self):
        return self._id
    def getModel(self):
        return self.model
    def getName(self):
        return self.name
    def getMass(self):
        return self.mass
    def getEndoSteel(self):
        return self.endo_steel
    def getPowerPlant(self):
        return self.power_plant
    def getXL(self):
        return self.xl
    def getWalkingSpeed(self):
        return self.walking_speed
    def getRunningSpeed(self):
        return self.running_speed
    def getJumpJets(self):
        return self.jump_jets
    def getJumpDistance(self):
        return self.jump_distance
    def getFerroFibrous(self):
        return self.ferro_fibrous
    def getArmorMass(self):
        return self.armor_mass
    def getArmorFactor(self):
        return self.armor_factor
    def getHeatSinks(self):
        return self.heat_sinks
    def getDblHeatSinks(self):
        return self.dbl_heat_sinks

    def __str__(self):

        # Grab values through tuple implementation
        ferro_fibrous = ("Standard", "Ferro Fibrous")[self.getFerroFibrous()]
        chassis = ("Standard", "Endo Steel")[self.getEndoSteel()]
        power_plant = ("Standard", "XL")[self.getXL()]
        heat_sinks = (str(self.getHeatSinks()), str(self.getHeatSinks()) + "(" + str(self.getHeatSinks()*2) + ")")[self.getDblHeatSinks()]

        return "\n*******************************" + \
            "\n*         Mech Stats          *" + \
            "\n*******************************" + \
            "\nType:\t\t" + self.getModel() + " " + self.getName().title() + \
            "\nMass:\t\t" + str(self.getMass()) + " tons" + \
            "\nChassis:\t" + ferro_fibrous + \
            "\nPower Plant:\t" + str(self.getPowerPlant()) + " " + power_plant + \
            "\nWalking Speed:\t" + str(self.getWalkingSpeed()) + \
            "\nRunning Speed:\t" + str(self.getRunningSpeed()) + \
            "\nJump Distance:\t" + str(self.getJumpDistance()) + \
            "\nArmor:\t\t" + str(self.getArmorFactor()) + " " + ferro_fibrous + \
            "\nArmor Mass:\t" + str(self.getArmorMass()) + " tons" + \
            "\nHeat Sinks:\t" + heat_sinks