import random

numbers = []

for i in range(1,50):
	numbers.append(i)
print numbers


ticket  = []

for i in range (1,7):
	remainingnumbers = len(numbers)

	selectednumber = random.randrange(1,remainingnumbers)
	numberindex = numbers.index(selectednumber)

	del numbers[i]



	ticket.append(selectednumber)

ticket.sort()
print ticket	



