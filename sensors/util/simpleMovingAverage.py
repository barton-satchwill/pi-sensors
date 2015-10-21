from collections import deque


class SimpleMovingAverage:

    def __init__(self, id, window_size=10):
        self.id = id
        self.window_size = window_size
        self.values = deque([0.0] * self.window_size)
        self.sum = 0.0
        self.n = 0

        print "initialising smoothed average for '" + self.id +"'"


    def getAverage(self, newValue=None, debug=False):
        if newValue:
            self.values.append(newValue)
            self.sum += newValue - self.values.popleft()
            self.n+=1
        self.n = min(self.n, self.window_size)
        if debug:
            for v in self.values:
                print "{:.2f} ".format(v),
            print " ==> %.2f/%d = %f" % (self.sum, self.n, self.sum/self.n)
            
        return self.sum/self.n
