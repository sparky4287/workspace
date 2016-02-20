using System;
namespace EnumApplication
{
	class EnumProgram
	{
		enum Days {
			Sun,
			Mon,
			Tues,
			Wed,
			Thurs,
			Fri,
			Sat
		};

		static void Main()
		{
			int WeekdayStart = (int)Days.Mon,
				WeekdayEnd = (int)Days.Fri;

			Console.WriteLine("Monday: {0}", WeekdayStart);
			Console.WriteLine("Friday: {0}", WeekdayEnd);

			Console.ReadKey();
		}
	}
}