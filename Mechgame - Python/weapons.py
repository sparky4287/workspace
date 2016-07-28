""" Weapon Construction """
class Weapon(object):
    def __init__(self, name, wtype, criticals, mass, heat, damage, min_range, short_range, med_range, long_range):
        self.name = name
        self.wtype = wtype              """1=ballistic, 2=missile, 3=energy"""
        self.criticals = criticals
        self.mass = mass
        self.heat = heat
        self.damage = damage
        self.min_range = min_range
        self.short_range = short_range
        self.med_range = med_range
        self.long_range = long_range

""" Ballistic Weapon Code Construction """
machine_gun = Weapon("Machine Gun",1,1,)
ac_2 = Weapon("Autocannon-2",1)
ac_5 = Weapon("Autocannon-5",1)
ac_10 = Weapon("Autocannon-10",1)
ac_20 = Weapon("Autocannon-20",1)

""" Missile Weapon Code Construction """
srm_2 = Weapon("SRM 2",2)
srm_4 = Weapon("SRM 4",2)
srm_6 = Weapon("SRM 6",2)
lrm_5 = Weapon("LRM 5",2)
lrm_10 = Weapon("LRM 10",2)
lrm_15 = Weapon("LRM 15",2)
lrm_20 = Weapon("LRM 20",2)

""" Energy Weapon Code Construction """
flamer = Weapon("Flamer",3,1,)
sm_laser = Weapon("Small Laser",3,1,.5,)
md_laser = Weapon("Medium Laser",3,1,1,)
lg_laser = Weapon("Large Laser",3,2,5,)
ppc = Weapon("PPC",3,3,7,10,10,)