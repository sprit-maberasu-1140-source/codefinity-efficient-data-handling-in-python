def running_average():
    total = 0
    count = 0
    average = None
    while True:
        value = yield average
        total +=value
        count +=1
        average = total/count

# Sample usage:
gen = running_average()
next(gen)
print(gen.send(10))  # Should print 10.0
print(gen.send(20))  # Should print 15.0
print(gen.send(30))  # Should print 20.0
