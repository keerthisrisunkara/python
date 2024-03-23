class grandparent:
    def body(self):
        print("fat")


class parent(grandparent):
    def iris(self):
        print("brown")


class child(parent):
    def hair(self):
        print("black")


obj3 = child()

obj3.body()
obj3.hair()
obj3.iris()
