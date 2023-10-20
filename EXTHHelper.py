class EXTHHelper:
    types = {
        1: "drm server id",
        2: "drm commerce id",
        3: "drm ebookbase book id",
        100: "author",
        101: "publisher",
        102: "imprint",
        103: "description",
        104: "isbn",
        105: "subject",
        106: "publishingdate",
        107: "review",
        108: "contributor",
        109: "rights",
        110: "subjectcode",
        111: "type",
        112: "source",
        113: "asin",
        114: "versionnumber",
        115: "sample",
        116: "startreading",
        118: "retail price",
        119: "retail price currency",
        201: "coveroffset",
        202: "thumboffset",
        203: "hasfakecover",
        204: "Creator Software",
        205: "Creator Major Version",
        206: "Creator Minor Version",
        207: "Creator Build Number",
        208: "watermark",
        209: "tamper proof keys",
        300: "fontsignature",
        401: "clippinglimit",
        402: "publisherlimit",
        403: "403",
        404: "ttsflag",
        501: "cdetype",
        502: "lastupdatetime",
        503: "updatedtitle"
    }

    flippedTypes = {
        "drm server id": 1,
        "drm commerce id": 2,
        "drm ebookbase book id": 3,
        "author": 100,
        "publisher": 101,
        "imprint": 102,
        "description": 103,
        "isbn": 104,
        "subject": 105,
        "publishingdate": 106,
        "review": 107,
        "contributor": 108,
        "rights": 109,
        "subjectcode": 110,
        "type": 111,
        "source": 112,
        "asin": 113,
        "versionnumber": 114,
        "sample": 115,
        "startreading": 116,
        "retail price": 118,
        "retail price currency": 119,
        "coveroffset": 201,
        "thumboffset": 202,
        "hasfakecover": 203,
        "Creator Software": 204,
        "Creator Major Version": 205,
        "Creator Minor Version": 206,
        "Creator Build Number": 207,
        "watermark": 208,
        "tamper proof keys": 209,
        "fontsignature": 300,
        "clippinglimit": 401,
        "publisherlimit": 402,
        "403": 403,
        "ttsflag": 404,
        "cdetype": 501,
        "lastupdatetime": 502,
        "updatedtitle": 503
    }

    @staticmethod
    def typeToText(type):
        if type in EXTHHelper.types:
            return EXTHHelper.types[type]
        return type

    @staticmethod
    def textToType(text):
        text = text.lower()
        if text in EXTHHelper.flippedTypes:
            return EXTHHelper.flippedTypes[text]
        return False

    @staticmethod
    def convert(n, size):
        mask = 0xFF
        out = bytearray()
        for i in range(size):
            out.insert(0, (n & mask) >> (8 * i))
            mask = mask << 8
        return bytes(out)

    @staticmethod
    def getRightRepresentation(type, value):
        if 100 <= type < 200:
            return value
        else:
            return EXTHHelper.toHex(value)

    @staticmethod
    def toHex(value):
        out = ""
        for i in range(len(value)):
            if i > 0:
                out += " "
            hex_value = format(value[i], '02x')
            out += hex_value
        return out
