#Testing how to count matches

a = [1,2,3,4,5,6]
b = [4,5,3,12,1]

numberofmatches =  len(set(a) & set(b))

distribution = [0] * 6

distribution[numberofmatches] += 1

print "MATCHES"

for index, item in enumerate(distribution):
    print index + 1, item
