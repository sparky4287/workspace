using System;
namespace BoxApplication
{
	class Box
	{
		private double length;
		private double breadth;
		private double height;
		
		public void setLength(double l)
		{
			length = l;
		}

		public void setBreadth(double b)
		{
			breadth = b;
		}

		public void setHeight(double h)
		{
			height = h;
		}

		public double getVolume()
		{
			return length * breadth * height;
		}
	}

	class BoxTest
	{
		static void Main(string[] args)
		{
			Box Box1 = new Box();
			Box Box2 = new Box();
			double volume;

			Box1.setLength(3.3);
			Box1.setBreadth(3.7);
			Box1.setHeight(4.2);

			Box2.setLength(5.4);
			Box2.setBreadth(1.2);
			Box2.setHeight(4.9);

			volume = Box1.getVolume();
			Console.WriteLine("Volume of box 1: {0}", volume);

			volume = Box2.getVolume();
			Console.WriteLine("Volume of box 2: {0}", volume);

			Console.ReadKey();
		}
	}
}