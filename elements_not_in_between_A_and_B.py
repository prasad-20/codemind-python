n=int(input())
lst=list(map(int,input().split()))
n,m=map(int,input().split())
f=0
for i in lst:
    if i<n or i>m:
        print(i,end=" ")
        f=1
if f==0:
    print(-1)