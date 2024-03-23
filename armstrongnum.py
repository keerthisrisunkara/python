#  calculate the sum of digits of a number where each digit is powered to total number of digits
#  if the sum is equals to the original number,print "yes" otherwise "no"
n = int(input("enter a number"))
count = 0
sum = 0
n1 = n
n2 = n
while n > 0:
    n = n//10
    count = count+1
while n1 > 0:
    a = n1 % 10
    a1 = a**count
    sum = sum + a1
    n1 = n1//10
if sum == n2:
    print("yes")
else:
    print("no")
