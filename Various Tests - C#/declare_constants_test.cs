using System;
namespace DeclaringConstants
{
    class DeclareConstant
    {
        static void Main(string[] args)
        {
            const double pi = 3.14159;

            double r;
            Console.WriteLine("Please enter a radius: ");
            r = Convert.ToDouble(Console.ReadLine());
            double area = pi * r * r;
            Console.WriteLine("Radius: {0}\nArea: {1}", r, area);
            Console.ReadLine();
        }
    }
}