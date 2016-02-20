using System;
namespace OperatorOverloadApplication
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

		// Overload "+" operator to combine two Box objects
		public static Box operator+ (Box b, Box c)
		{
			Box box = new Box();
			box.length = b.length + c.length;
			box.breadth = b.breadth + c.breadth;
			box.height = b.height + c.height;
			return box;
		}

		public static bool operator == (Box lhs, Box rhs)
		{
			bool status = false;
			if(lhs.length == rhs.length && lhs.height == rhs.height && lhs.breadth == rhs.breadth)
			{
				status = true;
			}
			return status;
		}

		public static bool operator != (Box lhs, Box rhs)
		{
			bool status = false;
			if(lhs.length != rhs.length || lhs.height != rhs.height || lhs.breadth != rhs.breadth)
			{
				status = true;
			}
			return status;
		}

		public static bool operator < (Box lhs, Box rhs)
		{
			bool status = false;
			if(lhs.length < rhs.length && lhs.height < rhs.height && lhs.breadth < rhs.breadth)
			{
				status = true;
			}
			return status;
		}

		public static bool operator > (Box lhs, Box rhs)
		{
			bool status = false;
			if(lhs.length > rhs.length && lhs.height > rhs.height && lhs.breadth > rhs.breadth)
			{
				status = true;
			}
			return status;
		}

		public static bool operator <= (Box lhs, Box rhs)
		{
			bool status = false;
			if(lhs.length <= rhs.length && lhs.height <= rhs.height && lhs.breadth <= rhs.breadth)
			{
				status = true;
			}
			return status;
		}

		public static bool operator >= (Box lhs, Box rhs)
		{
			bool status = false;
			if(lhs.length >= rhs.length && lhs.height >= rhs.height && lhs.breadth >= rhs.breadth)
			{
				status = true;
			}
			return status;
		}

		public override string ToString()
		{
			return String.Format("({0}, {1}, {2})", length, breadth, height);
		}
	}

	class BoxTest
	{
		static void Main(string[] args)
		{
			Box box1 = new Box();
			Box box2 = new Box();
			Box box3 = new Box();
			Box box4 = new Box();
			double volume = 0.0;

			// Setting box 1 values
			box1.setLength(10.2);
			box1.setBreadth(8.3);
			box1.setHeight(2.7);

			// Setting box 2 values
			box2.setLength(6.5);
			box2.setBreadth(9.9);
			box2.setHeight(5.0);

			Console.WriteLine("Box 1: {0}", box1.ToString());
			Console.WriteLine("Box 2: {0}", box2.ToString());

			/* Console.WriteLine("Box 1: {0}", box1);
			Console.WriteLine("Box 2: {0}", box2);
			Console.WriteLine("Box 3: {0}", box3);
			Console.WriteLine("Box 4: {0}", box4); */

			// Calculate and show each box's volumes
			volume = box1.getVolume();
			Console.WriteLine("Volume of Box 1: {0}", volume);
			volume = box2.getVolume();
			Console.WriteLine("Volume of Box 2: {0}", volume);

			// Combine both Box objects
			box3 = box1 + box2;
			Console.WriteLine("Box 3: {0}", box3.ToString());

			// Calculate and show box 3's volume
			volume = box3.getVolume();
			Console.WriteLine("Volume of Box 3: {0}", volume);

			// Compare the boxes
			if(box1.getVolume() > box2.getVolume())
				Console.WriteLine("Box 1 is greater than Box 2");
			else
				Console.WriteLine("Box 1 is not greater than Box 2");

			if(box1.getVolume() < box2.getVolume())
				Console.WriteLine("Box 1 is less than Box 2");
			else
				Console.WriteLine("Box 1 is not less than Box 2");

			if(box1.getVolume() >= box2.getVolume())
				Console.WriteLine("Box 1 is greater or equal to Box 2");
			else
				Console.WriteLine("Box 1 is not greater or equal to than Box 2");

			if(box1.getVolume() <= box2.getVolume())
				Console.WriteLine("Box 1 is less or equal to Box 2");
			else
				Console.WriteLine("Box 1 is not less or equal to Box 2");

			if(box1.getVolume() != box2.getVolume())
				Console.WriteLine("Box 1 is not equal to Box 2");
			else
				Console.WriteLine("Box 1 is not greater or equal to Box 2");

			box4 = box3;

			if(box3.getVolume() == box4.getVolume())
				Console.WriteLine("Box 3 is equal to Box 4");
			else
				Console.WriteLine("Box 3 is not equal to Box 4");

			Console.ReadKey();
		}
	}
}