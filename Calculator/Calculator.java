import java.util.*;
public class Calculator{
	public static void main(String args[]){

		/* Input Calculation */
		String phrase = inputString();

		/* Find Operator */
		String operator = findOperator(phrase);

		/* Find Numbers */
		double num1 = Double.parseDouble(phrase.substring(0,phrase.indexOf(operator)));
		double num2 = Double.parseDouble(phrase.substring(phrase.indexOf(operator)+1));

		/* Calculate Answer */
		String answer = findAnswer(num1,num2,operator);
		System.out.println(answer);
	}
	
	/* Initial User Calculation Input (returns full string of input) */
	public static String inputString() {
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a string for calculation. Include two numbers and a mathematical operator: ");
		String answer = in.nextLine();
		return answer;
	}

	/* Finds the operator being used in the string (returns string of a single operator) */
	public static String findOperator(String phrase){
		String answer = "";
		int add_Index = phrase.indexOf("+");
		int sub_Index = phrase.indexOf("-");
		int mul_Index = phrase.indexOf("*");
		int div_Index = phrase.indexOf("/");

		if(add_Index != -1){
			answer = "+";
		} else if(sub_Index != -1) {
			answer = "-";
		} else if(mul_Index != -1) {
			answer = "*";
		} else if(div_Index != -1) {
			answer = "/";
		} else {
			answer = "error";
		}
		return answer;
	}

	/* Calculate input and return correct answer (returns String of equation input and answer) */
	public static String findAnswer(double num1, double num2, String op) {
		String answerString = "";
		double answer = 0.0;
		switch(op) {
			case "+":
				answer = num1 + num2;
				break;
			case "-":
				answer = num1 - num2;
				break;
			case "*":
				answer = num1 * num2;
				break;
			case "/":
				answer = num1 / num2;
				break;
			default:
				break;
		}
		answerString += num1 + " " + op + " " + num2 + " = " + answer;
		return answerString;
	}
}