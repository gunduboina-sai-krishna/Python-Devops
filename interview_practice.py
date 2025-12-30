#1. Is prime

# def is_prime(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     i=3
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 2 

#     return True    

# print(is_prime(n))

#  # print prime numbers from a range
# for i in range(1, 20):
#     if is_prime(i):
#         print(i)


#2 fabonocci

# n=10

# a, b = 0, 1

# for _ in range(n):
#     print(a, end=" ")  # end will give a space after every iteration prints the output in single line, we can pass like "\n" for new line.
#     a, b = b, a + b
    
 #3. Sum of digits

n = 1234

sum = 0

while n > 0:
    sum += n % 10
    n //= 10
print(sum)    

#4. factorial 

n = 5 
factorial = 1

for i in range(1, n+1):
    factorial *= i
print(factorial)    