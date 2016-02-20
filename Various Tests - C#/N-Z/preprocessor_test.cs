#define PI
#define DEBUG
#define VC_V10
using System;
namespace PreprocessorApplication
{
	class PreProcProgram
	{
		static void Main(string[] args)
		{
			#if(PI)
			{
				Console.WriteLine("Pi is defined");
				#if(DEBUG && !VC_V10)
					Console.WriteLine("DEBUG is defined");
				#elif(!DEBUG && VC_V10)
					Console.WriteLine("VC_V10 is defined");
				#elif(DEBUG && VC_V10)
					Console.WriteLine("DEBUG and VC_V10 are defined");
				#else
					Console.WriteLine("Neither DEBUG nor VC_V10 are defined");
				#endif
			}
			#else
				Console.WriteLine("Pi is not defined");
			#endif
			Console.ReadKey();
		}
	}
}