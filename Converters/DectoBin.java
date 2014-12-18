/*********************************************************************/
/* Program Name: DectoBin                                            */
/* Date: December 18, 2014                                           */
/* Description: Convert decimal to binary or binary to decimal       */
/*********************************************************************/

import java.util.*;
import java.lang.Math;
public class DectoBin{

	private static final double limit = Math.pow(2.0,23.0);

	public static void main(String args[]){
		Scanner input = new Scanner(System.in);
		System.out.print("Would you like to convert a decimal or a binary number? ");
		String dec_or_bin = input.nextLine();
		if(dec_or_bin.equalsIgnoreCase("decimal")){
			System.out.print("Input a decimal value: ");
			int value = input.nextInt();
			System.out.println(limit);
			int twoValues = (int)limit;
			for(int a=twoValues; a>0;){
				if(value - a > 0){
					System.out.println(a);
				}
				a /= 2;
			}
			// System.out.println(value);
			// value = value % 10;
			// System.out.println(value);
		} else if(dec_or_bin.equalsIgnoreCase("binary")){
			System.out.println("You chose binary, right?");
		} else {
			System.out.println("Yeah, you're not playing along, are you?");
		}
	}
}