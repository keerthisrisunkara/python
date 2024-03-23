row=int(input("enter num of rows"))
col= int(input("enter num of columns"))
for i in range(1,5):
    for j in range(1,5):
        if i==  or i==4 or j==1 or j==4:
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()