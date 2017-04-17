import sys
from standard import kkarp
from standard import gen_rand_sol as gen_standard
from standard import repeated_random as rr_standard
from standard import hill_climbing as hc_standard
from standard import simulated_annealing as sa_standard

# Read in numbers from input file and store in an array
fileName = sys.argv[1]
inFile = open(fileName)
A = []
for line in inFile:
	A.append(int(line))
inFile.close()

# Run Karmarkar Karp on input file numbers
k1 = kkarp(A)
print "Residue of input file numbers: ", k1

# Run 100 isntances of KK and three algorithms
for i in range(100):
	P = gen_standard()
	rr  = rr_standard(P)
	# hc = hc_standard(P)
	# sa = sa_standard(P)


