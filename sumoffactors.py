# wap to check if the sum of factors of a number is greater than the number or not.
n = int(input("enter a number"))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum = sum + i
if sum > n:
    print("greater")
else:
    print("not greater")
