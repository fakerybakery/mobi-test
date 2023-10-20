from .constants import *
import time
import random
class Settings:
    def __init__(self, additional_settings=None):
        self.values = {
            "attributes": 0,
            "version": 0,
            "creationTime": int(time.time()) + 94694400,
            "modificationTime": int(time.time()) + 94694400,
            "backupTime": 0,
            "modificationNumber": 0,
            "appInfoID": 0,
            "sortInfoID": 0,
            "prcType": "BOOK",
            "creator": "MOBI",
            "uniqueIDSeed": random.randint(0, 2**31 - 1),
            "nextRecordListID": 0,
            "recordAttributes": 0,
            "compression": NO_COMPRESSION,
            "recordSize": RECORD_SIZE,  # You should define RECORD_SIZE
            "encryptionType": NO_ENCRYPTION,  # You should define NO_ENCRYPTION and other constants
            "mobiIdentifier": "MOBI",
            "mobiHeaderLength": 0xe8,
            "mobiType": MOBIPOCKET_BOOK,  # You should define MOBIPOCKET_BOOK and other constants
            "textEncoding": UTF8,  # You should define UTF8 and other constants
            "uniqueID": random.randint(0, 2**31 - 1),
            "fileVersion": 6,
            "locale": 0x09,
            "inputLanguage": 0,
            "outputLanguage": 0,
            "minimumVersion": 6,
            "huffmanRecordOffset": 0,
            "huffmanRecordCount": 0,
            "exthFlags": 0x40,
            "drmOffset": 0xFFFFFFFF,
            "drmCount": 0,
            "drmSize": 0,
            "drmFlags": 0,
            "extraDataFlags": 0,
            "exthIdentifier": "EXTH",
            # These can be changed without any risk
            "title": "Unknown title",
            "author": "Unknown author",
            "subject": "Unknown subject"
        }

        if additional_settings is not None:
            self.values.update(additional_settings)

    def get(self, key):
        return self.values.get(key)

    def exists(self, key):
        return key in self.values
    def items(self):
        return self.values
    def set(self, item, value):
        self.values[item] = value
    def __str__(self):
        out = "Settings: {\n"
        for key, value in self.values.items():
            out += f"\t{key}: {value}\n"
        out += "}"
        return out
