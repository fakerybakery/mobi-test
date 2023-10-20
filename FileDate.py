import struct
import time
from .FileObject import FileObject
class FileDate(FileObject):
    def __init__(self, n=0):
        super().__init__(4)
        self.data = n
        self.set(n)

    def get(self):
        return self.data

    def set(self, value):
        self.data = int(value)

    def serialize(self):
        return struct.pack('I', self.data)
        # return str(self.data)

    def unserialize(self, data):
        self.__init__(*struct.unpack('I', data))

    def __str__(self):
        return f"FileDate: {{{time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(self.data - 94694400))}}}"

