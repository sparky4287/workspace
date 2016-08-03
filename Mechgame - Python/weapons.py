""" Weapon Construction """
class Weapon(object):
    def __init__(self, _id, name, mass, wtype, criticals, heat, damage, ammo_mult, min_r, short_r, med_r, long_r, extreme_r):
        self._id = _id
        self.name = name
        self.mass = mass
        self.wtype = wtype
        self.criticals = criticals
        self.heat = heat
        self.damage = damage
        self.ammo_mult = ammo_mult
        self.min_r = min_r
        self.short_r = short_r
        self.med_r = med_r
        self.long_r = long_r
        self.extreme_r = extreme_r

    ### Mutators ###
    def setId(self, _id):
        self._id = _id
    def setName(self, name):
        self.name = name
    def setMass(self, mass):
        self.mass = mass
    def setWType(self, wtype):
        self.wtype = wtype
    def setCriticals(self, criticals):
        self.criticals = criticals
    def setHeat(self, heat):
        self.heat = heat
    def setDamage(self, damage):
        self.damage = damage
    def setAmmoMult(self, ammo_mult):
        self.ammo_mult = ammo_mult
    def setMinRange(self, min_r):
        self.min_r = min_r
    def setShortRange(self, short_r):
        self.short_r = short_r
    def setMedRange(self, med_r):
        self.med_r = med_r
    def setLongRange(self, long_r):
        self.long_r = long_r
    def setExtremeRange(self, extreme_r):
        self.extreme_r = extreme_r

    ### Accessors ###
    def getId(self):
        return self._id
    def getName(self):
        return self.name
    def getMass(self):
        return self.mass
    def getWType(self):
        return self.wtype
    def getCriticals(self):
        return self.criticals
    def getHeat(self):
        return self.heat
    def getDamage(self):
        return self.damage
    def getAmmoMult(self):
        return self.ammo_mult
    def getMinRange(self):
        return self.min_r
    def getShortRange(self):
        return self.short_r
    def getMedRange(self):
        return self.med_r
    def getLongRange(self):
        return self.long_r
    def getExtremeRange(self):
        return self.extreme_r

    def __str__(self):
        return "\n*******************************" + \
            "\n*        Weapon Stats         *" + \
            "\n*******************************" + \
            "\nType:\t\t" + self.getName().title() + \
            "\nMass:\t\t" + str(self.getMass()) + " tons" + \
            "\nType:\t" + str(self.getWType()) + \
            "\nCriticals:\t" + str(self.getCriticals()) + \
            "\nHeat:\t" + str(self.getHeat()) + \
            "\nDamage:\t" + str(self.getDamage()) + \
            "\nAmmo Multiplier:\t" + str(self.getAmmoMult()) + \
            "\nMinimum Range:\t" + str(self.getMinRange()) + \
            "\nShort Range:\t\t" + str(self.getShortRange()) + \
            "\nMedium Range:\t" + str(self.getMedRange()) + \
            "\nLong Range:\t" + str(self.getLongRange()) + \
            "\nExtreme Range:\t" + str(self.getExtremeRange())