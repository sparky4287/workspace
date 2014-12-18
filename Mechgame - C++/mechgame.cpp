#include <iostream>
#include <string>
#include <istream>
#include <iomanip>
#include <math.h>
using namespace std;

const int SIZE = 50;

/* Esablishing Weapon Class (until file stream is learned) */
class Weapon
{
   	public:
   		string name,weapon_type;
   		int critical_spaces,range_short,range_medium,range_long,damage,ammo_per_ton;
   		float weight,heat;
};

/* Establishing initial Mech Class (until file stream is learned) */
class Mech
{
	public:
		string name,weapons[20];
		int walking_mp,running_mp,jumping_mp,armor_points,hd_armor,ct_armor,rt_armor,
			lt_armor,ra_armor,la_armor,rl_armor,ll_armor,rear_ct_armor,rear_rt_armor,
			rear_lt_armor;
		float remaining_tonnage;
};

/* Initial Menu */
int menu() {
	int choice;
	bool menu_valid = false;
	while(menu_valid == false) {
		cout << "|---------------------------------|" << endl;
		cout << "| Welcome to Mechwarrior Tactical |" << endl;
		cout << "| ------------------------------- |" << endl;
		cout << "| Choose an option:               |" << endl;
		cout << "| -----------------               |" << endl;
		cout << "| (1) New Campaign                |" << endl;
		cout << "| (2) Continue                    |" << endl;
		cout << "| (3) Mech Bay                    |" << endl;
		cout << "| (4) Exit                        |" << endl;
		cout << "|---------------------------------|" << endl;
		cin >> choice;
		switch (choice) {
			case 1:
			case 2:
			case 3:
			case 4:
				menu_valid = true;
				break;
			default:
				cout << "Error. Try again." << endl;
		}
	}
	return choice;
}

/* Find Engine Rating by Desired Walking MP */
int find_engine_rating(int tonnage) {
	int engine_rating,desired_mp;

	cout << "What is your desired walking MP? ";
	cin >> desired_mp;
	engine_rating = tonnage * desired_mp;
	return engine_rating;
}

/* Find Engine Weight by Engine Rating */
float find_engine_weight(int engine_rating) {
	float engine_weight;

	switch(engine_rating) {
		case 10:
		case 15:
		case 20:
		case 25:
			engine_weight = 0.5;
			break;
		case 30:
		case 35:
		case 40:
		case 45:
			engine_weight = 1.0;
			break;
		case 50:
		case 55:
		case 60:
			engine_weight = 1.5;
			break;
		case 65:
		case 70:
		case 75:
			engine_weight = 2.0;
			break;
		case 80:
		case 85:
			engine_weight = 2.5;
			break;
		case 90:
		case 95:
		case 100:
			engine_weight = 3.0;
			break;
		case 105:
		case 110:
			engine_weight = 3.5;
			break;
		case 115:
		case 120:
		case 125:
			engine_weight = 4.0;
			break;
		case 130:
		case 135:
			engine_weight = 4.5;
			break;
		case 140:
		case 145:
			engine_weight = 5.0;
			break;
		case 150:
		case 155:
			engine_weight = 5.5;
			break;
		case 160:
		case 165:
			engine_weight = 6.0;
			break;
		case 170:
			engine_weight = 6.5;
			break;
		case 175:
		case 180:
			engine_weight = 7.0;
			break;
		case 185:
		case 190:
			engine_weight = 7.5;
			break;
		case 195:
			engine_weight = 8.0;
			break;
		case 200:
		case 205:
			engine_weight = 8.5;
			break;
		case 210:
			engine_weight = 9.0;
			break;
		case 215:
			engine_weight = 9.5;
			break;
		case 220:
		case 225:
			engine_weight = 10.0;
			break;
		case 230:
			engine_weight = 10.5;
			break;
		case 235:
			engine_weight = 11.0;
			break;
		case 240:
			engine_weight = 11.5;
			break;
		case 245:
			engine_weight = 12.0;
			break;
		case 250:
			engine_weight = 12.5;
			break;
		case 255:
			engine_weight = 13.0;
			break;
		case 260:
			engine_weight = 13.5;
			break;
		case 265:
			engine_weight = 14.0;
			break;
		case 270:
			engine_weight = 14.5;
			break;
		case 275:
			engine_weight = 15.5;
			break;
		case 280:
			engine_weight = 16.0;
			break;
		case 285:
			engine_weight = 16.5;
			break;
		case 290:
			engine_weight = 17.5;
			break;
		case 295:
			engine_weight = 18.0;
			break;
		case 300:
			engine_weight = 19.0;
			break;
		case 305:
			engine_weight = 19.5;
			break;
		case 310:
			engine_weight = 20.5;
			break;
		case 315:
			engine_weight = 21.5;
			break;
		case 320:
			engine_weight = 22.5;
			break;
		case 325:
			engine_weight = 23.5;
			break;
		case 330:
			engine_weight = 24.5;
			break;
		case 335:
			engine_weight = 25.5;
			break;
		case 340:
			engine_weight = 27.0;
			break;
		case 345:
			engine_weight = 28.5;
			break;
		case 350:
			engine_weight = 29.5;
			break;
		case 355:
			engine_weight = 31.5;
			break;
		case 360:
			engine_weight = 33.0;
			break;
		case 365:
			engine_weight = 34.5;
			break;
		case 370:
			engine_weight = 37.0;
			break;
		case 375:
			engine_weight = 38.5;
			break;
		case 380:
			engine_weight = 41.0;
			break;
		case 385:
			engine_weight = 43.5;
			break;
		case 390:
			engine_weight = 46.0;
			break;
		case 395:
			engine_weight = 49.0;
			break;
		case 400:
			engine_weight = 52.5;
			break;
		default:
			cout << "Human error. Please recalculate." << endl;
	}
	return engine_weight;
}

/* Find If User Desires Jump Jets by Jump MP */
int find_jump_jets(int tonnage, int engine_rating) {
	int jump_jets,desired_mp=engine_rating/tonnage,valid=0;

	while(jump_jets>-1||jump_jets<(desired_mp+1)) {
		cout << "What is your desired jumping MP (cannot exceed " << desired_mp << ")? ";
		cin >> jump_jets;
		if(jump_jets < 0 || jump_jets > desired_mp) {
			cout << "Error. Please input a valid jumping MP or zero (0)." << endl;
		}
		else
			return jump_jets;
	}
}

/* Find Jump Jet Weight by Tonnage Range and Number of Jump Jets */
float find_jump_jet_weight(int tonnage,int jump_jet_number) {
	float total_jump_jet_weight=0.0,jump_jet_weight=0.0;

	if(tonnage <= 55) {
		jump_jet_weight=0.5;
	} else if (tonnage <= 85) {
		jump_jet_weight=1.0;
	} else if(tonnage <= 100) {
		jump_jet_weight=2.0;
	} else
		jump_jet_weight=0.0;
	total_jump_jet_weight = jump_jet_weight*(float)jump_jet_number;
	return total_jump_jet_weight;
}

/* Find If User Desires an XL Engine */
int find_xl_engine() {
	int xl_engine;
	cout << "Do you desire an XL engine (XL engines are half the weight, but requires much more internal room) (1=yes, 2=no)? " << endl;
	cin >> xl_engine;
	return xl_engine;
}

/* Find If User Desires Endo Steel Chassis */
int find_endo_steel() {
	int endo_steel;
	cout << "Do you desire an endo steel chassis (Endo steel chassis are half the weight, but requires much more internal room) (1=yes, 2=no)? " << endl;
	cin >> endo_steel;
	return endo_steel;
}

/* Find Gyro Weight by Engine Rating */
float find_gyro_weight(int engine_rating) {
	int gyro_weight;

	if(engine_rating <= 100) {
		gyro_weight = 1;
	} else if(engine_rating >= 105 && engine_rating <= 200) {
		gyro_weight = 2;
	} else if(engine_rating >= 205 && engine_rating <= 300) {
		gyro_weight = 3;
	} else
		gyro_weight = 4;
	return gyro_weight;
}

/* Find Armor Weight by Tonnage */
float find_armor_weight(int tonnage) {
	float armor_weight,max_armor;

	switch(tonnage) {
		case 20:
			max_armor = 4.5;
			break;
		case 25:
			max_armor = 6;
			break;
		case 30:
			max_armor = 7;
			break;
		case 35:
			max_armor = 7.5;
			break;
		case 40:
			max_armor = 9;
			break;
		case 45:
			max_armor = 10;
			break;
		case 50:
			max_armor = 11;
			break;
		case 55:
			max_armor = 12;
			break;
		case 60:
			max_armor = 13;
			break;
		case 65:
			max_armor = 13.5;
			break;
		case 70:
			max_armor = 14;
			break;
		case 75:
			max_armor = 14.5;
			break;
		case 80:
			max_armor = 15.5;
			break;
		case 85:
			max_armor = 16.5;
			break;
		case 90:
			max_armor = 17.5;
			break;
		case 95:
			max_armor = 18.5;
			break;
		case 100:
			max_armor = 19.5;
			break;
		default:
			cout << "Error. Armor not able to be computed." << endl;
	}
	cout << "How many tons of armor do you need (up to " << max_armor << " tons and in .5 increments)? ";
	cin >> armor_weight;
	return armor_weight;
}

int armor_point_calculator(float armor_weight,int max_armor_points) {
	int armor_points;

	if(armor_weight*16 > max_armor_points) {
		armor_points = max_armor_points;
	} else {
		armor_points = armor_weight*16;
	}
	return armor_points;
}

/* Find Armor Points by Tonnage and Armor Weight */
int find_armor_points(int tonnage,float armor_weight) {
	int armor_points,max_armor_points;

	switch(tonnage) {
		case 20:
			max_armor_points = 69;
			break;
		case 25:
			max_armor_points = 89;
			break;
		case 30:
			max_armor_points = 105;
			break;
		case 35:
			max_armor_points = 119;
			break;
		case 40:
			max_armor_points = 137;
			break;
		case 45:
			max_armor_points = 153;
			break;
		case 50:
			max_armor_points = 169;
			break;
		case 55:
			max_armor_points = 185;
			break;
		case 60:
			max_armor_points = 201;
			break;
		case 65:
			max_armor_points = 211;
			break;
		case 70:
			max_armor_points = 217;
			break;
		case 75:
			max_armor_points = 231;
			break;
		case 80:
			max_armor_points = 247;
			break;
		case 85:
			max_armor_points = 263;
			break;
		case 90:
			max_armor_points = 279;
			break;
		case 95:
			max_armor_points = 293;
			break;
		case 100:
			max_armor_points = 307;
			break;
		default:
			cout << "Error. Armor points not able to be computed." << endl;
	}
	armor_points = armor_point_calculator(armor_weight,max_armor_points);
	return armor_points;
}

/* Display All Current Stats for Mech being Created */
void mech_stats(string mechClass,string mechName,float cockpit,float internal_structure,float engine_rating,
	float engine_weight,float gyro_weight,float remaining_tonnage,int heat_sink_total,float heat_sink_weight,
	float armor_weight,int armor_points,int xl_engine,int endo_steel,int jump_jet_number,float jump_jet_weight) {
	cout << endl << "You are in the process of creating a new " << mechClass << " Mech called a " << mechName << "." << endl;
	cout << endl << "The " << mechName << " has the following specs so far:" << endl;
	cout << "----------------------------------------------------------------------------" << endl;
	cout << " Name                      Type/Number              Critical Space  Tonnage" << endl;
	cout << "----------------------------------------------------------------------------" << endl;
	cout << " Cockpit:" << setw(66) << fixed << setprecision(2)<< cockpit << endl;
	cout << " Internal Structure:        ";
	if(endo_steel==1) {
		cout << "Endo Steel" << setw(37) << internal_structure << endl;
	}
	else
		cout << " Standard" << setw(38) << internal_structure << endl;
	cout << " Heat Sinks:" << setw(21)<< heat_sink_total << setw(42) << heat_sink_weight << endl;
	cout << " Engine:" << setw(24) << (int)engine_rating;
	if(xl_engine==1) {
		cout << " XL" << setw(40) << engine_weight << endl;
	}
	else
		cout << " Standard" << setw(34) << engine_weight << endl;
	cout << " Gyro:" << setw(69) << gyro_weight << endl;
	cout << " Jump Jets:" << setw(22) << jump_jet_number << setw(42) << jump_jet_weight << endl;
	cout << " Armor:" << setw(26) << armor_points << setw(42) << armor_weight << endl;
	cout << "----------------------------------------------------------------------------" << endl;
	cout << " Remaining for Weapons:" << setw(52) << remaining_tonnage << endl;
	cout << "----------------------------------------------------------------------------" << endl << endl;
}

/* Preliminary Weapon List */
void add_weapons(float remaining_tonnage,int heat_sink_total,float heat_sink_weight) {
	int add_weapon,done=0;

	do {
		cout << "You currently have " << remaining_tonnage << " tons left. Would you like to add a weapon (1=yes, 2=no)? ";
		cin >> add_weapon;
		cout << endl << endl;
		cout << "*************************************************************************************" << endl;
		cout << "*      Weapon List         Heat   Damage   Min Short Medium Long  Tons  Crit Ammo/T *" << endl;
		cout << "*************************************************************************************" << endl;
		cout << "*                                 ---Energy Weapons---                              *" << endl;
		cout << "* (1)  Flamer                3       2      --    1     2     3     1     1    --   *" << endl;
		cout << "* (2)  Small Laser           1       3      --    1     2     3   0.5     1    --   *" << endl;
		cout << "* (3)  Medium Laser          3       5      --    3     6     9     1     1    --   *" << endl;
		cout << "* (4)  Large Laser           8       8      --    5    10    15     5     2    --   *" << endl;
		cout << "* (5)  PPC                  10      10       3    6    12    18     7     3    --   *" << endl;
		cout << "*                                ---Ballistic Weapons---                            *" << endl;
		cout << "* (6)  Machine Gun           0       2      --    1     2     3   0.5     1   200   *" << endl;
		cout << "* (7)  Autocannon 2          1       2       4    8    16    24     6     1    45   *" << endl;
		cout << "* (8)  Autocannon 5          1       5       3    6    12    18     8     4    20   *" << endl;
		cout << "* (9)  Autocannon 10         3      10      --    5    10    15    12     7    10   *" << endl;
		cout << "* (10) Autocannon 20         7      20      --    3     6     9    14    10     5   *" << endl;
		cout << "*                                 ---Missile Weapons---                             *" << endl;
		cout << "* (11) LRM 5                 2    1/Msl      6    7    14    21     2     1    24   *" << endl;
		cout << "* (12) LRM 10                4    1/Msl      6    7    14    21     5     2    12   *" << endl;
		cout << "* (13) LRM 15                5    1/Msl      6    7    14    21     7     3     8   *" << endl;
		cout << "* (14) LRM 20                6    1/Msl      6    7    14    21    10     5     6   *" << endl;
		cout << "* (15) SRM 2                 2    2/Msl     --    3     6     9     1     1    50   *" << endl;
		cout << "* (16) SRM 4                 3    2/Msl     --    3     6     9     2     1    25   *" << endl;
		cout << "* (17) SRM 6                 4    2/Msl     --    3     6     9     3     2    15   *" << endl;
		cout << "*                                 ---Other Equipment---                             *" << endl;
		cout << "* (18) Hatchet               0        *     --   --    --    --    **    **    --   *" << endl;
		cout << "* (19) Heat Sink            -1       --     --   --    --    --     1     1    --   *" << endl;
		cout << "*************************************************************************************" << endl << endl;
		cout << "* Mech tonnage divided by 5" << endl;
		cout << "* Mech tonnage divided by 15" << endl;
		cout << "Note: Ammo can only be in one ton allotments, expect for machine gun ammo (can be 0.5 for 100 rounds)" << endl << endl;
		cout << "Which weapon would you like to add? ";
	} while(remaining_tonnage > 0 && done == 0);
}

int armor_allocation(int armor_points,int tonnage) {
	int max_ct_armor,max_rt_armor,max_lt_armor,max_ra_armor,max_la_armor,max_rl_armor,
		max_ll_armor,hd_armor,ct_armor,rt_armor,lt_armor,ra_armor,la_armor,rl_armor,ll_armor,rear_ct_armor,
		rear_rt_armor,rear_lt_armor,done=0,decremented_armor_points;

	switch(tonnage) {
		case 20:
			max_ct_armor = 12;
			max_rt_armor = 10;
			max_lt_armor = 10;
			max_ra_armor = 6;
			max_la_armor = 6;
			max_rl_armor = 8;
			max_ll_armor = 8;
			break;
		case 25:
			max_ct_armor = 16;
			max_rt_armor = 12;
			max_lt_armor = 12;
			max_ra_armor = 8;
			max_la_armor = 8;
			max_rl_armor = 12;
			max_ll_armor = 12;
			break;
		case 30:
			max_ct_armor = 20;
			max_rt_armor = 14;
			max_lt_armor = 14;
			max_ra_armor = 10;
			max_la_armor = 10;
			max_rl_armor = 14;
			max_ll_armor = 14;
			break;
		case 35:
			max_ct_armor = 22;
			max_rt_armor = 16;
			max_lt_armor = 16;
			max_ra_armor = 12;
			max_la_armor = 12;
			max_rl_armor = 16;
			max_ll_armor = 16;
			break;
		case 40:
			max_ct_armor = 24;
			max_rt_armor = 20;
			max_lt_armor = 20;
			max_ra_armor = 12;
			max_la_armor = 12;
			max_rl_armor = 20;
			max_ll_armor = 20;
			break;
		case 45:
			max_ct_armor = 28;
			max_rt_armor = 22;
			max_lt_armor = 22;
			max_ra_armor = 14;
			max_la_armor = 14;
			max_rl_armor = 22;
			max_ll_armor = 22;
			break;
		case 50:
			max_ct_armor = 32;
			max_rt_armor = 24;
			max_lt_armor = 24;
			max_ra_armor = 16;
			max_la_armor = 16;
			max_rl_armor = 24;
			max_ll_armor = 24;
			break;
		case 55:
			max_ct_armor = 36;
			max_rt_armor = 26;
			max_lt_armor = 26;
			max_ra_armor = 18;
			max_la_armor = 18;
			max_rl_armor = 26;
			max_ll_armor = 26;
			break;
		case 60:
			max_ct_armor = 40;
			max_rt_armor = 28;
			max_lt_armor = 28;
			max_ra_armor = 20;
			max_la_armor = 20;
			max_rl_armor = 28;
			max_ll_armor = 28;
			break;
		case 65:
			max_ct_armor = 42;
			max_rt_armor = 30;
			max_lt_armor = 30;
			max_ra_armor = 20;
			max_la_armor = 20;
			max_rl_armor = 30;
			max_ll_armor = 30;
			break;
		case 70:
			max_ct_armor = 44;
			max_rt_armor = 30;
			max_lt_armor = 30;
			max_ra_armor = 22;
			max_la_armor = 22;
			max_rl_armor = 30;
			max_ll_armor = 30;
			break;
		case 75:
			max_ct_armor = 46;
			max_rt_armor = 32;
			max_lt_armor = 32;
			max_ra_armor = 24;
			max_la_armor = 24;
			max_rl_armor = 32;
			max_ll_armor = 32;
			break;
		case 80:
			max_ct_armor = 50;
			max_rt_armor = 34;
			max_lt_armor = 34;
			max_ra_armor = 26;
			max_la_armor = 26;
			max_rl_armor = 34;
			max_ll_armor = 34;
			break;
		case 85:
			max_ct_armor = 54;
			max_rt_armor = 36;
			max_lt_armor = 36;
			max_ra_armor = 28;
			max_la_armor = 28;
			max_rl_armor = 36;
			max_ll_armor = 36;
			break;
		case 90:
			max_ct_armor = 58;
			max_rt_armor = 38;
			max_lt_armor = 38;
			max_ra_armor = 30;
			max_la_armor = 30;
			max_rl_armor = 38;
			max_ll_armor = 38;
			break;
		case 95:
			max_ct_armor = 60;
			max_rt_armor = 40;
			max_lt_armor = 40;
			max_ra_armor = 32;
			max_la_armor = 32;
			max_rl_armor = 40;
			max_ll_armor = 40;
			break;
		case 100:
			max_ct_armor = 62;
			max_rt_armor = 42;
			max_lt_armor = 42;
			max_ra_armor = 34;
			max_la_armor = 34;
			max_rl_armor = 42;
			max_ll_armor = 42;
			break;
	}
	do {
		hd_armor=0;
		ct_armor=0;
		rt_armor=0;
		lt_armor=0;
		ra_armor=0;
		la_armor=0;
		rl_armor=0;
		ll_armor=0;
		rear_ct_armor=0;
		rear_rt_armor=0;
		rear_lt_armor=0;
		cout << "How many armor points for the head (up to 9)?" << endl;
		cin >> hd_armor;
		decremented_armor_points = armor_points;
		decremented_armor_points -= hd_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the center torso (up to " << max_ct_armor << ")?" << endl;
		cout << "*Remember that this total takes into account rear-facing armor allocated later..." << endl;
		cin >> ct_armor;
		decremented_armor_points -= ct_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the right torso (up to " << max_rt_armor << ")?" << endl;
		cout << "*Remember that this total takes into account rear-facing armor allocated later..." << endl;
		cin >> rt_armor;
		decremented_armor_points -= rt_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the left torso (up to " << max_lt_armor << ")?" << endl;
		cout << "*Remember that this total takes into account rear-facing armor allocated later..." << endl;
		cin >> lt_armor;
		decremented_armor_points -= lt_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the right arm (up to " << max_ra_armor << ")?" << endl;
		cin >> ra_armor;
		decremented_armor_points -= ra_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the left arm (up to " << max_la_armor << ")?" << endl;
		cin >> la_armor;
		decremented_armor_points -= la_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the right leg (up to " << max_rl_armor << ")?" << endl;
		cin >> rl_armor;
		decremented_armor_points -= rl_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the left leg (up to " << max_ll_armor << ")?" << endl;
		cin >> ll_armor;
		decremented_armor_points -= ll_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the rear center torso (up to " << max_ct_armor << ")?" << endl;
		cin >> rear_ct_armor;
		decremented_armor_points -= rear_ct_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the rear right torso (up to " << max_rt_armor << ")?" << endl;
		cin >> rear_rt_armor;
		decremented_armor_points -= rear_rt_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		cout << "How many armor points for the rear left torso (up to " << max_lt_armor << ")?" << endl;
		cin >> rear_lt_armor;
		decremented_armor_points -= rear_lt_armor;
		cout << "Remaining/unallocated armor points: " << decremented_armor_points << endl << endl;
		if(decremented_armor_points != 0) {
			cout << "Unallocated armor points. Please restart allocation process." << endl;
		} else {
			cout << "...Armor allocation successful..." << endl;
			cout << "*********************************" << endl;
			cout << "* Head:                      " << setw(2) << hd_armor << " *" << endl;
			cout << "* Center Torso:              " << setw(2) << ct_armor << " *" << endl;
			cout << "* R/L Torso:              " << setw(2) << rt_armor << "/" << setw(2) << lt_armor << " *" << endl;
			cout << "* R/L Arm:                " << setw(2) << ra_armor << "/" << setw(2) << la_armor << " *" << endl;
			cout << "* R/L Leg:                " << setw(2) << rl_armor << "/" << setw(2) << ll_armor << " *" << endl;
			cout << "* Rear Center Torso:         " << setw(2) << rear_ct_armor << " *" << endl;
			cout << "* Rear R/L Torso:         " << setw(2) << rear_rt_armor << "/" << setw(2) << rear_lt_armor << " *" << endl;
			cout << "*********************************" << endl << endl;
			cout << "Allocation satisfactory? (1=yes, 2=restart allocation) ";
			cin >> done;
		}
	} while (!(done == 1));
	// user_mech1.hd_armor = hd_armor;
	// user_mech1.ct_armor = ct_armor;
	// user_mech1.rt_armor = rt_armor;
	// user_mech1.lt_armor = lt_armor;
	// user_mech1.ra_armor = ra_armor;
	// user_mech1.la_armor = la_armor;
	// user_mech1.rl_armor = rl_armor;
	// user_mech1.ll_armor = ll_armor;
	// user_mech1.rear_ct_armor = rear_ct_armor;
	// user_mech1.rear_rt_armor = rear_rt_armor;
	// user_mech1.rear_lt_armor = rear_lt_armor;
}

int main() {

	/* Created Base Weapon Objects */

	//Flamer
	Weapon flamer;
	flamer.name = "Flamer";
	flamer.weight = 1.0;
	flamer.heat = 3.0;
	flamer.critical_spaces = 1;
	flamer.range_short = 1;
	flamer.range_medium = 2;
	flamer.range_long = 3;
	flamer.damage = 2;
	flamer.ammo_per_ton = 0;
	flamer.weapon_type = "E";

	//Small Laser
	Weapon small_laser;
	small_laser.name = "Small Laser";
	small_laser.weight = 0.5;
	small_laser.heat = 1.0;
	small_laser.critical_spaces = 1;
	small_laser.range_short = 1;
	small_laser.range_medium = 2;
	small_laser.range_long = 3;
	small_laser.damage = 3;
	small_laser.ammo_per_ton = 0;
	small_laser.weapon_type = "E";

	//Medium Laser
	Weapon medium_laser;
	medium_laser.name = "Medium Laser";
	medium_laser.weight = 1.0;
	medium_laser.heat = 3.0;
	medium_laser.critical_spaces = 1;
	medium_laser.range_short = 3;
	medium_laser.range_medium = 6;
	medium_laser.range_long = 9;
	medium_laser.damage = 5;
	medium_laser.ammo_per_ton = 0;
	medium_laser.weapon_type = "E";

	//Large Laser
	Weapon large_laser;
	large_laser.name = "Large Laser";
	large_laser.weight = 5.0;
	large_laser.heat = 8.0;
	large_laser.critical_spaces = 2;
	large_laser.range_short = 5;
	large_laser.range_medium = 10;
	large_laser.range_long = 15;
	large_laser.damage = 8;
	large_laser.ammo_per_ton = 0;
	large_laser.weapon_type = "E";

	//PPC
	Weapon ppc;
	ppc.name = "PPC";
	ppc.weight = 7.0;
	ppc.heat = 10.0;
	ppc.critical_spaces = 3;
	ppc.range_short = 6;
	ppc.range_medium = 12;
	ppc.range_long = 18;
	ppc.damage = 10;
	ppc.ammo_per_ton = 0;
	ppc.weapon_type = "E";

	//Machine Gun
	Weapon machine_gun;
	machine_gun.name = "Machine Gun";
	machine_gun.weight = 0.5;
	machine_gun.heat = 0.0;
	machine_gun.critical_spaces = 1;
	machine_gun.range_short = 1;
	machine_gun.range_medium = 2;
	machine_gun.range_long = 3;
	machine_gun.damage = 2;
	machine_gun.ammo_per_ton = 200;
	machine_gun.weapon_type = "B";

	//Autocannon 2
	Weapon autocannon_2;
	autocannon_2.name = "Autocannon 2";
	autocannon_2.weight = 6.0;
	autocannon_2.heat = 1.0;
	autocannon_2.critical_spaces = 1;
	autocannon_2.range_short = 8;
	autocannon_2.range_medium = 16;
	autocannon_2.range_long = 24;
	autocannon_2.damage = 2;
	autocannon_2.ammo_per_ton = 45;
	autocannon_2.weapon_type = "B";

	//Autocannon 5
	Weapon autocannon_5;
	autocannon_5.name = "Autocannon 5";
	autocannon_5.weight = 8.0;
	autocannon_5.heat = 1.0;
	autocannon_5.critical_spaces = 4;
	autocannon_5.range_short = 6;
	autocannon_5.range_medium = 12;
	autocannon_5.range_long = 18;
	autocannon_5.damage = 5;
	autocannon_5.ammo_per_ton = 20;
	autocannon_5.weapon_type = "B";

	//Autocannon 10
	Weapon autocannon_10;
	autocannon_10.name = "Autocannon 10";
	autocannon_10.weight = 12.0;
	autocannon_10.heat = 3.0;
	autocannon_10.critical_spaces = 7;
	autocannon_10.range_short = 5;
	autocannon_10.range_medium = 10;
	autocannon_10.range_long = 15;
	autocannon_10.damage = 10;
	autocannon_10.ammo_per_ton = 10;
	autocannon_10.weapon_type = "B";

	//Autocannon 20
	Weapon autocannon_20;
	autocannon_20.name = "Autocannon 20";
	autocannon_20.weight = 14.0;
	autocannon_20.heat = 7.0;
	autocannon_20.critical_spaces = 10;
	autocannon_20.range_short = 3;
	autocannon_20.range_medium = 6;
	autocannon_20.range_long = 9;
	autocannon_20.damage = 20;
	autocannon_20.ammo_per_ton = 5;
	autocannon_20.weapon_type = "B";

	//LRM 5
	Weapon lrm_5;
	lrm_5.name = "LRM 5";
	lrm_5.weight = 2.0;
	lrm_5.heat = 2.0;
	lrm_5.critical_spaces = 1;
	lrm_5.range_short = 7;
	lrm_5.range_medium = 14;
	lrm_5.range_long = 21;
	lrm_5.damage = 1;
	lrm_5.ammo_per_ton = 24;
	lrm_5.weapon_type = "L";

	//LRM 5
	Weapon lrm_10;
	lrm_10.name = "LRM 10";
	lrm_10.weight = 5.0;
	lrm_10.heat = 4.0;
	lrm_10.critical_spaces = 2;
	lrm_10.range_short = 7;
	lrm_10.range_medium = 14;
	lrm_10.range_long = 21;
	lrm_10.damage = 1;
	lrm_10.ammo_per_ton = 12;
	lrm_10.weapon_type = "L";

	//LRM 5
	Weapon lrm_15;
	lrm_15.name = "LRM 15";
	lrm_15.weight = 7.0;
	lrm_15.heat = 5.0;
	lrm_15.critical_spaces = 3;
	lrm_15.range_short = 7;
	lrm_15.range_medium = 14;
	lrm_15.range_long = 21;
	lrm_15.damage = 1;
	lrm_15.ammo_per_ton = 8;
	lrm_15.weapon_type = "L";

	//LRM 5
	Weapon lrm_20;
	lrm_20.name = "LRM 20";
	lrm_20.weight = 10.0;
	lrm_20.heat = 6.0;
	lrm_20.critical_spaces = 5;
	lrm_20.range_short = 7;
	lrm_20.range_medium = 14;
	lrm_20.range_long = 21;
	lrm_20.damage = 1;
	lrm_20.ammo_per_ton = 6;
	lrm_20.weapon_type = "L";

	//SRM 2
	Weapon srm_2;
	srm_2.name = "SRM 2";
	srm_2.weight = 1.0;
	srm_2.heat = 2.0;
	srm_2.critical_spaces = 1;
	srm_2.range_short = 3;
	srm_2.range_medium = 6;
	srm_2.range_long = 9;
	srm_2.damage = 2;
	srm_2.ammo_per_ton = 50;
	srm_2.weapon_type = "S";

	//SRM 4
	Weapon srm_4;
	srm_4.name = "SRM 4";
	srm_4.weight = 2.0;
	srm_4.heat = 3.0;
	srm_4.critical_spaces = 1;
	srm_4.range_short = 3;
	srm_4.range_medium = 6;
	srm_4.range_long = 9;
	srm_4.damage = 2;
	srm_4.ammo_per_ton = 25;
	srm_4.weapon_type = "S";

	//SRM 6
	Weapon srm_6;
	srm_6.name = "SRM 6";
	srm_6.weight = 3.0;
	srm_6.heat = 4.0;
	srm_6.critical_spaces = 2;
	srm_6.range_short = 3;
	srm_6.range_medium = 6;
	srm_6.range_long = 9;
	srm_6.damage = 2;
	srm_6.ammo_per_ton = 15;
	srm_6.weapon_type = "S";

	string mechClass,mechName;
	int decision,tonnage,heat_sink_total=10,armor_points,xl_engine,endo_steel,jump_jet_number,unallocated_armor_points;
	float engine_rating=0.0,internal_structure=0.0,cockpit=3.0,engine_weight=0.0,
		gyro_weight=0.0,remaining_tonnage=0.0,heat_sink_weight=0.0,armor_weight=0.0,jump_jet_weight=0.0;
	bool valid=false;

	decision = menu();
	cout << "***************************MECH BAY***************************" << endl;
	cout << "Input name (Please use underscore instead of spaces): ";
	cin >> mechName;
	while(valid == false) {
		cout << "Input tonnage: ";
		cin >> tonnage;
		if(tonnage < 20 || tonnage > 100 || tonnage % 5 != 0){
			cout << "Invalid tonnage. Please try again." << endl;
		}else
			valid = true;
	}
	if(tonnage <= 35) {
		mechClass = "light";
	} else if(tonnage <= 55) {
		mechClass = "medium";
	} else if(tonnage <= 75) {
		mechClass = "heavy";
	} else if(tonnage <= 100) {
		mechClass = "assault";
	} else {
		cout << "Error. Invalid tonnage." << endl;
	}
	engine_rating = find_engine_rating(tonnage);
	engine_weight = find_engine_weight(engine_rating);
	jump_jet_number = find_jump_jets(tonnage,engine_rating);
	jump_jet_weight = find_jump_jet_weight(tonnage,jump_jet_number);
	internal_structure = (float)tonnage/10.0;
	xl_engine = find_xl_engine();
	if(xl_engine == 1) {
		engine_weight = engine_weight/2;
	}
	endo_steel = find_endo_steel();
	if(endo_steel == 1) {
		internal_structure = internal_structure/2;
	}
	gyro_weight = find_gyro_weight(engine_rating);
	armor_weight = find_armor_weight(tonnage);
	armor_points = find_armor_points(tonnage,armor_weight);
	remaining_tonnage = (float)tonnage-cockpit-internal_structure-engine_weight-gyro_weight-armor_weight-jump_jet_weight;
	mech_stats(mechClass,mechName,cockpit,internal_structure,engine_rating,engine_weight,gyro_weight,
		remaining_tonnage,heat_sink_total,heat_sink_weight,armor_weight,armor_points,xl_engine,endo_steel,
		jump_jet_number,jump_jet_weight);

	/* Initial Mech Object Creation */
	Mech user_mech1;
	user_mech1.name = mechName;
	user_mech1.walking_mp = engine_rating/tonnage;
	user_mech1.running_mp = floor(user_mech1.walking_mp*1.5 + 0.5);
	user_mech1.jumping_mp = jump_jet_number;
	user_mech1.armor_points = armor_points;
	user_mech1.remaining_tonnage = remaining_tonnage;
	unallocated_armor_points = user_mech1.armor_points;
	cout << "Your new Mech: " << endl;
	cout << "**************" << endl;
	cout << "Name: " << user_mech1.name << endl;
	cout << "Walking MP: " << user_mech1.walking_mp << endl;
	cout << "Running MP: " << user_mech1.running_mp << endl;
	cout << "Jumping MP: " << user_mech1.jumping_mp << endl;
	cout << "Unallocated Armor Points: " << user_mech1.armor_points << endl;
	cout << "Unallocated Equipment Tonnage: " << user_mech1.remaining_tonnage << endl << endl;

	unallocated_armor_points = armor_allocation(user_mech1.armor_points,tonnage);

	/* Preliminary Weapon List for Adding Weapons */
	// while(more_weapons == 1) {
	// 	add_weapons(remaining_tonnage,heat_sink_total,heat_sink_weight);
	// }

return(0);
}