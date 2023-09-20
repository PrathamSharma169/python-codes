def checkpalindrome(a):
    a=str(a)
    n=len(a)
    s=0
    e=n-1
    while s<=e:
        if(a[s]==a[e]):
            result= "true"
        else:
            result="false"
            break
        s=s+1
        e=e-1
    return result
n=str(input("entre your word for checking palindrome\n"))
print(checkpalindrome(n))
