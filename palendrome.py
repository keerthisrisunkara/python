# check a number palendrome or not
n = int(input("enter a number"))
n1 = n
sum = 0
while n > 0:
    a = n % 10
    sum = sum*10+a
    n = n//10
if sum == n1:
    print("palendrome")
else:
    print("not palendrome")
