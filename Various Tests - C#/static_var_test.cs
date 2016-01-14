using System;
namespace StaticVarApplication
{
	class StaticVar
	{
		// Declare static int, num
		public static int num;

		// Method increases num by 1 each invocation
		public void count()
		{
			num++;
		}

		// Retrieve num (static methods can only access static variables)
		public static int getNum()
		{
			return num;
		}
	}

	class StaticTest
	{
		static void Main(string[] args)
		{
			// Create two instances of the StaticVar class
			StaticVar s1 = new StaticVar();
			StaticVar s2 = new StaticVar();

			// Count method is invoked by both instances on the same static variable, thus incrementing num 6 times
			s1.count();
			s1.count();
			s1.count();
			s2.count();
			s2.count();
			s2.count();

			// Display results. Notice both answers draw from the single static var, num, so they are the same
			// Console.WriteLine("Variable num for s1 instance: {0}.", s1.getNum());
			// Console.WriteLine("Variable num for s2 instance: {0}.", s2.getNum());

			// Display results
			// Notice that you must retrieve the variable, num, by type rather than the instance name
			Console.WriteLine("Variable num: {0}.", StaticVar.getNum());
			Console.ReadKey();
		}
	}
}