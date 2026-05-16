class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s)==1:
            if s[0]=='*':
                return True
            else:
                return False
        indexsx=[]
        indexdx=[]
        indexjo=[]
        ss=s[len(s)::-1]
        i=0
        for i in range(len(s)):
            if s[i] == '(':
                indexsx.append(i)
            if s[i] == '*':
                indexjo.append(i)
            if s[i] == ')':
                if len(indexsx) != 0:
                    indexsx.pop()
                elif len(indexjo) != 0:
                    indexjo.pop()
                elif len(indexsx) == 0 and len(indexjo) == 0:
                    return False
        numsx=len(indexsx)-1
        rimossi=0
        while indexsx and indexjo:
            if indexsx.pop() > indexjo.pop():
                return False
        if len(indexsx) == 0:
            return True
        else:
            return False
