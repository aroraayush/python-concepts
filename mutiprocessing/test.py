import multiprocessing as mp,os
from datetime import timedelta, date
import os

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def unwrap_self(cls, kw1, kw2):
    cls.process_wrapper(kw1, kw2)
def unwrap_self_listener(cls):
    cls.listener()

class MultiProcessor(object):
    def __init__(self, fname, cores, size=None, fout=None):
        self.fname = fname
        self.cores = cores
        self.fout = fout
        if size == None:
            filesize = os.path.getsize(fname)
            if filesize > 0:
                if filesize < cores:
                    self.size = filesize
                    self.cores = 1
                else:
                    self.size = int(filesize/cores)
            else:
                self.size = 0
        else:
            self.size = int(size)
         
        manager = mp.Manager()
        self.queue = manager.Queue()

    def process(self, line):
        self.queue.put(line + '\n') 

    def process_wrapper(self, chunkStart, chunkSize):
        n = 0
        with open(self.fname) as f:
            f.seek(chunkStart)
            lines = f.read(chunkSize).splitlines()
            for line in lines:
                self.process(line)
                n = n + 1

    def chunkify(self):
        """partition file into small chunks for each process
        """
        if self.size <= 0: return
        fileEnd = os.path.getsize(self.fname)
        with open(self.fname,'r') as f:
            chunkEnd = f.tell()
            while True:
                chunkStart = chunkEnd
                f.seek(self.size,1)
                f.readline()
                chunkEnd = f.tell()
                yield chunkStart, chunkEnd - chunkStart
                if chunkEnd > fileEnd:
                    break

    def listener(self):
        """listen other process sending data 
        """
        f = open(self.fout, 'w')
        n = 0
        while 1:
            m = self.queue.get()
            if m == 'kill':
                break
            f.write(m)
            f.flush()
            n = n + 1
        f.close()


    def run(self):
        #init objects
        pool = mp.Pool(self.cores + 1)
        jobs = []
        
        # start queue for writing file
        if self.fout != None: 
            watcher = pool.apply_async(unwrap_self_listener, (self,))

        #create jobs
        for chunkStart,chunkSize in self.chunkify():
            jobs.append(pool.apply_async(unwrap_self, (self, chunkStart, chunkSize)))

        #wait for all jobs to finish
        for job in jobs:
            job.get()

        #clean up
        # waiting untill queue push data to file 
        if self.fout != None:
            self.queue.put('kill')
            watcher.get()

        pool.close()

if __name__ == '__main__':
    p = MultiProcessor(fname='empty', cores=4, fout='out.tmp')
    p.run()