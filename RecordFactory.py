from .Record import Record
from .Settings import Settings
class RecordFactory:
    def __init__(self, settings: Settings):
        self.settings = settings

    def create_records(self, data):
        records = []
        record_size = self.settings.get("recordSize")
        compression = self.settings.get("compression")
        data_entries = [data[i:i + record_size] for i in range(0, len(data), record_size)]

        for data_entry in data_entries:
            record = Record(data_entry)
            record.compress(compression)
            records.append(record)

        return records

    def create_eof_record(self):
        return Record(0xe98e0d0a)

    def create_fcis_record(self, text_length):
        r = "FCIS"
        r += self.as_string(20, 4)
        r += self.as_string(16, 4)
        r += self.as_string(1, 4)
        r += self.as_string(0, 4)
        r += self.as_string(text_length, 4)
        r += self.as_string(0, 4)
        r += self.as_string(32, 4)
        r += self.as_string(8, 4)
        r += self.as_string(1, 2)
        r += self.as_string(1, 2)
        r += self.as_string(0, 4)
        return Record(r)

    def create_flis_record(self):
        r = "FLIS"
        r += self.as_string(8, 4)
        r += self.as_string(65, 2)
        r += self.as_string(0, 2)
        r += self.as_string(0, 4)
        r += self.as_string(-1, 4)
        r += self.as_string(1, 2)
        r += self.as_string(3, 2)
        r += self.as_string(3, 4)
        r += self.as_string(1, 4)
        r += self.as_string(-1, 4)
        return Record(r)

    def as_string(self, integer, size):
        out = ""
        for i in range(size):
            byte = format(integer & 0xFF, '02X')
            out = byte + " " + out if i > 0 else byte + out
            integer >>= 8
        return out

    def __str__(self):
        out = "Record Factory: {\n"
        out += f"\tRecord Size: {self.settings.get('recordSize')}\n"
        out += f"\tCompression: {self.settings.get('compression')}\n"
        out += "}"
        return out