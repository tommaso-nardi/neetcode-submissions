class Solution:
    def simplifyPath(self, path: str) -> str:
        
        azioni=path.split('/')
        percorso=[]
        for a in azioni:
            if a == '' or a == '.':
                continue
            if a == '..':
                if percorso:
                    percorso.pop()
            else:
                percorso.append(a)
        return "/"+"/".join(percorso)