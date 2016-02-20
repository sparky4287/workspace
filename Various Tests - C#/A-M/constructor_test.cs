using System;
namespace LineApplication
{
	class Line
	{
		// Line length
		private double length;

		// Constructor (parameterized)
		public Line(double l)
		{
			Console.WriteLine("Line object is being created with length = {0}.", l);
			length = l;
		}

		// Destructor
		~Line()
		{
			Console.WriteLine("Line object is being deleted.");
		}

		public void setLength(double l)
		{
			length = l;
		}

		public double getLength()
		{
			return length;
		}

		static void Main(string[] args)
		{
			Line line = new Line(3.2);
			Console.WriteLine("Length of line: {0}", line.getLength());

			line.setLength(7.3);
			Console.WriteLine("Length of line: {0}", line.getLength());
			Console.ReadKey();
		}
	}
}