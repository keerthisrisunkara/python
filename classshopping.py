class shopping:
    def dresstype(self, typeofdress):
        self.a = typeofdress

    def price(self, priceofdress):
        self.b = priceofdress

    def size(self, sizeofdress):
        self.c = sizeofdress
    def display(self):
        print(self.a)
        print(self.b)
        print(self.c)


keerthi = shopping()
keerthi.dresstype("skirt")
keerthi.price(1000)
keerthi.size("medium")
keerthi.display()
