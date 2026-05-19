class Solution:
    def simplifyPath(self, path: str) -> str:
        
        #.split('/') fa si che dividiamo tutto basandoci sugli slash restituendo una lista
        azioni=path.split('/')
        percorso=[]
        for a in azioni:
            #Se non è niente di che, continue
            if a == '' or a == '.':
                continue
            #Se è una rimozione, rimuovi l'ultima cartella con .pop()
            if a == '..':
                if percorso:
                    percorso.pop()
            #Altrimenti semplicemente salva la cartella nel percorso fatto
            else:
                percorso.append(a)
        #Return fatto in modo che all'inizio si mette lo '/' e poi lo '/.join' fa si che in mezzo ad ogni elemento
        #nel percorso ci mettiamo uno slash e restituiamo il tutto come stringa, percorso[0]/percorso[1]/...
        return "/"+"/".join(percorso)