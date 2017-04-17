import random
bound = 10 ** 12
file = open('test.txt', 'w')

for i in range(100):
	n = random.randint(1, bound)
	file.write(str(n)+'\n')
file.close()

