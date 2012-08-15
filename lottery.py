import random

winningnumbers = [1,2,3,4,5,6]
distribution = [0] * 7

winningset = set(winningnumbers)

for i in range (1,100000):

	numbers = []

	for i in range(1,50):
		numbers.append(i)


	ticket  = []

	for i in range (1,7):
		remainingnumbers = len(numbers)

		numberindex = random.randrange(0,remainingnumbers)
		
		selectednumber = numbers[numberindex]


		del numbers[numberindex]



		ticket.append(selectednumber)

	ticket.sort()
	#print ticket	


	numberofmatchingnumbers = len(winningset & set(ticket))
	distribution[numberofmatchingnumbers] += 1

print "MATCHES"

for index, item in enumerate(distribution):
    print index, item
