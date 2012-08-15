import random

winners = 0

for i in range (1,10000000):

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

	if ticket == [1,2,3,4,5,6]:
		winners += 1

print "Number of winners: %d" % winners


