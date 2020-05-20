
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.index = 0

    def append(self, item):
       
        if len(self.buffer) < self.capacity:
            self.buffer.append(item)

       
        else:
            self.buffer[self.index] = item
            self.index += 1

       
        if self.index == self.capacity:
            self.index = 0

    def get(self):
        final = []
        for item in self.buffer:
            final.append(item)

        return final

