class F15:
    def light(self):
        print("ok switching on the lights")

    def fan(self, speed):
        print(" fan is on and the speed is", speed)
        self.s = speed

    def cpu(self):
        print("cpu is on ")
        print(self.s)


# class childclass(parentclass)
class shopping(F15):
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
keerthi.fan(5)
keerthi.light()
