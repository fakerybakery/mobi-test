from .FileObject import FileObject
class FileShort(FileObject):
    def __init__(self, n=0):
        super().__init__(2)
        self.set(n)

    def get(self):
        return self.data

    def set(self, value):
        self.data = int(value) & 0xFFFF

    def serialize(self):
        return self.shortToString(self.data)
        # return str(self.data)

    def unserialize(self, data):
        self.__init__(self.to_int(data))

    def __str__(self):
        return "FileShort: {" + self.shortAsString(self.data) + "}"
