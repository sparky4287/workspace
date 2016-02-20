using System;
using System.Linq;
namespace CalculatorApplication
{
	class Calculation{

		public double FindMax(double num1, double num2)
		{
			double answer;
			if(num1 > num2)
				answer = num1;
			else
				answer = num2;
			return answer;
		}

		public double FindMin(double num1, double num2)
		{
			double answer;
			if(num1 < num2)
				answer = num1;
			else
				answer = num2;
			return answer;
		}

		public int FindFactorial(int num)
		{
			int answer;
			if(num == 1)
			{
				return num;
			}
			else
			{
				answer = FindFactorial(num - 1) * num;
				return answer;
			}
		}

		static void Main(string[] args)
		{
			int[] choice_array = {1, 2, 3, 4};
			int choice = 0,
				quit = choice_array[choice_array.Length-1],
				intAnswer,
				num3;
			double num1, num2, answer;

			Console.WriteLine("Choice array at last position: {0}", quit);

			while(choice != quit)
			{
				Console.WriteLine("Please choose an operation to perform:");
				Console.WriteLine("(1) Find maximum of two numbers");
				Console.WriteLine("(2) Find minimum of two numbers");
				Console.WriteLine("(3) Find the factorial of a number");
				Console.WriteLine("(4) Quit");
				choice = Convert.ToInt32(Console.ReadLine());

				if(choice == quit)
				{
					Console.WriteLine("You chose to exit. Goodbye!");
					Console.ReadLine();
					break;
				}
				else if(!choice_array.Contains(choice))
				{
					Console.WriteLine("You chose a weird option... Try again!");
					Console.ReadLine();
					continue;
				}
				else
				{
					switch(choice)
					{
						case 1:
							Console.WriteLine("Enter first number: ");
							num1 = Convert.ToDouble(Console.ReadLine());
							Console.WriteLine("Enter second number: ");
							num2 = Convert.ToDouble(Console.ReadLine());
							Calculation calc1 = new Calculation();
							answer = calc1.FindMax(num1, num2);
							Console.WriteLine("The maximum of {0} and {1} is {2}.", num1, num2, answer);
							Console.ReadLine();
							break;
						case 2:
							Console.WriteLine("Enter first number: ");
							num1 = Convert.ToDouble(Console.ReadLine());
							Console.WriteLine("Enter second number: ");
							num2 = Convert.ToDouble(Console.ReadLine());
							Calculation calc2 = new Calculation();
							answer = calc2.FindMin(num1, num2);
							Console.WriteLine("The minimum of {0} and {1} is {2}.", num1, num2, answer);
							Console.ReadLine();
							break;
						case 3:
							Console.WriteLine("Enter a number: ");
							num3 = Convert.ToInt32(Console.ReadLine());
							Calculation calc3 = new Calculation();
							intAnswer = calc3.FindFactorial(num3);
							Console.WriteLine("The factorial for {0} is {1}.", num3, intAnswer);
							Console.ReadLine();
							break;
						default:
							break;
					}
				}
			}
		}
	}
}