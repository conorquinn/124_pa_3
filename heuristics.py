import random
max_iter = 25000
 
# HELPER FUNCTIONS
    
# Generate a random solution
def gen_rand_sol():
  rand_lst = []
  for i in range (0, 100):
    sign = random.randint(0,1)
    if sign == 0: 
      sign -= 1
    rand_lst.append(sign)
  return rand_lst

# Returns the residue of a partion solution S for an array A
def residue(S, A):
  sum1 = 0
  sum2 = 0
  for i in range(0, len(A)):
    if (S[i] == 1):
      sum1 += A[i]
    else:
      sum2 += A[i]
      
  return abs(sum1 - sum2)
  
# Generate a random list A for testing
def rand_lst():
  lst = []
  for i in range(0,100):
    lst.append(random.randint(0, 10000))
  return lst
  
# Repeated random
def repeated_random():
  A = rand_lst()
  S = gen_rand_sol()
  for i in range(1, max_iter):
    _S = gen_rand_sol()
    if (residue(_S, A) < residue(S, A)):
      S = _S
  return S
  
print repeated_random();
