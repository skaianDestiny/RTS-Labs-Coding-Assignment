# Rotate the characters in a string by a given input and have the overflow appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.

string = "MyString"
print("Original: " + string)

rotate = input("Enter number to rotate string by: ")

# Converts the number if it's greater than the string length to the equivalent under the length
# eg. with a string length of 5, rotating by 7 is the same as rotating by 2; 7 mod 5 = 2
r = rotate % len(string)	

s1 = string[-rotate:]
s2 = string[:-rotate]

print(s1 + "\n" + s2)

print("Rotated by " + str(rotate) + ": " + s1 + s2)