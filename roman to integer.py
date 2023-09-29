class Solution(object):
    def romanToInt(self, s):
        s=str(s)
        a=0
        b=0
        c=0
        d=0
        e=0
        f=0
        g=0
        i=0
        while i<len(s):
            if s[i]=='I':
                if i!=len(s)-1:
                    if s[i+1]=='V':
                        a=a+4
                        i=i+1
                        
                    elif s[i+1]=='X' :
                        a=a+9
                        i=i+1
                    else:
                        a=a+1
                else :
                    a=a+1
            elif s[i]=='X':
                if i!=len(s)-1:
                    if s[i+1]=='C':
                        c=c+90
                        i=i+1
                        
                    elif s[i+1]=='L':
                        c=c+40
                        i=i+1
                    else:
                        c=c+10
                else:
                    c=c+10
            elif s[i]=='C':
                if i!=len(s)-1:
                    if s[i+1]=='M':
                        e=e+900
                        i=i+1
                        
                    elif s[i+1]=='D':
                        e=e+400
                        i=i+1
                    else:
                        e=e+100
                else:
                    e=e+100
            elif s[i]=='V':
                b=b+5
            elif s[i]=='L':
                d=d+50
            elif s[i]=='D':
                f=f+500
            elif s[i]=='M':
                g=g+1000
            i=i+1
        sum = a + b + c + d + e + f + g
        return sum
obj=Solution()
x=str(input("enter the roman number you want to convert in numerical \n"))
z=obj.romanToInt(x)
print(f"integer conversion of roman {x} is {z}")
