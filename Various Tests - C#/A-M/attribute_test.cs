#define DEBUG
using System;
using System.Diagnostics;

public class Myclass
{
	[Conditional("DEBUG")]
	public static void Message(string msg)
	{
		Console.WriteLine(msg);
	}
}

class Test
{
	static void func1()
	{
		Myclass.Message("In func1.");
		func2();
	}
	static void func2()
	{
		Myclass.Message("In func2.");
	}
	public static void Main()
	{
		Myclass.Message("In main function.");
		func1();
		Console.ReadKey();
	}
}