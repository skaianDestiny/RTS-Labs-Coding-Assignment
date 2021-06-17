# Print the number of integers in an array that are above the given input and the number that are below, e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.

array = [1, 2, 5, 6, 8]

try:
	num = int(input("Enter number to compare: "))
	
	below = 0
	above = 0

	for x in array:
		if x > num:
			above += 1
		elif x < num:
			below += 1

	print("Above: " + str(above) + "\nBelow: " + str(below))
except TypeError:
	print("Not a valid number")
