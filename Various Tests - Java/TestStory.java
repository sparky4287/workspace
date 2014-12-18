/*
*	(11/7/2014 2:30pm)
*	Program is a choose-your-own-adventure whose scenarios change based on character characteristics
*/

import java.util.*;
public class TestStory{ 

	public static void main(String args[]){
		Scanner in = new Scanner(System.in);	// Set Scanner in
		String gender = establishGender(in);	// Get gender of character
		String pronoun = proNoun(gender);		// Get pronoun based on gender
	}

	// /* Chapter One -- Returns Scenario Outcome */
	// public static int chapterOne(){

	// }

	// /* Chapter Two -- Returns Scenario Outcome */
	// public static int chapterTwo(){
		
	// }

	// /* Chapter Three -- Returns Scenario Outcome */
	// public static int chapterThree(){
		
	// }

	// /* Final Chapter -- Returns Scenario Outcome */
	// public static int finalChapter(){
		
	// }

	/*
	*	(11/7/2014 2:41pm)
	*	Establish, then validates whether the player is male or female
	*/
	public static String establishGender(Scanner in){
		String gender = "";
		do{
			System.out.print("Please enter your character's gender ('m' or 'f'): ");
			gender = in.nextLine();
			if(!(gender.equals("m") || gender.equals("f"))){
				System.out.println("Please enter a valid choice for gender.");
			}
		} while(!(gender.equals("m") || gender.equals("f")));
		return gender;
	}

	/* 	
	*	(11/7/2014 2:41pm)
	*	Through validated gender, establishes pronoun to be used in the story
	*/
	public static String proNoun(String gender){
		String pronoun = "";
		switch(gender){
			case "m":
				pronoun = "He";
				break;
			case "f":
				pronoun = "She";
				break;
			default: 
				break;
		}
		return pronoun;
	}
}


/****************************************************/
/*                                 *                */
/*                                 *                */
/*                                 *                */
/*                                 *                */
/******************                *                */
/*                                                  */
/*                                                  */
/*                                                  */
/*                                                  */
/*                ******************                */
/*                *
/*                *
/*                *
/*                *
/*                ***********************************/
/*
/*
/*
/*
/****************************************************/