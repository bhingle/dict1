from collections import Counter
for _ in range(int(input())):
    n=int(input())
    xco,yco=[],[]
    for _ in range(4*n-1):
        x,y=map(int,input().split())
        xco.append(x)
        yco.append(y)
    xdic=Counter(xco)
    ydic=Counter(yco)
    for key, value in xdic.items():
         if value %2!=0:
             print(key,end=" ")
    for key, value in ydic.items():
         if value%2!=0:
             print(key)
    #happy