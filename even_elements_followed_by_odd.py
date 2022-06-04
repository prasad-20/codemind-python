n=int(input())
lst=list(map(int,input().split()))
x=[]
y=[]
for i in lst:
    if i%2==0:
        x.append(i)
    elif i%2==1:
        y.append(i)
print(*x+y)
