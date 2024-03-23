mylist = [42, 36, 28, 96, 4, -1, 1]
mini = 999
maxi = -999
for i in range(0, len(mylist)):
    if mylist[i] < mini:
        mini = mylist[i]
    if mylist[i] > maxi:
        maxi = mylist[i]
print(mini+maxi)
