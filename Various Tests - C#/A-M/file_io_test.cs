using System;
using System.IO;

namespace FileIOApplication
{
	class Program
	{
		static void Main(string[] args)
		{
			FileStream F = new FileStream("test.dat", FileMode.OpenOrCreate, FileAccess.ReadWrite);
			for(int a=1; a<=20; a++)
			{
				F.WriteByte((byte)a);
			}

			F.Position = 0;
			for(int b=0; b<=20; b++)
			{
				Console.Write(F.ReadByte() + " ");
			}
			F.Close();
			Console.ReadKey();
		}
	}
}