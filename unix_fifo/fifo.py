"""
this is simple lib use to access linux fifo file function

"""

import os

def open(filename):
    return FIFO(filename)


class FIFO:
    """
    this is simple unix object
    use to access fifo object
    """
    def __init__(self, filename):
        """
        def __init__(self, filename):

        filename is the path of fifo file
        """
        self.fd = os.open(filename, os.O_RDWR)
        self.fr = os.fdopen(self.fd, 'ra+')



    def readline(self):
        """
        def readline(self):

        this function read one line from filename
        """
        return self.fr.readline()

    def read(self):
        """
        def read(self):

        this function read all context from filename
        """
        return self.fr.read()
    
    def write(self, value):
        """
        def write(self, value):

        this function send
        """
        #return os.write(self.fd, value)
        self.fr.write(value)
        self.fr.flush()
    

    def writeline(self, value):
        """
        def writeline(self, value):

        this function is write value with new line
        """
        self.write(value)
        self,write('\n')

if __name__ == '__main__':
    """
    example:
    """
    name = '/tmp/simple'
    os.mkfifo( name )
    fifo = open( name )
    
    fifo.write('123\n')
    print fifo.readline(), 'result'
    os.remove( name )

