<<<<<<< HEAD
def reversestring(a):
    a=list(a)
    n=len(a)
    s=0
    e=n-1
    while s<=e:
        a[s],a[e]=a[e],a[s]
        s=s+1
        e=e-1
    sum=''
    for i in range(len(a)):
        sum=sum+a[i]
    return sum
n=str(input("entre string\n"))
============
def reversestring(a):
    a=list(a)
    n=len(a)
    s=0
    e=n-1
    while s<=e:
        a[s],a[e]=a[e],a[s]
        s=s+1
        e=e-1
    sum=''
    for i in range(len(a)):
        sum=sum+a[i]
    return sum
n=str(input("entre string\n"))
>>>>>>> 97c619817484d04a3021ad3cda11ac9712492c81
print(reversestring(n))