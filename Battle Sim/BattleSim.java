/*********************************************************************/
/* Program Name: BattleSim                                           */
/* Date: December 17, 2014                                           */
/* Description: At present, create a character, and fight a randomly */
/*     generated enemy by alternating damage within a single         */
/*     instance. Need to implement special "tech" abilities and      */
/*     multiple turn logic.                                          */
/*********************************************************************/

import java.util.*;
public class BattleSim{
	public static void main(String args[]){

		/* Main() Variable Assignment */
		Scanner in = new Scanner(System.in);
		int char_class = 0, enem_class = 0;
		int life_pts = 0;
		int tech_pts = 0;
		int power = 0;
		int hit_rate = 0;
		String name = "";
		Random rand = new Random();

		/* Introduction and Instructions */

		/* Choose Class and Name Character */
		System.out.println();
		System.out.println("Choose a class: (Warrior(1), Ranger(2), or Wizard(3))");
		char_class = in.nextInt();
		in.nextLine();
		System.out.println("Enter your character's name: ");
		name = in.nextLine();

		/* Character Class Assignment */
		switch(char_class){
			case 1:
				life_pts = 1000;
				tech_pts = 50;
				power = 200;
				hit_rate = 50;
				break;
			case 2:
				life_pts = 900;
				tech_pts = 50;
				power = 100;
				hit_rate = 100;
				break;
			case 3:
				life_pts = 800;
				tech_pts = 50;
				power = 150;
				hit_rate = 75;
				break;
			default:
				break;
		}

		/* Character and Opponent Creation */
		Hero character = new Hero(name, char_class, life_pts, tech_pts, power, hit_rate);
		Enemy enemy = new Enemy();
		enem_class = rand.nextInt(3)+1;
		switch(enem_class){
			case 1:
				enemy = new Enemy(enem_class, 1000, 50, 200, 50);
				break;
			case 2:
				enemy = new Enemy(enem_class, 900, 50, 100, 100);
				break;
			case 3:
				enemy = new Enemy(enem_class, 800, 50, 150, 75);
				break;
			default:
				break;
		}

		System.out.println(character);
		System.out.println(enemy);

		/* Enter Fray */
		boolean heal = true;
		do {
			int choice = menu(character,enemy,in,heal);
			if(heal){
				switch(choice){
					case 1:
						heroAttack(character, enemy);
						System.out.println(enemy);
						break;
					case 2:
						heroTech(character, enemy);
						System.out.println(enemy);
						break;
					case 3:
						heal = heroHeal(character);
						System.out.println(character);
						break;
					default:
						break;
				}
			} else {
				switch(choice){
					case 1:
						heroAttack(character, enemy);
						System.out.println(enemy);
						break;
					case 2:
						heroTech(character, enemy);
						System.out.println(enemy);
						break;
					default:
						break;
				}
			}

			/* If enemy has no life points after character action, declare victory and break while loop */
			if(enemy.getLife_Pts() <= 0){
				System.out.println(character.getName() + " killed the mighty " + enemy.getName() + "!");
				System.out.println(character);
				System.out.println(enemy);
				break;
			}

			/* Enemy attack */
			enemyAttack(character, enemy);
			System.out.println(character);

			/* If character has no life points after enemy action, declare defeat and break while loop */
			if(character.getLife_Pts() <= 0){
				System.out.println(character.getName() + " was slain by the mighty " + enemy.getName() + "!");
				System.out.println(character);
				System.out.println(enemy);
				break;
			}
			System.out.println();
		} while(character.getLife_Pts() != 0 || enemy.getLife_Pts() != 0);
	}

	/* Character orders menu */
	public static int menu(Hero character, Enemy enemy, Scanner in, boolean heal){
		System.out.println("***************************");
		System.out.println("* Choose action:          *");
		System.out.println("*                         *");
		System.out.println("*   (1) Attack            *");
		System.out.println("*   (2) Technique         *");
		if(heal != false){
			System.out.println("*   (3) Use Heal Potion   *");
		}
		System.out.println("*                         *");
		System.out.println("***************************");
		int choice = in.nextInt();
		return choice;
	}

	/* Calculate Hero's Attack Based on Class and Hit Rate */
	public static void heroAttack(Hero character, Enemy enemy){
		int hit = 0;
		Random rand = new Random();
		switch(character.getChar_Class()){
			case 1:
				hit = rand.nextInt(2);
				if(hit == 1){
					successAttack(character,enemy);
				} else {
					failAttack(character,enemy);
				}
				break;
			case 2:
				hit = rand.nextInt(1);
				if(hit == 0){
					successAttack(character,enemy);
				} else {
					failAttack(character,enemy);
				}
				break;
			case 3:
				hit = rand.nextInt(4);
				if(hit != 3){
					successAttack(character,enemy);
				} else {
					failAttack(character,enemy);
				}
				break;
			default:
				break;
		}
	}

	/* Calculates a Successful Attack's Damage Done to Enemy */
	public static void successAttack(Hero character, Enemy enemy){
		Random rand = new Random();
		int attack = rand.nextInt(character.getPower()-(int)(character.getPower()*0.75)) + (int)(character.getPower()*0.75+1);
		enemy.setLife_Pts(enemy.getLife_Pts() - attack);
		System.out.println(character.getName() + " struck " + enemy.getName() + " for " + attack + " points!");
	}

	/* Prints the Fail Attack Message */
	public static void failAttack(Hero character, Enemy enemy){
		System.out.println(character.getName() + " missed striking " + enemy.getName() + ".");
	}

	/* Calculate Hero's Tech Based on Class */
	public static void heroTech(Hero character, Enemy enemy){
		int hit = 0;
		Random rand = new Random();
		switch(character.getChar_Class()){
			case 1:
				if(character.getTech_Pts() >= 20){
					character.setTech_Pts(character.getTech_Pts() - 20);
					int attack = 200;
					enemy.setLife_Pts(enemy.getLife_Pts() - attack);
					System.out.println(character.getName() + " used both hands and struck " + enemy.getName() + " with all of their might for " + attack + " points!");
				} else {
					System.out.println("You limply swung your arms at " + enemy.getName() + ". " + character.getName() + "  doesn't have enough energy for their best techniques!");
				}
				break;
			case 2:
				if(character.getTech_Pts() >= 20){
					character.setTech_Pts(character.getTech_Pts() - 20);
					int attack = rand.nextInt(character.getPower()-(int)(character.getPower()*0.75)) + (int)(character.getPower()*0.75+1);
					attack += 50;
					enemy.setLife_Pts(enemy.getLife_Pts() - attack);
					System.out.println(character.getName() + " used a special blessed arrow head and hit " + enemy.getName() + " square in the chest for " + attack + " points!");
				} else {
					System.out.println(character.getName() + " fumbled with some arrows while trying to attack " + enemy.getName() + ". " + character.getName() + " doesn't have enough energy for their best techniques!");
				}
				break;
			case 3:
				if(character.getTech_Pts() >= 20){
					character.setTech_Pts(character.getTech_Pts() - 20);
					character.setPower(character.getPower() - 10);
					int attack = 300;
					enemy.setLife_Pts(enemy.getLife_Pts() - attack);
					System.out.println(character.getName() + " focused all of their power and sent an enormous fireball at " + enemy.getName() + ", causing " + attack + " damage, but also drained some of " + character.getName() + "\'s power from the exertion!");
				} else {
					System.out.println(character.getName() + " feebly raised tired arms at " + enemy.getName() + ". " + character.getName() + " doesn't have enough energy for their best techniques!");
				}
				break;
			default:
				break;
		}
	}

	/* Heal Hero by 150 life_points */
	public static boolean heroHeal(Hero character){
		int hp = character.getLife_Pts();
		int char_class = character.getChar_Class();
		character.setLife_Pts(hp + 150);
		switch(char_class){
			case 1:
				if(hp > 1000){
					character.setLife_Pts(1000);
				}
				break;
			case 2:
				if(hp > 900){
					character.setLife_Pts(900);
				}
				break;
			case 3:
				if(hp > 800){
					character.setLife_Pts(800);
				}
				break;
			default:
				break;
		}
		System.out.println(character.getName() + " drank a handy potion and healed 150 points!");
		return false;
	}

	/* Calculate Enemy's Attack Based on Hit Rate */
	public static void enemyAttack(Hero character, Enemy enemy){
		int hit = 0;
		int epower = enemy.getPower();
		Random rand = new Random();
		switch(enemy.getEnem_Class()){
			case 1:
				hit = rand.nextInt(2);
				if(hit == 1){
					int attack = rand.nextInt(epower-(int)(epower*0.75)) + (int)(epower*0.75+1);
					character.setLife_Pts(character.getLife_Pts() - attack);
					System.out.println(character.getName() + " was struck by " + enemy.getName() + " for " + attack + " points!");
				} else {
					System.out.println(character.getName() + " evaded a strike by " + enemy.getName() + ".");
				}
				break;
			case 2:
				hit = rand.nextInt(1);
				if(hit == 0){
					int attack = rand.nextInt(epower-(int)(epower*0.75)) + (int)(epower*0.75+1);
					character.setLife_Pts(character.getLife_Pts() - attack);
					System.out.println(character.getName() + " was struck by " + enemy.getName() + " for " + attack + " points!");
				} else {
					System.out.println(character.getName() + " evaded a strike by " + enemy.getName() + ".");
				}
				break;
			case 3:
				hit = rand.nextInt(4);
				if(hit != 3){
					int attack = rand.nextInt(epower-(int)(epower*0.75)) + (int)(epower*0.75+1);
					character.setLife_Pts(character.getLife_Pts() - attack);
					System.out.println(character.getName() + " was struck by " + enemy.getName() + " for " + attack + " points!");
				} else {
					System.out.println(character.getName() + " evaded a strike by " + enemy.getName() + ".");
				}
				break;
			default:
				break;
		}
	}
}