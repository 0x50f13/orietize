import pickle

import threading

mutex=threading.Lock()
class Storage:
    def __init__(self, _fname):
        '''
        :param _fname:File name to save storage into
        '''
        self.data = dict()
        self.fname = _fname

    def save(self):
        mutex.acquire()
        with open(self.fname, "wb+") as f:
            pickle.dump(self.data, f)
        mutex.release()
    def load(self):
        mutex.acquire()
        with open(self.fname, "rb") as f:
            self.data=pickle.load(f)
        mutex.release()
    def get(self,key):
        mutex.acquire()
        val=self.data[key]
        mutex.release()
        return val
    def update(self,key,val):
        mutex.acquire()
        self.data.update({key:val})
        mutex.release()