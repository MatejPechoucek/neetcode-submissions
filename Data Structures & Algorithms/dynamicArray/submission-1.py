class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 1:
            self.capacity = 1
        else:
            self.capacity = capacity
        self.items = []

    def get(self, i: int) -> int:
        return self.items[i]

    def set(self, i: int, n: int) -> None:
        self.items[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            self.resize()
        self.items.append(n)

    def popback(self) -> int:
        return self.items.pop()

    def resize(self) -> None:
        self.capacity *= 2

    def getSize(self) -> int:
        return len(self.items)
    
    def getCapacity(self) -> int:
        return self.capacity