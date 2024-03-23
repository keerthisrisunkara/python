# calculate the sum of digits of a number 12345
n = 12345
sum = 0
while n > 0:
    a = n % 10
    sum = sum + a
    n = n//10
print(sum)
