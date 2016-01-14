using System;
namespace ArithmeticOps
{
	class ArithmeticOps
	{
		public static string boolCheck(bool tmpBool) {
			switch(tmpBool)
			{
				case true:
					return "\t\t";
				case false:
					return "\t";
				default:
					break;
			}
			return "Error!";
		}

		static void Main(string[] args)
		{
			int a,b;
			Console.WriteLine("Please enter an integer for (A): ");
			a = Convert.ToInt32(Console.ReadLine());
			Console.WriteLine("Please enter another integer (B): ");
			b = Convert.ToInt32(Console.ReadLine());

			// Arithmetic Operator Examples
			Console.WriteLine("|---------------------------------------|");
			Console.WriteLine("|     Arithmetic Operator Examples      |");
			Console.WriteLine("|---------------------------------------|");
			Console.WriteLine("|  Operator  ||         Example         |");
			Console.WriteLine("|------------||-------------------------|");
			Console.WriteLine("|      +     ||  A + B = {0}\t\t|", a+b);
			Console.WriteLine("|      -     ||  A - B = {0}\t\t|", a-b);
			Console.WriteLine("|      *     ||  A * B = {0}\t\t|", a*b);
			Console.WriteLine("|      /     ||  A / B = {0}\t\t|", a/b);
			Console.WriteLine("|      %     ||  A % B = {0}\t\t|", a%b);
			Console.WriteLine("|      ++    ||  A++ = {0}\t\t|", ++a);
			Console.WriteLine("|      --    ||  B-- = {0}\t\t|", --b);
			Console.WriteLine("|---------------------------------------|\n");

			// Relational Operator Examples
			bool tmpBool;
			Console.WriteLine("|---------------------------------------|");
			Console.WriteLine("|     Relational Operator Examples      |");
			Console.WriteLine("|---------------------------------------|");
			Console.WriteLine("|  Operator  ||         Example         |");
			Console.WriteLine("|------------||-------------------------|");
			tmpBool = (a==b);
			Console.WriteLine("|      ==    ||  A == B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (a!=b);
			Console.WriteLine("|      !=    ||  A != B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (a>b);
			Console.WriteLine("|      >     ||  A >  B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (a<b);
			Console.WriteLine("|      <     ||  A <  B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (a>=b);
			Console.WriteLine("|      >=    ||  A >= B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (a<=b);
			Console.WriteLine("|      <=    ||  A <= B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			Console.WriteLine("|---------------------------------------|\n");

			// Attain new round of variables (true or false)
			int c,d;
			bool cbool, dbool;
			Console.WriteLine("Please choose true (1) or false (0): ");
			c = Convert.ToInt32(Console.ReadLine());
			Console.WriteLine("Again, please choose true (1) or false (0): ");
			d = Convert.ToInt32(Console.ReadLine());

			// Workaround for C# implicit bool representations
			cbool = c==1 ? true : false;
			dbool = d==1 ? true : false;

			// Logical Operator Examples
			Console.WriteLine("|---------------------------------------|");
			Console.WriteLine("|        Logical Operator Examples      |");
			Console.WriteLine("|---------------------------------------|");
			Console.WriteLine("|  Operator  ||         Example         |");
			Console.WriteLine("|------------||-------------------------|");
			tmpBool = (cbool&&dbool);
			Console.WriteLine("|      &&    ||  A && B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (cbool||dbool);
			Console.WriteLine("|      ||    ||  A || B is {0}{1}|", tmpBool, boolCheck(tmpBool));
			tmpBool = (!(cbool&&dbool));
			Console.WriteLine("|      !     ||  !(A&&B) is {0}\t|", tmpBool);
			Console.WriteLine("|---------------------------------------|");
			Console.ReadLine();
		}
	}
}