#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
using namespace std;

/* Function for a Single Roll of One Six-Sided Dice */
int roll_1d6() {
    int roll;

    roll = rand() % 6 + 1;
    return roll;
}

/* Function for a Single Roll of Two Six-Sided Dice */
int roll_2d6() {
    int roll;

    roll = rand() % 11 + 2;
    return roll;
}

/* Randomly Determines a Gunnery Skill for the Pilot */
int find_gunnery_skill() {
    int value,gunnery_skill;

    value = roll_1d6();
    if(value > 0 && value <= 4) {
        gunnery_skill = 4;
    } else if(value > 4 && value <= 6) {
        gunnery_skill = 3;
    }
    return gunnery_skill;
}

/* User Determines a Range for the Firing Weapon */
int find_range(int max) {
    int range,valid=0;

    do {
        cout << "What is the range to the target? ";
        cin >> range;
        if(range < 0 || range > max) {
            cout << "Invalid range. The range must be between 0 and " << max << " spaces. Please try again." << endl;
        } else
            valid = 1;
    } while(!(valid == 1));
    return range;
}

/* User Determines Distance Traveled (Assumes a Heavy Mech) */
int find_traveled(int max_mp) {
    int traveled,valid=0;

    do {
        cout << "How far have you traveled this turn? ";
        cin >> traveled;
        if(traveled < 0 || traveled > max_mp) {
            cout << "Invalid distance for your Mech. Please try again." << endl;
        } else
            valid = 1;
    } while(!(valid == 1));
    return traveled;
}

/* User Determines Target Speed (Assumes a Heavy Mech) */
int find_target_speed() {
    int target_speed,valid=0;

    do {
        cout << "How fast is the target moving (0-8) this turn? ";
        cin >> target_speed;
        if(target_speed < 0 || target_speed > 8) {
            cout << "Invalid speed. For the target heavy Mech, the distance traveled can only be 0-8. Please try again." << endl;
        } else
            valid = 1;
    } while(!(valid == 1));
    return target_speed;
}

/* User Determines Intervening Terrain Modifier */
int find_intervening_terrain() {
    int intervening_terrain,valid=0;

    do {
        cout << "What should the terrain modifier be (0-4) this turn? ";
        cin >> intervening_terrain;
        cout << endl;
        if(intervening_terrain < 0 || intervening_terrain > 4) {
            cout << "Invalid terrain modifier. For the purposes of this process, choose 0-4. Please try again." << endl;
        } else
            valid = 1;
    } while(!(valid == 1));
    return intervening_terrain;
}

/* Compute Range Modifier Based on Range and Weapon Ranges */
int find_range_modifier(int range,int minimum,int short_range,int medium_range,int max_range) {
    if(range <= minimum) {
        return minimum-range+1;
    } else if(range <= short_range) {
        return 0;
    } else if(range <= medium_range) {
        return 2;
    } else if(range <= max_range) {
        return 4;
    }
}

/* Compute Traveled Modifier Based on Traveled Distance and Movement Ranges */
int find_traveled_modifier(int traveled,int walking,int running) {
    if(traveled == 0) {
        return 0;
    } else if(traveled <= walking) {
        return 1;
    } else if(traveled <= running) {
        return 2;
    }
}

/* Compute Target Speed Modifier Based on Traveled Distance */
int find_target_speed_modifier(int target_speed) {
    if(target_speed <= 2) {
        return 0;
    } else if(target_speed <= 4) {
        return 1;
    } else if(target_speed <= 6) {
        return 2;
    } else if(target_speed <= 9) {
        return 3;
    } else if(target_speed <= 17) {
        return 4;
    } else if(target_speed <= 24) {
        return 5;
    } else {
        return 6;
    }
}

int main () {
    int decision,roll,valid=1,gunnery_skill,range,traveled,target_speed,intervening_terrain,
    base_to_hit,hit_roll,attack,damage_roll,damage,weapon_choice,minimum,short_range,medium_range,
    max_range,walking,running;
    string weapon;

    srand (time(NULL));

    do {
        base_to_hit=0;
        cout << "Fire at a target? (1=yes, 0=exit)" << endl;
        cin >> decision;
        if(decision == 0) {
            cout << endl << "Okie doke. Goodbye!" << endl;
            valid = 0;
        } else if(decision == 1) {
            cout << "**********************" << endl;
            cout << "(1) LRM 20" << endl;
            cout << "(2) PPC" << endl;
            cout << "**********************" << endl;
            cout << "Which weapon are you firing? ";
            cin >> weapon_choice;
            if(weapon_choice == 1) {
                weapon = "LRM 20";
                minimum = 6;
                short_range = 7;
                medium_range = 14;
                max_range = 21;
            } else {
                weapon = "PPC";
                minimum = 3;
                short_range = 6;
                medium_range = 12;
                max_range = 18;
            }
            gunnery_skill = find_gunnery_skill();
            cout << "What is your walking speed? ";
            cin >> walking;
            cout << "What is your running speed? ";
            cin >> running;
            base_to_hit += gunnery_skill;
            range = find_range(max_range);
            base_to_hit += find_range_modifier(range,minimum,short_range,medium_range,max_range);
            traveled = find_traveled(running);
            base_to_hit += find_traveled_modifier(traveled,walking,running);
            target_speed = find_target_speed();
            base_to_hit += find_target_speed_modifier(target_speed);
            intervening_terrain = find_intervening_terrain();
            base_to_hit += intervening_terrain;
            cout << "**********************" << endl;
            cout << "Gunnery Skill: " << gunnery_skill << endl;
            cout << "Range: " << range << endl;
            cout << "Distance Traveled: " << traveled << endl;
            cout << "Target Speed: " << target_speed << endl;
            cout << "Intervening Terrain: " << intervening_terrain << endl;
            cout << "**********************" << endl;
            cout << "To-Hit Final Number: " << base_to_hit << endl;
            hit_roll = roll_2d6();
            cout << "Your Roll: " << hit_roll << endl;
            cout << "**********************" << endl;
            if(hit_roll >= base_to_hit) {
                attack = 1;
                cout << "Attack Succeeds!!!" << endl << endl;
                damage_roll = roll_2d6();
                if(weapon_choice == 1) {
                    cout << "LRM Damage Amount Roll: " << damage_roll << endl << endl;
                    if(damage_roll < 4) {
                        damage = 6;
                    } else if(damage_roll == 4) {
                        damage = 9;
                    } else if(damage_roll < 9) {
                        damage = 12;
                    } else if(damage_roll < 11) {
                        damage = 16;
                    } else if(damage_roll <= 12) {
                        damage = 20;
                    }
                } else if(weapon_choice == 2) {
                    damage = 10;
                }
                cout << "Your attack caused " << damage << " points of damage!" << endl << endl;
            } else {
                attack = 0;
                cout << "Attack Fails......" << endl << endl;
            }
        } else
            cout << "Error. Invalid input." << endl << endl;
    } while (!(valid == 0));
}