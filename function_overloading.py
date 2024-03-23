class arthimetic:
    def add(self, a):
        print(a)

    def ad(self, a, b):
        print(a+b)

    def add(self, a, b, c):
        print(a+b+c)


obj = arthimetic()
obj.add(10)
obj.add(10, 20)
obj.add(1, 2, 3)

# in java,the ouput will be 10,30,6
# in python, the last function will only be executed with the values of 1st class
# so, error will be displayed saying two values are missing.
