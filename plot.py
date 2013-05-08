import cv2
import numpy as np
from cv2plot import plotBlock

class bufferedArray(object):
    """
    stand-in for openmdao assembly
    """
    def __init__(self, n = 100):
        self.data = None
        self.n = n
        self.ready = False
        
    def add(self, data):
        if not isinstance(self.data, np.ndarray):
            self.data = data
        else:
            self.data = np.concatenate((self.data,data),axis=1)
        if self.data.shape[1] > self.n:
            self.ready = True
            self.data = self.data[:,-self.n:]

        
if __name__ == "__main__":
    import time
    b = bufferedArray(n=400)
    labels = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    while True:
        t = np.linspace(1,10,1)
        data = np.random.randn(16,3)
        b.add(data)
        #t= time.time()
        plotBlock(b.data, labels = labels, name = "Epoc")
        #print time.time()-t
        key = cv2.waitKey(10)
        if key == 27:
            break
        