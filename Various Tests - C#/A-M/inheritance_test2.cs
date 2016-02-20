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

	// Base class PaintCost
	public interface PaintCost
	{
		int getCost(int area);
	}

	// Derived (Child) Class
	class Rectangle : Shape, PaintCost
	{
		public int getArea()
		{
			return width * height;
		}
		public int getCost(int area)
		{
			return area * 70;
		}
	}

	class RectangleTest
	{
		static void Main(string[] args)
		{
			Rectangle Rect = new Rectangle();
			int area;
			Rect.setWidth(15);
			Rect.setHeight(10);
			area = Rect.getArea();

			Console.WriteLine("Total area:       {0}", Rect.getArea());
			Console.WriteLine("Total paint cost: {0}", Rect.getCost(area));
			Console.ReadKey();
		}
	}
}