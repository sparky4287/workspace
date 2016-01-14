using System;
namespace InheritanceApplication
{
	class Shape
	{
		protected int width;
		protected int height;

		public void setWidth(int w)
		{
			width = w;
		}

		public void setHeight(int h)
		{
			height = h;
		}
	}

	class Rectangle : Shape
	{
		public int getArea()
		{
			return width * height;
		}
	}

	class RectangleTest
	{
		static void Main(string[] args)
		{
			Rectangle Rect = new Rectangle();

			Rect.setWidth(9);
			Rect.setHeight(6);

			Console.WriteLine("Total area: {0}", Rect.getArea());
			Console.ReadKey();
		}
	}
}