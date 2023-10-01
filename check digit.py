import string

def check(value):
	for letter in value:
		
		if letter not in string.digits:
			return False
	return True

input1 = "0123 456 789"
print(input1, "--> ", check(input1))
	
input2 = "12.0124"
print(input2, "--> ", check(input2))
	
input3 = "12345"
print(input3, "--> ", check(input3))
