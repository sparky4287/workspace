import pickle

data1 = {
	2:  {7:1,12:2},
	4:  {2:1,6:2,10:3,12:4},
	6:  {3:2,5:3,8:4,10:5,12:6},
	5:  {2:1,4:2,8:3,10:4,12:5},
	10: {3:3,4:4,8:6,10:8,12:10},
	15: {3:5,4:6,8:9,10:12,12:15},
	20: {3:6,4:9,8:12,10:16,12:20}
}

with open('mhTable.pickle', 'wb') as f:
	pickle.dump(data1, f, pickle.HIGHEST_PROTOCOL)

data2 = {
	30: {'mP_modifier': -5, 'toHit_modifier': 4, 'ammo_explosion_roll': 8, 'shut_down_roll': 10, 'shut_down': True},
	28: {'mP_modifier': -5, 'toHit_modifier': 4, 'ammo_explosion_roll': 8, 'shut_down_roll': 10, 'shut_down': False},
	26: {'mP_modifier': -5, 'toHit_modifier': 4, 'ammo_explosion_roll': 6, 'shut_down_roll': 10, 'shut_down': False},
	25: {'mP_modifier': -5, 'toHit_modifier': 4, 'ammo_explosion_roll': 6, 'shut_down_roll': 8, 'shut_down': False},
	24: {'mP_modifier': -4, 'toHit_modifier': 4, 'ammo_explosion_roll': 6, 'shut_down_roll': 8, 'shut_down': False},
	23: {'mP_modifier': -4, 'toHit_modifier': 3, 'ammo_explosion_roll': 6, 'shut_down_roll': 8, 'shut_down': False},
	20: {'mP_modifier': -4, 'toHit_modifier': 3, 'ammo_explosion_roll': 4, 'shut_down_roll': 6, 'shut_down': False},
	19: {'mP_modifier': -3, 'toHit_modifier': 3, 'ammo_explosion_roll': 4, 'shut_down_roll': 6, 'shut_down': False},
	18: {'mP_modifier': -3, 'toHit_modifier': 3, 'ammo_explosion_roll': None, 'shut_down_roll': 6, 'shut_down': False},
	17: {'mP_modifier': -3, 'toHit_modifier': 3, 'ammo_explosion_roll': None, 'shut_down_roll': 4, 'shut_down': False},
	15: {'mP_modifier': -3, 'toHit_modifier': 2, 'ammo_explosion_roll': None, 'shut_down_roll': 4, 'shut_down': False},
	14: {'mP_modifier': -2, 'toHit_modifier': 2, 'ammo_explosion_roll': None, 'shut_down_roll': 4, 'shut_down': False},
	13: {'mP_modifier': -2, 'toHit_modifier': 2, 'ammo_explosion_roll': None, 'shut_down_roll': None, 'shut_down': False},
	10: {'mP_modifier': -2, 'toHit_modifier': 1, 'ammo_explosion_roll': None, 'shut_down_roll': None, 'shut_down': False},
	8:  {'mP_modifier': -1, 'toHit_modifier': 1, 'ammo_explosion_roll': None, 'shut_down_roll': None, 'shut_down': False},
	5:  {'mP_modifier': -1, 'toHit_modifier': 0, 'ammo_explosion_roll': None, 'shut_down_roll': None, 'shut_down': False}
}

with open('heTable.pickle', 'wb') as f:
	pickle.dump(data2, f, pickle.HIGHEST_PROTOCOL)
	
with open('mhTable.pickle', 'rb') as f:
	data1 = pickle.load(f)
	
with open('heTable.pickle', 'rb') as f:
	data2 = pickle.load(f)
	
print(data1)
print(data2)