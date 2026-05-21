class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        i=0
        for i in range(len(asteroids)):
            vivo=True
            #Se va verso sinistra (negativo) e abbiamo altri asteroidi che vanno verso destra (positivo)
            #Allora vedi chi sopravvive finchè non esplode quello attuale o tutti i positivi rimasti
            while asteroids[i]<0 and stack and stack[-1] > 0:
                if abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    vivo=False
                    break
                elif abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                else:
                    vivo=False
                    break
            if vivo==True:
                stack.append(asteroids[i])
        return stack
            
                 