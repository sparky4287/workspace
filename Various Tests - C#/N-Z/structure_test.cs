using System;
namespace StructureApplication
{
	struct Books
	{
		private string title;
		private string author;
		private string subject;
		private int book_id;

		public void getValues(string t, string a, string s, int id)
		{
			title = t;
			author = a;
			subject = s;
			book_id = id;
		}

		public void display()
		{
			Console.WriteLine("Title:   {0}", title);
			Console.WriteLine("Author:  {0}", author);
			Console.WriteLine("Subject: {0}", subject);
			Console.WriteLine("Book ID: {0}\n", book_id);
		}
	};

	public class testStructure
	{
		public static void Main(string[] args)
		{
			// Book declarations
			Books Book1 = new Books();
			Books Book2 = new Books();

			// Book 1 attributes
			Book1.getValues("How to Not Be An Idiot", "Simon Pegg", "Humorous Self-Analyzation", 65698722);

			// Book 2 attributes
			Book2.getValues("Why Simon Pegg is An Idiot", "Nick Frost", "Humerous Observations of Others", 21224498);

			// Book 1 display
			Book1.display();

			// Book 2 display
			Book2.display();

			Console.ReadKey();
		}
	}
}