from .FileObject import FileObject
class FileTri(FileObject):
    def __init__(self, n=0):
        super().__init__(3)
        self.data = 0
        self.set(n)

    def get(self):
        return self.data

    def set(self, value):
        self.data = int(value) & 0xFFFFFF

    def serialize(self):
        return self.triAsString(self.data)

    def unserialize(self, data):
        self.__init__(self.to_int(data))

    def __str__(self):
        return "FileTri: {" + self.triAsString(self.data) + "}"
