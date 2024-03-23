# #class classname:
#   features
class F15:
    def light(self):
        print("ok switching on the lights")

    def fan(self, speed):
        print(" fan is on and the speed is", speed)
        self.s = speed

    def cpu(self):
        print("cpu is on ")
        print(self.s)


#objectname= classname()
chandu = F15()
# objectname.functionname()
chandu.light()
chandu.fan(5)
chandu.cpu()
