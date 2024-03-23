listuu = [8, 1, 2, 5, 6, 0, 7, 8, 9, 8]
listuu.append("number")
listuu.insert(10, "phone")
print(listuu)
print(listuu[2])
print(listuu[8])
for i in range(0, len(listuu)):
    print(listuu[i])
for i in listuu:
    print(i)
print(listuu[:-2])
print(listuu[5:2:2])
print(listuu[3:])
print(listuu[4:9])
listuu[10] = "my "
print(listuu)
