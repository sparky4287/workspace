""" Mech Construction """
class Mech(object):
    def __init__(self, name, mass, endo_steel, power_plant, xl, walking_speed, running_speed, jump_jets, jump_distance, ferro_fibrous, armor_mass, armor_factor, heat_sinks, dbl_heat_sinks):
        self.name = name
        self.mass = mass
        self.chassis = chassis
        self.power_plant = power_plant
        self.walking_speed = walking_speed
        self.running_speed = running_speed
        self.jump_jets = jump_jets
        self.jump_distance = jump_distance
        self.armor_type = armor_type
        self.armor_mass = armor_mass
        self.armor_factor = armor_factor
        self.heat_sinks = heat_sinks

""" Light Mech Code Construction """
flea = Mech("Flea", 20, True, 120, False, 6, 9, 0, 0, False, 3, 48, 10, False)

hornet = Mech("Hornet", 20, True, 100, False, 5, 8, )

raptor_prime = Mech("Raptor Prime", 25, True, 175, True, 7, 11, 0, 0, False, 3.5, 56, 10, True)
raptor_a = Mech("Raptor A", 25, True, 175, True, 7, 11, 0, 0, False, 3.5, 56, 10, True)
raptor_b = Mech("Raptor B", 25, True, 175, True, 7, 11, 0, 0, False, 3.5, 56, 10, True)
raptor_c = Mech("Raptor C", 25, True, 175, True, 7, 11, 0, 0, False, 3.5, 56, 10, True)
raptor_d = Mech("Raptor D", 25, True, 175, True, 7, 11, 0, 0, False, 3.5, 56, 10, True)

owens_prime = Mech("Owens Prime", 35, False, 280, True, 8, 12, 0, 0, False, 7, 112, 10, False)
owens_a = Mech("Owens A", 35, False, 280, True, 8, 12, 0, 0, False, 7, 112, 10, False)
owens_b = Mech("Owens B", 35, False, 280, True, 8, 12, 0, 0, False, 7, 112, 10, False)
owens_c = Mech("Owens C", 35, False, 280, True, 8, 12, 0, 0, False, 7, 112, 10, False)
owens_d = Mech("Owens D", 35, False, 280, True, 8, 12, 0, 0, False, 7, 112, 10, False)

""" Medium Mech Code Construction """
strider_prime = Mech("Strider Prime", 40, True, 240, False, 6, 9, 0, 0, False, 7.5, 120, 10, False)
strider_a = Mech("Strider A", 40, True, 240, False, 6, 9, 0, 0, False, 7.5, 120, 10, False)
strider_b = Mech("Strider B", 40, True, 240, False, 6, 9, 0, 0, False, 7.5, 120, 10, False)
strider_c = Mech("Strider C", 40, True, 240, False, 6, 9, 0, 0, False, 7.5, 120, 10, False)
strider_d = Mech("Strider D", 40, True, 240, False, 6, 9, 0, 0, False, 7.5, 120, 10, False)

""" Heavy Mech Code Construction """

""" Assault Mech Code Construction """


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