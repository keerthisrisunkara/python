n = int(input("enter a number"))


def is_prime():
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break  # if break is not used then the output will be printed multiple times
    else:
        print("prime")


is_prime()
