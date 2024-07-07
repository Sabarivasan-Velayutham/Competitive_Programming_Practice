import numpy as np
a = []
print("Enter the number of equations involved")
eq = int(input())
if eq == 2:
    rows = 3
elif eq == 3:
    rows = 4
print("Enter matrix")
for i in range(rows):
    k = list(map(int, input().split()))
    a.append(k)
a = np.array(a, np.int32)
a = a.astype(np.float64)
flag = 0
steps = 0
while(flag == 0):
    steps += 1
    k = np.min(a[rows-1])
    # print(k)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j] == k):
                mincol = j
                break
    # print("col-",mincol)
    r = []
    r.append(a[0][-1]//a[0][mincol])
    # print("r1=",r1)
    r.append(a[1][-1]//a[1][mincol])
    # print("r2=",r2)
    if(rows == 4):
        r.append(a[2][-1]//a[2][mincol])
    m = min(r)
    for i in range(len(r)):
        if(m == r[i]):
            minrow = i
    # print("row-",minrow)
    pivot = a[minrow][mincol]
    a[minrow] = a[minrow]/pivot
    for i in range(rows):
        if(i == minrow):
            continue
        else:
            a[i] = a[i]-(a[i][mincol])*a[minrow]
    print(a)
    count = 0
    for i in range(len(a[0])):
        if(a[-1][i] < 0):
            flag = 0
            break
        else:
            count += 1
    xc = yc = zc = 0
    for i in range(rows):
        if a[i][0] == 1:
            xc += 1
        if a[i][1] == 1:
            yc += 1
        if a[i][2] == 1:
            zc += 1
    if(count == 6 and rows == 3):
        if(xc == 1):
            if(a[0][0] == 1):
                x = a[0][-1]
            elif(a[1][0] == 1):
                x = a[1][-1]
        else:
            x = 0
        if(yc == 1):
            if(a[0][1] == 1):
                y = a[0][-1]
            elif(a[1][1] == 1):
                y = a[1][-1]
        else:
            y = 0
        flag = 1
        print("Max value is", a[-1][-1], "at x=", round(x), "and y=", round(y))
    elif(count == 8 and rows == 4):
        if(xc == 1):
            if(a[0][0] == 1):
                x = a[0][-1]
            elif(a[1][0] == 1):
                x = a[1][-1]
            elif(a[2][0] == 1):
                x = a[2][-1]
        else:
            x = 0
        if(yc == 1):
            if(a[0][1] == 1):
                y = a[0][-1]
            elif(a[1][1] == 1):
                y = a[1][-1]
            elif(a[2][1] == 1):
                y = a[2][-1]
        else:
            y = 0
        if(zc == 1):
            if(a[0][2] == 1):
                z = a[0][-1]
            elif(a[1][2] == 1):
                z = a[1][-1]
            elif(a[2][2] == 1):
                z = a[2][-1]
        else:
            z = 0
        flag = 1
        print("Max value is", a[-1][-1], "at x=",
              round(x), "and y=", round(y), "and z=", round(z))
print("number of iterations- %d" % (steps))
