import random
import math
from heap import MaxHeap

max_iter = 25000
n = 100
largest = 10 ** 12

def gen_rand_sol(l):
	sol = []
	for i in range(0,l):
		sol.append(random.randint(0, l))
	return sol

def _A(sol):
	_a = [0] * len(sol)
	for i in range(0,len(sol)):
		_a[sol[i]] = _a[sol[i]] + sol[i]
	return _a

def rand_neighbor(S):
	lim = len(S)
	while(1):
		i = random.randint(1, lim)
		j = random.randint(1, lim)
		if (S[i] != j):
			S[i] = j
			break
	return S


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
  return S

 # Hill Climbing 
def hill_climbing():
  A = rand_lst()
  S = kkarp(_A(gen_rand_sol(n)))
  for i in range(0, max_iter):
    _S = rand_neighbor(S)
    if (residue(_S, A) < residue(S, A)):
      S = _S
  return S