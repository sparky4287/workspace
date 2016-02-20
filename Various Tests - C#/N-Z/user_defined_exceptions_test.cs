using System;

public class TempIsZeroException: Exception
{
	public TempIsZeroException(string message): base(message)
	{ }
}

public class Temperature
{
	int temperature = 0;

	public void showTemp()
	{
		if(temperature == 0)
			throw(new TempIsZeroException("Zero temperature found"));
		else
			Console.WriteLine("Temperature: {0}", temperature);
	}
}

namespace UserDefinedException
{
	class TestTemperature
	{
		static void Main(string[] args)
		{
			Temperature temp = new Temperature();
			try
			{
				temp.showTemp();
			}
			catch(TempIsZeroException e)
			{
				Console.WriteLine("TempIsZeroException: {0}", e.Message);
			}
			Console.ReadKey();
		}
	}
}