#include <iostream>
#include <string>
#include <istream>
#include <iomanip>
#include <math.h>
using namespace std;

/* Initial User Calculation Input (returns full string of input) */
string inputString(){
	string phrase;
	cout << "Please enter a string for calculation. Include two numbers and a mathematical operator: ";
	cin >> phrase;
	return phrase;
}

/* Finds the operator being used in the string (returns string of a single operator) */
string findOperator(string phrase){
	string answer;
	string::size_type add = phrase.find("+", 0);
	string::size_type sub = phrase.find("-", 0);
	string::size_type mul = phrase.find("*", 0);
	string::size_type div = phrase.find("/", 0);

	if(add != std::string::npos) {
		answer = "+";
	}
	if(sub != std::string::npos) {
		answer = "-";
	}
	if(mul != std::string::npos) {
		answer = "*";
	}
	if(div != std::string::npos) {
		answer = "/";
	}
	return answer;
}

int main() {

		/* Input Calculation */
		string phrase = inputString();

		/* Find Operator */
		string op = findOperator(phrase);

		/* Find Numbers */
		std::string::size_type sz;   // alias of size_t

		//int num1 = std::stoi (phrase,&sz);

		//cout << num1 << endl;

		//double num1 = Double.parseDouble(phrase.substring(0,phrase.indexOf(operator)));
		//double num2 = Double.parseDouble(phrase.substring(phrase.indexOf(operator)+1));

		/* Calculate Answer */
		//string answer = findAnswer(num1,num2,op);
		//cout << answer;
	//}
	return(0);
}
