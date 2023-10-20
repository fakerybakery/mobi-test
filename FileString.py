from .FileObject import FileObject
class FileString(FileObject):
    def __init__(self, first=None, second=None):
        self.forcedLength = -1
        self.data = ""

        if second is not None:
            self.data = first
            self.forcedLength = second
        elif first is not None:
            if isinstance(first, str):
                self.data = first
            else:
                self.forcedLength = first

    def getByteLength(self):
        return self.getLength()

    def getLength(self):
        if self.forcedLength >= 0:
            return self.forcedLength
        return len(self.data)

    def get(self):
        return self.data

    def set(self, value):
        self.data = value

    def serialize(self):
        output = self.data
        curLength = len(output)

        if self.forcedLength >= 0:
            if self.forcedLength > curLength:
                return output.ljust(self.forcedLength, '\0')
            elif self.forcedLength == curLength:
                return output
            else:
                return output[:self.forcedLength]

        return output

    def unserialize(self, data):
        self.__init__(data)

    def __str__(self):
        out = "FileString"
        if self.forcedLength >= 0:
            out += f" {self.forcedLength}"
        out += ': {"' + self.serialize().replace(" ", "&nbsp;").replace("\0", "&nbsp;") + '"}'
        return out
