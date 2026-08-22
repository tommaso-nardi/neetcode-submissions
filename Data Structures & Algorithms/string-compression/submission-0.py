class Solution:
    def compress(self, chars: List[str]) -> int:
        
        puntwrite=0
        puntread=0

        while puntread in range(len(chars)):
            car=chars[puntread]
            count=0
            while puntread in range(len(chars)) and car==chars[puntread]:
                puntread+=1
                count+=1
            chars[puntwrite]=car
            puntwrite+=1
            moltatt=1
            if count==1:
                continue
            while count//moltatt>=10:
                moltatt*=10
            while moltatt!=1:
                chars[puntwrite]=str(count//moltatt%10)
                moltatt//=10
                puntwrite+=1
            chars[puntwrite]=str(count//moltatt%10)
            puntwrite+=1
        
        return puntwrite
