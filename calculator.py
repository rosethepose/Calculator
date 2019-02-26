play = True
while play:
	op = input("Choose your operation:\na) addition\nb) subtraction\nc) multiplication\nd) division\n >>")
	op = op.rstrip()

	if op != "a" and op != "b" and op != "c" and op != "d" :
		print("Error!")
		again = input("\n\n Would you like to go again? (yes or no): ")
		again = again.rstrip()

		if again == "yes":
			continue
		elif again != "no":
			print("Error!")
			again = input("\n\n Would you like to go again? (yes or no): ")
			again = again.rstrip()
			if again == "yes":
				continue
			else:
				print("Bye!")
				break
		else:
			print("Bye!")
			break

	num1 = input("\nNumber 1: ")
	num1 = num1.rstrip()
	if num1.isnumeric():
		num1 = int(num1)
	else:
		print("Error!")
		num1 = input("\nNumber 1: ")
		num1 = num1.rstrip()
		num1 = int(num1)

	num2 = input("\nNumber 2: ")
	num2 = num2.rstrip()
	if num2.isnumeric():
		num2 = int(num2)
	else:
		print("Error!")
		num2 = input("\nNumber 2: ")
		num2 = num2.rstrip()
		num2 = int(num2)

	

	if op == "a":
		answer = num1 + num2
	elif op == "b":
		answer = num1 - num2
	elif op == "c":
		answer = num1 * num2
	else:
		answer = num1 / num2

	print("Your answer is " + str(answer))
	again = input("\n\n Would you like to go again? (yes or no): ")
	again = again.rstrip()

	if again == "yes":
		continue
	elif again != "no":

		print("Error!")
		again = input("\n\n Would you like to go again? (yes or no): ")
		again = again.rstrip()
		if again == "yes":
			continue
		else:
			print("Bye!")
			break
	else:
		print("Bye!")
		break
	
 
