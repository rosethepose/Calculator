eq = input("Enter your equation in RPN notation: ")
eq = eq.rstrip()
myList = eq.split(' ')
count = len(myList)
a = 0
for x in range(a, count):
	if myList[0].isnumeric():
		num = int(myList[0])
		myList.append(num)
		myList.pop(0)
		a = 0
	elif myList[0] == '+':
		myList.append(myList.pop() + myList.pop())
		myList.pop(0)
	elif myList[0] == '-':
		first = myList.pop()
		second = myList.pop()
		myList.append(second - first)
		myList.pop(0)
	elif myList[0] == '*':
		myList.append(myList.pop() * myList.pop())
		myList.pop(0)
	elif myList[0] == '/':
		first = myList.pop()
		second = myList.pop()
		myList.append(second / first)
		myList.pop(0)
	else:
		print("Error!")

print(myList[0])