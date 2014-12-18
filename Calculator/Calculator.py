def get_operator(text):
	answer = ""
	for i in range(len(text)):
		if text[i].lower not in ["a","e","i","o","u"]:
			anti_text += text[i]
	print anti_text
	return anti_text

var = raw_input("Enter the string: ")
anti_vowel(var)
print var
