/******************************************************************/
/* Jon Shamber                                                    */
/* CSC15 – Professor Gita Faroughi                                */
/* Tuesday & Thursday 12:30 - 1:20pm                              */
/* HW #5: Calculate standard deviation of inputted set of numbers */
/******************************************************************/
import java.util.*;
 
public class StandardDeviation {
	static Scanner in = new Scanner(System.in);
	public static final int  Max_Number_Scores = 100;
  
  	public static void main(String[] args) {
   	
   		// Declare array and boolean for main while loop
	 	double[] scores = new double[Max_Number_Scores];
	 	boolean again = true;

	 	// Main prompt
		System.out.println("You will be prompted to enter your numbers. Enter -1 to indicate the end of your input.");
		System.out.println();

 		// Main while loop that repeats as long as the user wishes
 		while(again) {

 			// Declare main calculation variables while calling appropriate methods
	 		int count = fillArray(scores);
		 	double average=getAverage(scores, count),
		 		variance=getVariance(scores, count, average),
		 		standardDeviation=getStandardDeviation(variance);

		 	// Output
	 		System.out.println("You entered: " + arrayToString(scores, count));
	 		System.out.println("Average = " + average);
	 		System.out.println("Variance = " + variance);
	 		System.out.println("Standard Deviation = " + standardDeviation);
	 		System.out.println();
	 		System.out.println("*****************************************");
	 		System.out.println();
	 		System.out.println();

	 		// Ask user if another iteration is necessary
	 		System.out.println("Do you have another set of numbers? (yes/no)");
            String answer = in.next();
            if(answer.equalsIgnoreCase("no")) {
            	System.out.println("Goodbye");
                again = false;
            }
	 	}
  	}
  
  	// Transforms entire array of input into a string for output
   	public static String arrayToString(double[] scores, int count) {
	  	String phrase="";
	  	for(int a=0; a<count; a++){
	  		if(a != (count-1)){
	  			phrase += scores[a] + ", ";
	  		} else {
	  			phrase += scores[a];
	  		}
	  	}
	  	return phrase;
	}

	// Prompts user for input of numbers, validates, and then populates array while returning the count of inputs
	public static int fillArray(double[] scores) {
	  	int count=0;
	  	int index=1;
	  	double num=0.0;
	  	while(num >= 0){
	  		index = count+1;
	  		System.out.println("Enter number " + index);
            while(!in.hasNextDouble()) {
                System.out.println("Enter a valid double number:");
                in.next();
            }
            num = in.nextDouble();
            if (num >= 0){
                scores[count] = num;
                count++;
            }
	  	}
	   	return count;
	}

	// Calculates and returns the average of the numbers input in this iteration
	public static double getAverage(double[] scores, int count) {
	   	double sum=0.0;
	   	for(int a=0; a<count; a++){
	   		sum += scores[a];
	   	}
	   	return Math.round((sum / count) * 100.0) / 100.0;
	   
	}	
	
	// Calculates and returns the variance of the numbers input in this iteration based on average
	public static double getVariance(double[] scores, int count, double average) {
	    double sum=0.0;
	    for(int a=0; a<count; a++){
	    	sum += Math.pow((scores[a] - average), 2);
	    }
		return Math.round((sum / count) * 100.0) / 100.0;
	}

	// Calculates and returns the standard deviation of the numbers input in this iteration based on variance
	public static double getStandardDeviation(double variance) {
	  	return Math.round((Math.sqrt(variance)) * 100.0) / 100.0;
	}  	
}