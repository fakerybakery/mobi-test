from .FileElement import FileElement
from .FileShort import FileShort
from .FileString import FileString
from .FileInt import FileInt
from .FileDate import FileDate
from .FileByte import FileByte
from .FileTri import FileTri
class Prc(FileElement):
    def __init__(self, settings, records):
        super().__init__({
            "title": FileString(32),
            "attributes": FileShort(),
            "version": FileShort(),
            "creationTime": FileDate(),
            "modificationTime": FileDate(),
            "backupTime": FileDate(),
            "modificationNumber": FileInt(),
            "appInfoID": FileInt(),
            "sortInfoID": FileInt(),
            "prcType": FileString(4),
            "creator": FileString(4),
            "uniqueIDSeed": FileInt(),
            "nextRecordListID": FileInt(),
            "numberRecords": FileShort(),
            "recordList": FileElement(),
            "filler": FileShort(),
            "records": FileElement()
        })

        # Set values from the info block
        for name, val in self.elements.items():
            if name in settings.items():
                val.set(settings.items()[name])

        self.get("numberRecords").set(len(records))

        i = 0
        for record in records:
            offset = FileInt()
            attr = FileByte()
            uniqueID = FileTri(i)

            self.elements["recordList"].add("Rec" + str(i), FileElement({
                "offset": offset,
                "attribute": attr,
                "uniqueID": uniqueID
            }))

            self.elements["records"].add("Rec" + str(i), record)
            i += 1

        self.update_offsets(records)

    def get_byte_length(self):
        raise Exception("Test")

    def update_offsets(self, records):
        base = self.offset_to_entry("records")

        i = 0
        for record in records:
            el = self.elements["recordList"].get("Rec" + str(i))
            local = self.elements["records"].offset_to_entry("Rec" + str(i))
            el.get("offset").set(base + local)
            i += 1

    def save(self, file):
        with open(file, "w") as handle:
            handle.write(self.serialize())

    def output(self):
        print(self.serialize())

    def __str__(self):
        output = f"Prc ({self.get_byte_length()} bytes): {{\n"
        for key, value in self.elements.items():
            output += f"\t{key}: {value}\n"
        output += "}"
        return output
