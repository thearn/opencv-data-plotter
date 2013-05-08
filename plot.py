import cv2
import numpy as np

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

def plotBlock(data,t=None, size = (600,1000), labels = [],margin = 5, 
              name = "plot"):
    m,n = data.shape
    if n<2:
        return
    if not t:
        t = range(len(data[0]))
    
    w = float(size[1])
    h = size[0]/float(m)    
    
    t = np.array(t)
    tt = (w-2*margin)*(t - t.min()) / (t.max() - t.min())+margin
    P, i = [], 0
    z = np.zeros((size[0],size[1],3))
    for y in data:
        y = -np.array(y)
        yy = (h-2*margin)*(y - y.min()) / (y.max() - y.min())+margin + i*h
        maxy = max(yy)
        
        pts = np.array([[x_, y_] for x_, y_ in zip(tt,yy)],np.int32)
        P.append(pts)
        if labels:
            col = (0,255,0)
            cv2.putText(z,labels[i],(0,int(i*h+margin+0.5*h)),
                        cv2.FONT_HERSHEY_PLAIN,1,col)  
            cv2.putText(z,labels[i],(int(tt[-1])+1,int(i*h+margin+0.5*h)),
                        cv2.FONT_HERSHEY_PLAIN,1,col)  
        i+=1
    """
    for p in P:
        for i in xrange(len(p)-1):
            cv2.line(z,tuple(p[i]),tuple(p[i+1]), (255,255,255),1)  
    """
    for p in P:
        cv2.polylines(z, [p], False, (255,255,255),1)
    cv2.imshow(name,z)
        
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
        cv2.waitKey(10)