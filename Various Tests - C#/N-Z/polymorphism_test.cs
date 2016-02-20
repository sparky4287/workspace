using System;
namespace PolymorphismApplication
{
	class PrintData
	{
		void print(int i)
		{
			Console.WriteLine("Printing int: {0}", i);
		}
		void print(double d)
		{
			Console.WriteLine("Printing double: {0}", d);
		}
		void print(string s)
		{
			Console.WriteLine("Printing string: {0}", s);
		}

		static void Main(string[] args)
		{
			PrintData p = new PrintData();

			p.print(5);
			p.print(5.23);
			p.print("Hello world!");
			Console.ReadKey();
		}
	}
}