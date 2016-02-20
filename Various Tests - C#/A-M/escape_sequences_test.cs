using System;
namespace EscapeSequencesApplication
{
	class EscapeSequences
	{
		static void Main(string[] args)
		{
			Console.WriteLine("Slash:             \\");
			Console.WriteLine("Apostrophe:        \'");
			Console.WriteLine("Double Apostrophe: \"");
			Console.WriteLine("Question Mark:     ?");
			Console.WriteLine("Alert or Bell:     x\ax");
			Console.WriteLine("Backspace:         x\bx");
			Console.WriteLine("Form Feed:         \f");
			Console.WriteLine("Newline:           \n");
			Console.WriteLine("Carriage Return:   \r");
			Console.WriteLine("Horizontal Tab:    \tx");
			Console.WriteLine("Vertical Tab:      \vx");
			Console.WriteLine("Octal Number:      \023");
			Console.WriteLine("Hex Number:        (Not Working)");
			Console.ReadLine();

			Console.WriteLine("hello, dear");
			Console.WriteLine("hello, "+"d"+"ear");
			Console.WriteLine(@"hello, dear");
			Console.ReadLine();
		}
	}
}