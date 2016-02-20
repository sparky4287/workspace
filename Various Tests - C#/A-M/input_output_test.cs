using System;
namespace InputOutputApplication
{
	class InputOutput
	{
		static void Main(string[] args)
		{
			int num;
			Console.WriteLine("Please input a number: ");
			num = Convert.ToInt32(Console.ReadLine());

			Console.WriteLine("You inputted the number: {0}", num);
			Console.ReadLine();
		}
	}
}