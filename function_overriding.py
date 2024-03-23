class father:
    def bike(self):
        print("harley devidson")

    def laptop(self):
        print("laptop with 2 gb ram")


class kiki(father):
    def laptop(self):
        print("laptop with 8 gb ram")


obj = kiki()
obj.bike()
obj.laptop()  # laptop function will be overriden.
