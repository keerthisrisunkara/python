n = int(input("enter a number"))


def is_prime():
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count = count+1
    if count > 2:
        print("not prime")
    else:
        print("prime")


is_prime()
