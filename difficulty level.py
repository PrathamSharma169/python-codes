T=int(input())
cnt=0
for i in range(T):
    N=int(input())
    X=list(map(int,input().split()))
    for j in range(len(X)):
        X[j]=int(X[j])
        if X[j]>=1000:
            cnt=cnt+1
    print(cnt)
    