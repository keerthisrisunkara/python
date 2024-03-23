mytuple = ("hi", 2, "k", 13.3, False)
print(type(mytuple))
mytuple = mytuple + ("hello",)
print(mytuple)
mytuple = mytuple + (1, 2, 3)
print(mytuple)
# adding sequence of numbers to tuple
for i in range(0, 5):
    n = int(input("enter"))
    mytuple = mytuple + (n,)
