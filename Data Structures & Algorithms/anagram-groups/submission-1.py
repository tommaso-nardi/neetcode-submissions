class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt={}
        solparola=[]
        soltutte=[]
        for stringa in strs:
            chiave="".join(sorted(stringa))
            if chiave not in dictt:
                dictt[chiave]=[]
            dictt[chiave].append(stringa)
        for chiave in dictt:
            for parola in dictt[chiave]:
                solparola.append(parola)
            if solparola != []:
                soltutte.append(solparola)
                solparola=[]
        return soltutte