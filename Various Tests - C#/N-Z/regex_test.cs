using System;
using System.Text.RegularExpressions;

namespace RegexApplication
{
	class Program
	{
		private static void showMatch(string text, string expr)
		{
			Console.WriteLine("The expression: " + expr);
			MatchCollection mc = Regex.Matches(text, expr);
			foreach(Match m in mc)
			{
				Console.WriteLine(m);
			}
		}

		static void Main(string[] args)
		{
			string str = "A Thousand Splendid Suns";

			Console.WriteLine("The string: \"{0}\"", str);
			Console.WriteLine("Matching words that start with 'S'...");
			showMatch(str, @"\bS\S*");
			Console.ReadKey();

			str = "make maze and manage to measure it";

			Console.WriteLine("The string: \"{0}\"", str);
			Console.WriteLine("Matching words that start with 'm' and end with 'e'...");
			showMatch(str, @"\bm\S*e\b");
			Console.ReadKey();

			string input = "Hello     World     ",
				pattern = "\\s+",
				replacement = " ";
			Regex rgx = new Regex(pattern);
			string result = rgx.Replace(input, replacement);

			Console.WriteLine("Original string: {0}", input);
			Console.WriteLine("Replacement string: {0}", result);
			Console.ReadKey();
		}
	}
}