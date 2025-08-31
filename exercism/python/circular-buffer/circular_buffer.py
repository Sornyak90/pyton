class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.buf = [[] for i in range(capacity)]
        self.old_reg = 0
        self.last_rec= 0

    def read(self):
        for i in self.buf:
            if i != []:
                break
        else:
            raise BufferEmptyException("Circular buffer is empty")
        
        tmp = self.buf[self.old_reg][0] 
        self.buf[self.old_reg] = [] 
        if  self.old_reg+1 != len(self.buf):
             self.old_reg+=1
        else:
            self.old_reg=0
       
        return tmp  

    def write(self, data):
        for i in range(len(self.buf)):
            if self.buf[i] ==[]:
                break
        else:
            raise BufferFullException("Circular buffer is full")

        self.buf[self.last_rec].append(data)
        if self.last_rec + 1 != len(self.buf):
            self.last_rec+=1
        else:
            self.last_rec = 0
        # for i in range(len(self.buf)):
        #     if self.buf[i] != []:
        #         continue
        #     else:
        #         self.buf[i].append(data)
        #         break
            


    
        return self.buf

    def overwrite(self, data):
        for i in range(len(self.buf)):
            if self.buf[i] ==[]:
                self.buf[i].append(data)
                break
        else:
            self.buf[self.old_reg].clear()
            self.buf[self.old_reg].append(data)
            if  self.old_reg+1 != len(self.buf):
                self.old_reg+=1
            else:
                self.old_reg=0

    def clear(self):
        for i in self.buf:
            i.clear()