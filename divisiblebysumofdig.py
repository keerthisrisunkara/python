# wap to check if a number is divisible by its sum of digits. If yes,print "divisible" else "not divisible"
n = int(input("enter a number"))
sum = 0
n1 = n
while n > 0:
    a = n % 10
    sum = sum + a
    n = n//10
if n1 % sum == 0:
    print("divisible")
else:
    print("not divisible")
