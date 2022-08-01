def checkGreater(number):
	original = [1, 2, 3, 4, 5]
	original.sort()
	if number > original[-1]:
		print("Yes, the entered number is greater than the numbers in the list.")
	else:
		print("No, the entered number is not greater than the numbers in the list.")

if __name__=='__main__':
	userInput = int(input("Enter the number to check: "))
	checkGreater(userInput)