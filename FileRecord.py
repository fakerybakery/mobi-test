from .FileObject import FileObject
class FileRecord(FileObject):
    def __init__(self, record):
        """
        Make a record to be stored in a file
        :param Record record:
        """
        self.record = record

    def getByteLength(self):
        return self.getLength()

    def getLength(self):
        return self.record.getLength()

    def get(self):
        return self.record

    def set(self, record):
        self.record = record

    def serialize(self):
        return self.record.serialize()

    def unserialize(self, data):
        self.__init__(self.record.unserialize(data))
