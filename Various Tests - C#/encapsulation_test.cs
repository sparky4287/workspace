using System;
namespace EncapsulationApplication
{
	// Public example
	class Rectangle
	{
		// Member variables
		public double length;
		public double width;

		public double GetArea()
		{
			return length * width;
		}

		public void Display()
		{
			Console.WriteLine("Length: {0}", length);
			Console.WriteLine("Width: {0}", width);
			Console.WriteLine("Area: {0}", GetArea());
		}
	}

	// Private example
	class PrivateRectangle
	{
		// Member variables
		private double length;
		private double width;

		public void AcceptDetails()
		{
			Console.WriteLine("Enter length: ");
			length = Convert.ToDouble(Console.ReadLine());
			Console.WriteLine("Enter width: ");
			width = Convert.ToDouble(Console.ReadLine());
		}

		public double GetArea()
		{
			return length * width;
		}

		public void Display()
		{
			Console.WriteLine("Length: {0}", length);
			Console.WriteLine("Width: {0}", width);
			Console.WriteLine("Area: {0}", GetArea());
		}
	}

	// Internal example
	class InternalRectangle
	{
		// Member variables
		internal double length;
		internal double width;

		double GetArea()
		{
			return length * width;
		}

		public void Display()
		{
			Console.WriteLine("Length: {0}", length);
			Console.WriteLine("Width: {0}", width);
			Console.WriteLine("Area: {0}", GetArea());
		}
	}

	// Main execution
	class ExecuteRectangle
	{
		static void Main(string[] args)
		{
			// Run public example
			Rectangle rect = new Rectangle();
			rect.length = 4.56;
			rect.width = 3.24;
			rect.Display();
			Console.ReadLine();

			// Run private example
			PrivateRectangle prir = new PrivateRectangle();
			prir.AcceptDetails();
			prir.Display();
			Console.ReadLine();

			// Run internal example
			InternalRectangle intr = new InternalRectangle();
			intr.length = 7.22;
			intr.width = 2.13;
			intr.Display();
			Console.ReadLine();
		}
	}
}