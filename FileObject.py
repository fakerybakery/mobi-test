class FileObject:
    def __init__(self, byteLength=-1):
        self.byteLength = byteLength

    def getByteLength(self):
        if self.byteLength >= 0:
            return self.byteLength
        return self.getLength()

    def getLength(self):
        raise Exception("Sub-class needs to implement this if it doesn't have a fixed length")

    def toInt(self, string):
        out = 0
        for i in range(min(4, len(string))):
            out |= ord(string[i]) << ((len(string) - i - 1) * 8)
        return out

    def byteToString(self, integer):
        return self.toString(integer, 1)

    def byteAsString(self, integer):
        return self.asString(integer, 1)

    def shortToString(self, integer):
        return self.toString(integer, 2)

    def shortAsString(self, integer):
        return self.asString(integer, 2)

    def triToString(self, integer):
        return self.toString(integer, 3)

    def triAsString(self, integer):
        return self.asString(integer, 3)

    def intToString(self, integer):
        return self.toString(integer, 4)

    def intAsString(self, integer):
        return self.asString(integer, 4)

    def toString(self, integer, size):
        out = bytearray()
        for i in range(size):
            out.append(integer & 0xFF)
            integer >>= 8
        return bytes(out)

    def asString(self, integer, size):
        out = ""
        for i in range(size):
            if i > 0:
                out = " " + out
            byte = format(integer & 0xFF, "02X")
            out = byte + out
            integer >>= 8
        return out

    def get(self):
        pass

    def set(self, value):
        pass

    def serialize(self):
        pass

    def unserialize(self, data):
        pass
