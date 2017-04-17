import random
import math
from heap import MaxHeap

max_iter = 25000
n = 100
largest = 10 ** 12

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

# HELPER FUNCTIONS
    
# Generate a random solution
def gen_rand_sol():
  rand_lst = []
  for i in range (0, n):
    sign = random.randint(0,1)
    if sign == 0: 
      sign -= 1
    rand_lst.append(sign)
  return rand_lst

# Returns the residue of a partion solution S for an array A
def residue(sol, A):      
  return abs(sum([a * s for a,s in zip (A, sol)]))
  
# Generate a random list A for testing
def rand_lst():
  lst = []
  for i in range(0,n):
    lst.append(random.randint(0, largest))
  return lst
  
# Repeated random
def repeated_random():
  A = rand_lst()
  S = gen_rand_sol()
  for i in range(0, max_iter):
    _S = gen_rand_sol()
    if (residue(_S, A) < residue(S, A)):
      S = _S
  return S

def diff(A,B):
  for i in range(0, len(A)):
    if (A[i] != B[i]):
      print "diff"

# Generates a random neighbor of S 
def rand_neighbor(S):
  _S = S[:]
  i = 0
  j = 0
  while (i == j):
      i = random.randint(0, 99)
      j = random.randint(0, 99)
  pr_swap = random.randint(0,1)
  _S[i] = -_S[i]
  if pr_swap == 1:
    _S[j] = -_S[j]
  return _S
  
# Hill Climbing 
def hill_climbing():
  A = rand_lst()
  S = gen_rand_sol()
  for i in range(0, max_iter):
    _S = rand_neighbor(S)
    if (residue(_S, A) < residue(S, A)):
      S = _S
  return S

tenten = 10 ** 10
def T(iter):
  return float(tenten)*0.8**(math.floor(float(iter)/300.))

# Simulated Annealing
def simulated_annealing():
  A = rand_lst()
  S = gen_rand_sol()
  b = S
  best = S
  for i in range(0, max_iter):
    _S = rand_neighbor(S)
    r1 = residue(S, A)
    r2 = residue(_S, A)
    if r2 < r1:
      S = _S
    else:
      r = -1 * (r2-r1)
      n = math.exp(r/T(i))
      if n >= random.uniform(0,1):
        S = _S
    if residue(S, A) < residue(best, A):
      best = S
  return best 




