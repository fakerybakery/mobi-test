from .FileObject import FileObject
class FileInt(FileObject):
    def __init__(self, n=0):
        super().__init__(4)
        self.data = n

    def get(self):
        return self.data

    def set(self, value):
        self.data = int(value)

    def serialize(self):
        return str(self.data)
        # return (self.data).serialize()

    def unserialize(self, data):
        self.__init__(self.to_int(data))

    def __str__(self):
        return "FileInt: {" + self.intAsString(self.data) + "}"
