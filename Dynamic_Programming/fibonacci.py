# Given positive integers n <= 40 and k <= 5, retern the total # of pairs of rabbits present after n months if we begin with 1 pair and each generation every pair produces a litter of k pairs

# Given n = 5, k = 3 => 19


def fibonacci(n, k):
  if n == 0:
    return 0

  elif n <= 2:
    return 1

  else:
    return fibonacci(n - 1, k) + (k * (fibonacci(n - 2, k)))


print(fibonacci(6, 5))

##########################################
# Refactor using dynamic programming & compile

# memo = {}

# def fib(n,k=1):
#   args = (n,k)
#   if args in memo:
#     return memo[args]

#   if n <= 2:
#     ans = 1
#   else:
#     ans = fib(n-1, k) + k * fib(n-2, k)

#   memo[args] = ans
#   return ans

# print(fib(5,3))
