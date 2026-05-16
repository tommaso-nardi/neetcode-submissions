class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        dictt = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        queue=[]
        for char in s:
            if char in dictt:
                if not queue:
                    return False
                estratto=queue.pop()
                if estratto!=dictt[char]:
                    return False
            else:
                queue.append(char)
        return not queue
        
        