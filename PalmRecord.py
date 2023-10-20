from .FileObject import FileObject
from .FileElement import FileElement
from .FileShort import FileShort
from .FileString import FileString
from .FileInt import FileInt
from .EXTHHelper import EXTHHelper


class PalmRecord(FileObject):
    def __init__(self, settings, records, textRecords, textLength, images):
        self.elements = {
            "compression": FileShort(),
            "unused": FileShort(),
            "textLength": FileInt(),
            "recordCount": FileShort(),
            "recordSize": FileShort(),
            "encryptionType": FileShort(),
            "unused2": FileShort(),
            # MOBI Header
            "mobiIdentifier": FileString("MOBI", 4),
            "mobiHeaderLength": FileInt(),
            "mobiType": FileInt(),
            "textEncoding": FileInt(),
            "uniqueID": FileInt(),
            "fileVersion": FileInt(),
            "reserved": FileString(40),
            "firstNonBookIndex": FileInt(),
            "fullNameOffset": FileInt(),
            "fullNameLength": FileInt(),
            "locale": FileInt(),
            "inputLanguage": FileInt(),
            "outputLanguage": FileInt(),
            "minimumVersion": FileInt(),
            "firstImageIndex": FileInt(),
            "huffmanRecordOffset": FileInt(),
            "huffmanRecordCount": FileInt(),
            "unused3": FileString(8),
            "exthFlags": FileInt(0x40),
            "unknown": FileString(32),
            "drmOffset": FileInt(0xFFFFFFFF),
            "drmCount": FileShort(0xFFFFFFFF),
            "drmSize": FileShort(),
            "drmFlags": FileInt(),
            "mobiFiller": FileString(72),
            # EXTH Header
            "exthIdentifier": FileString("EXTH", 4),
            "exthHeaderLength": FileInt(),
            "exthRecordCount": FileInt(),
            "exthRecords": FileElement(),
            "exthPadding": FileString(),
            # "fullNamePadding": FileString(100),
            "fullName": FileString(),
        }

        # Set values from the info block
        for name, val in settings.values.items():
            if name in self.elements:
                self.elements[name] = settings.get(name)

        els = settings.values

        exthElems = FileElement()
        i = 0
        l = 0
        for name, val in els.items():
            type = EXTHHelper.textToType(name)
            if type is not False:
                type = FileInt(type)
                length = FileInt(8 + len(val))
                data = FileString(val)
                l += 8 + len(val)
                exthElems.add("type" + str(i), type)
                exthElems.add("length" + str(i), length)
                exthElems.add("data" + str(i), data)
                i += 1

        if images > 0:
            self.elements["firstImageIndex"] = textRecords + 1
        self.elements["firstNonBookIndex"] = textRecords + 2 + images
        self.elements["reserved"] = "".rjust(40, chr(255))
        self.elements["exthRecordCount"] = i
        self.elements["exthRecords"] = exthElems
        pad = l % 4
        pad = (4 - pad) % 4
        self.elements["exthPadding"] = "\0" * pad
        self.elements["exthHeaderLength"] = 12 + l + pad

        self.elements["recordCount"] = textRecords
        self.elements["fullNameOffset"] = FileElement(self.elements).offset_to_entry(
            "fullName"
        )
        self.elements["fullNameLength"] = len(settings.get("title"))
        self.elements["fullName"] = settings.get("title")
        self.elements["textLength"] = textLength

    def getByteLength(self):
        return self.getLength()

    def getLength(self):
        return FileElement(self.elements).get_byte_length()

    def get(self):
        return self

    def set(self, elements):
        raise Exception("Unallowed set")

    def serialize(self):
        return FileElement(self.elements).serialize()

    def unserialize(self, data):
        self.elements.unserialize(data)

    def __str__(self):
        output = f"PalmDoc Record ({self.getByteLength()} bytes):\n"
        output += str(self.elements)
        return output
