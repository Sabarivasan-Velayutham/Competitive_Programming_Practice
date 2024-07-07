import matplotlib.pyplot as plt
cnt1=0
def add(a,b):
    global cnt1
    res=[]
    for i in range(len(a)):
        x=[]
        for j in range(len(a[i])):
            cnt1+=1
            x.append(a[i][j]+b[i][j])
        res.append(x) 
    return res  

def sub(a,b):
    global cnt1
    res=[]
    for i in range(len(a)):
        x=[]
        for j in range(len(a[i])):
            cnt1+=1
            x.append(a[i][j]-b[i][j])
        res.append(x)       
    return res


def mul(a,b,n):
    global cnt1
    cnt1+=1
    c=[]
    if(n==2):
        x=[]
        x.append(a[0][0]*b[0][0]+a[0][1]*b[1][0])
        x.append(a[0][0]*b[0][1]+a[0][1]*b[1][1])
        c.append(x)
        x=[]
        x.append(a[1][0]*b[0][0]+a[1][1]*b[1][0])
        x.append(a[1][0]*b[0][1]+a[1][1]*b[1][1])
        c.append(x)
    else:
        a11=[]
        a12=[]
        a21=[]
        a22=[]
        b11=[]
        b12=[]
        b21=[]
        b22=[]
        c11=[]
        c12=[]
        c21=[]
        c22=[]
        for i in range(n//2):
            a11.append(a[i][:n//2])
            a12.append(a[i][n//2:])
            a21.append(a[n//2+i][:n//2])
            a22.append(a[n//2+i][n//2:])

            b11.append(b[i][:n//2])
            b12.append(b[i][n//2:])
            b21.append(b[n//2+i][:n//2])
            b22.append(b[n//2+i][n//2:])

        p=mul(add(a11,a22),add(b11,b22),n//2)
        q=mul(add(a21,a22),b11,n//2)
        r=mul(a11,sub(b12,b22),n//2)
        s=mul(a22,sub(b21,b11),n//2)
        t=mul(add(a11,a12),b22,n//2)
        u=mul(sub(a21,a11),add(b11,b12),n//2)
        v=mul(sub(a12,a22),add(b21,b22),n//2)

        c11=add(sub(add(p,s),t),v)
        c12=add(r,t)
        c21=add(q,s)
        c22=add(sub(add(p,r),q),u)

        for i in range(n//2):
            x1=(c11[i][:])
            x2=(c12[i][:])
            c.append(x1+x2)
        for i in range(n//2):
            x1=c21[i][:]
            x2=c22[i][:]
            c.append(x1+x2)
    return c


def mul2(a,b,n):
    global cnt1
    cnt1+=1
    c=[]
    if(n==2):
        x=[]
        x.append(a[0][0]*b[0][0]+a[0][1]*b[1][0])
        x.append(a[0][0]*b[0][1]+a[0][1]*b[1][1])
        c.append(x)
        x=[]
        x.append(a[1][0]*b[0][0]+a[1][1]*b[1][0])
        x.append(a[1][0]*b[0][1]+a[1][1]*b[1][1])
        c.append(x)
    else:
        a11=[]
        a12=[]
        a21=[]
        a22=[]
        b11=[]
        b12=[]
        b21=[]
        b22=[]
        c11=[]
        c12=[]
        c21=[]
        c22=[]
        for i in range(n//2):
            a11.append(a[i][:n//2])
            a12.append(a[i][n//2:])
            a21.append(a[n//2+i][:n//2])
            a22.append(a[n//2+i][n//2:])

            b11.append(b[i][:n//2])
            b12.append(b[i][n//2:])
            b21.append(b[n//2+i][:n//2])
            b22.append(b[n//2+i][n//2:])

        c11=add(mul2(a11,b11,n//2),mul2(a12,b21,n//2))
        c12=add(mul2(a11,b12,n//2),mul2(a12,b22,n//2))
        c21=add(mul2(a21,b11,n//2),mul2(a22,b21,n//2))
        c22=add(mul2(a21,b12,n//2),mul2(a22,b22,n//2))

        for i in range(n//2):
            x1=(c11[i][:])
            x2=(c12[i][:])
            c.append(x1+x2)
        for i in range(n//2):
            x1=c21[i][:]
            x2=c22[i][:]
            c.append(x1+x2)
    return c

y=[]
y2=[]
a=[]
b=[]
n=4

cnt1=0
for i in range(n):
    x=list(map(int,input().split())) 
    a.append(x)
for i in range(n):
    x=list(map(int,input().split())) 
    b.append(x)
mul(a,b,n)
y.append(cnt1)
print("1",cnt1)
cnt1=0
mul2(a,b,n)
y2.append(cnt1)
print("2",cnt1)


cnt1=0
a=[]
b=[]
n=8
for i in range(n):
    x=list(map(int,input().split())) 
    a.append(x)
for i in range(n):
    x=list(map(int,input().split())) 
    b.append(x)
mul(a,b,n)
y.append(cnt1)
print("1",cnt1)
cnt1=0
mul2(a,b,n)
y2.append(cnt1)
print("2",cnt1)


cnt1=0
a=[]
b=[]
n=16
for i in range(n):
    x=list(map(int,input().split())) 
    a.append(x)
for i in range(n):
    x=list(map(int,input().split())) 
    b.append(x)
mul(a,b,n)
y.append(cnt1)
print("1",cnt1)
cnt1=0
print
mul2(a,b,n)
y2.append(cnt1)
print("2",cnt1)

plt.plot([4,8,16],y)
plt.plot([4,8,16],y2)

plt.xlabel("n")
plt.ylabel("No.of operations")
plt.show()

