class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str: 
        if len(str1) < len(str2):
            str1,str2 = str2,str1
        
        #Startswith molto carina, vede una stringa comincia con un altra
        #Il trucco dell'esecuzione invece sta nel tagliare la stringa più grande fino a che non
        #diventa uguale di lunghezza alla più piccola
        while str1!=str2:
            if not str1.startswith(str2):
                return ""
            str1=str1[len(str2):]
            if len(str1) < len(str2):
                str1,str2 = str2,str1
        
        return str1