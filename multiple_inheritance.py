class parent1:
    math = int(input("enter math marks"))


class parent2:
    phy = int(input("enter phy marks"))

# class childname(parent1,parent2)


class child(parent1, parent2):
    def total(self):
        if self.math >= 40 and self.phy >= 40:
            print("pass")
        else:
            print("fail")


obj1 = child()
obj1.total()
