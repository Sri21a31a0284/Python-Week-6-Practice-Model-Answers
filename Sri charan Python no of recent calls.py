class RecentCounter:
    def _init_(self):
        self.queue = []
        self.miliseconds = 3000

    def ping(self, t:int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-self.miliseconds:
            self.queue.pop(0)
        return len(self.queue)
