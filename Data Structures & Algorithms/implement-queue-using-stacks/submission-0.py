class MyQueue:

    def __init__(self):
        self.queuein=[]
        self.queueout=[]

    def push(self, x: int) -> None:
        self.queuein.append(x)

    def pop(self) -> int:
        if self.queueout:
            return self.queueout.pop()
        while self.queuein:
            self.queueout.append(self.queuein.pop())
        return self.queueout.pop()

    def peek(self) -> int:
        if self.queueout:
            return self.queueout[-1]
        while self.queuein:
            self.queueout.append(self.queuein.pop())
        return self.queueout[-1]

    def empty(self) -> bool:
        return not self.queueout and not self.queuein
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()