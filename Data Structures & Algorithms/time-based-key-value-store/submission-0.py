class TimeMap:

    def __init__(self):
        self.dictt={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictt:
            self.dictt[key] = []
        self.dictt[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ris= ""
        if key not in self.dictt:
            return ""
        sx=0
        dx=len(self.dictt[key])-1
        while sx<=dx:
            mid=(sx+dx)//2
            if self.dictt[key][mid][1] <= timestamp:
                ris=self.dictt[key][mid][0]
                sx=mid+1
            else:
                dx=mid-1
        return ris
        
