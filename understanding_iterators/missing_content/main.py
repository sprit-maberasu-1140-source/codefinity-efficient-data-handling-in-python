class OddRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = None

        if start % 2 ==0:
            self.current = start + 1
        else:
            self.current = start
            
    def __iter__(self):
        return self

    def __next__(self):

        pass

        if self.current >= self.stop:
            raise StopIteration

        result = self.current
        self.current += 2
        return result
        

# Example usage
odds = OddRange(3, 11)
for number in odds:
    print(number)
