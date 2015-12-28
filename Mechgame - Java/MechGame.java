/*********************************************************************/
/* Program Name: MechGame                                            */
/* Date: October 31, 2015                                            */
/* Description: Basic Java version of Mechwarrior tabletop game      */
/*********************************************************************/

import java.util.*;
public class MechGame
{
	public static void main(String args[])
	{
		Weapon test = new Weapon("Small Laser","Energy",1,2,0.5,0,1,2,3,3);
		test.toString();
	}
}