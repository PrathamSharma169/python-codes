def repeatedSubstringPattern( s):
        s=list(s)
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if(s[i]==s[j]):
                    if (j==len(s)-1 ):
                        break 
                    else:
                        if(s[i+1]==s[j+1]):
                            return 'true'
        return 'false'
s="abcab"
print(repeatedSubstringPattern(s))