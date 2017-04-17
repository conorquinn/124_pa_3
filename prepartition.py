import random
import math
from heap import MaxHeap

max_iter = 25000
n = 100
largest = 10 ** 12

def residue(S, A):
	l = len(S)
	_a = [0] * l
	for i in range(l):
		_a[S[i]-1] += A[i]
	sol = kkarp(_a)
	return sol

def gen_rand_sol(l):
	sol = []
	for i in range(l):
		sol.append(random.randint(0, l))
	return sol

# Generate a random list A for testing
def rand_lst():
  lst = []
  for i in range(0,n):
    lst.append(random.randint(0, largest))
  return lst
  

def rand_neighbor(S):
	_S = S[:]
	lim = len(S)
	while(1):
		i = random.randint(1, lim) - 1
		j = random.randint(1, lim) 
		if (_S[i] != j):
			_S[i] = j
			break
	return _S


def kkarp(A):
  maxh = MaxHeap()
  for n in A:
      maxh.heappush(n)
  n1 = maxh.heappop()
  n2 = maxh.heappop()
  while n2 > 0:
    diff = n1 - n2
    maxh.heappush(diff)
    maxh.heappush(0)
    n1 = maxh.heappop()
    n2 = maxh.heappop()
  return n1

# Repeated random
def repeated_random():
  A = rand_lst()
  S = kkarp(_A(gen_rand_sol(n)))
  for i in range(0, max_iter):
    _S = kkarp(_A(gen_rand_sol(n)))
    if (residue(_S, A) < residue(S, A)):
      S = _S
  return residue(S, A)

 # Hill Climbing 
def hill_climbing():
  A = rand_lst()
  r1 = gen_rand_sol(n)
  S = kkarp(_A(r1))
  for i in range(0, max_iter):
    r2 = rand_neighbor(r1)
    _S = kkarp(_A(r2))
    if (residue(_S, A) < residue(S, A)):
      S = _S
      r1 = r2
  return residue(S, A)

tenten = 10 ** 10
def T(iter):
  return float(tenten)*0.8**(math.floor(float(iter)/300.))

# Simulated Annealing
def simulated_annealing(A):
  S = gen_rand_sol(n)
  best = S
  for i in range(0, max_iter):
	_S = rand_neighbor(S)
	if residue(_S, A) < residue(S, A):
		S = _S
	else:
		r = -1 * (residue(_S, A)-residue(S, A))
		p = math.exp(r/T(i))
    	if p >= random.uniform(0,1):
			S = _S
	if residue(S, A) < residue(best, A):
		best = S
  return residue(best, A) 

print simulated_annealing()
