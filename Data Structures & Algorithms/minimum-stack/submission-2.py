class MinStack:

    def __init__(self):
        self.arr = []
        self.smallest = []
        

    def push(self, val: int) -> None:

        new = [val]
        self.arr = new + self.arr
        
        if not self.smallest:
            self.smallest.append(val)
        else:
            self.smallest = [min(val, self.smallest[0])] + self.smallest
        

    def pop(self) -> None:

        new = self.arr[1:]
        self.arr = new
        
        new2 = self.smallest[1:]
        self.smallest = new2



    def top(self) -> int:
        return self.arr[0]
        

    def getMin(self) -> int:
        return self.smallest[0]

        
