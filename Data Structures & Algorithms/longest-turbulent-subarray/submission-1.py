class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        window_sx=0
        massimo=1
        attuale=0
        # 0 è '=', 1 è '<', 2 è '>'
        segno=-1
        for window_dx in range(1,len(arr)):
            if arr[window_dx-1] > arr[window_dx]:
                attuale=2
            elif arr[window_dx-1] < arr[window_dx]:
                attuale=1
            elif arr[window_dx-1] == arr[window_dx]:
                attuale=0
            
            if attuale==0:
                window_sx=window_dx
            elif attuale==segno:
                window_sx=window_dx-1
                
            
            segno=attuale

            massimo=max(massimo,window_dx-window_sx+1)

        return massimo
                