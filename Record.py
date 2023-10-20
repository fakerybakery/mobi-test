class Record:
    """
    A Record of a PDB file
    """

    NO_COMPRESSION = 0
    PALMDOC_COMPRESSION = 1
    HUFF = 2

    def __init__(self, data="", length=-1):
        """
        Create a record

        :param data: Data contained in the record
        :param length: Length of the record (if set to -1, the length of data will be taken)
        """
        self.data = data
        if length >= 0:
            self.length = length
        else:
            self.length = len(str(data).encode())

    def compress(self, compression_method):
        pass

    def get_byte_length(self):
        return self.get_length()

    def get_length(self):
        return self.length

    def get(self):
        return self.data

    def set(self, value):
        self.data = value

    def serialize(self):
        return self.data

    def unserialize(self, data):
        self.__init__(data)

    def __str__(self):
        to_show = self.data
        if len(str(self.data)) > 103:
            to_show = self.data[:100] + "..."
        out = "Record: {\n"
        out += "\t" + str(to_show) + "\n"
        out += "}"
        return out
