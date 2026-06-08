try:
	n = int(input("Enter number: "))

	for i in range(1, n+1):
		print(i,end="")
	print("")
except ValueError:
	print("Please enter a whole number")
