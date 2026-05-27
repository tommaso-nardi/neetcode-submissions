class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #Approccio due puntatori ricerca binaria.
        sx=0
        dx=len(arr)-1
        mid=0
        #Cerca il centro perfetto
        while sx<dx:
            mid=(sx+dx)//2
            if arr[mid]==x:
                break
            if arr[mid]>x:
                dx=mid
            else:
                sx=mid+1
        
        #Questo controllo serve per assicurarci che mid è corretto, perchè magari
        #il ciclo terminerebbe senza contare un elemento che è in realtà il centro vero
        #inoltre mid=sx perchè se siamo usciti senza Break, l'indice più corretto è li
        if sx==dx:
            mid=sx
        if mid > 0 and abs(arr[mid - 1] - x) <= abs(arr[mid] - x):
            mid = mid - 1
        
        sx=mid
        dx=mid
        #E dopo partendo da quel mid vedi dove espanderti ad ogni step, se a sx o dx
        #a seconda della distanza, se sx-1 conviene allora prendi quello, altrimenti dx+1
        while dx-sx+1<k:
            if sx==0:
                dx+=1
            elif dx==len(arr)-1:
                sx-=1
            else:
                if abs(arr[sx - 1] - x) <= abs(arr[dx + 1] - x):
                    sx -= 1
                else:
                    dx += 1
        
        return arr[sx:dx+1]