class Array:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.array = [None]*capacity
      
    def push_front(self,data):
        if self.size == self.capacity:
            print("Array is full")
        else:
            for i in range(self.size, 0, -1):
                self.array[i]=self.array[i-1]
            self.array[0] = data
            self.size = self.size+1
    
    def push_back(self, val):
        if self.size == self.capacity:
            print("Array is full")
        else:
            self.array[self.size] = val
            self.size += 1
            
    def insert(self, data, pos):
        if self.size == self.capacity:
            print("Array is full")
        if pos < 0 or pos > self.size:
            print("Invalid pos")
        else:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]
            self.array[pos] = data
            self.size = self.size + 1
    
    def pop_front(self):
        if self.size == 0:
            print("Array Is Empty")
            return
        
        for i in range(1, self.size):
            self.array[i-1] = self.array[i]
            
        self.array[self.size-1] = None
        
        self.size -= 1
    
    def pop_back(self):
        self.array[self.size-1] = None
        self.size -= 1
    
    def erase(self, pos):
        if self.size == 0:
            print("Array Is Empty")
            return
        if pos < 0 or pos > self.size:
            print("Invalid pos")
            return
        
        for i in range(pos+1, self.size):
            self.array[pos] = self.array[i]
        
        self.size -= 1

    def print(self):
        print("[", end="")
        for i in range(self.size-1):
            print(self.array[i], end=",")
        print(self.array[self.size-1], end="")
        print("]", end="\n")

def main():
    array = Array(10)

if __name__ == "__main__":
    main()