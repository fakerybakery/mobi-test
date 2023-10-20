class FileElement:
    def __init__(self, elements=None):
        self.elements = elements if elements is not None else {}

    def get_byte_length(self):
        return self.get_length()

    def get_length(self):
        total = 0
        for val in self.elements.values():
            total += len(str(val).encode())
        return total

    def offset_to_entry(self, name):
        pos = 0
        for key, value in self.elements.items():
            if name == key:
                break
            pos += len(str(value).encode())
        return pos

    def exists(self, key):
        return key in self.elements

    def get(self, key):
        return self.elements[key]

    def set(self, key, value):
        self.elements[key] = value

    def add(self, key, value):
        self.elements[key] = value

    def serialize(self):
        result = []
        # print(self.elements)
        for e in self.elements:
            # print(self.elements[e])
            # print(self.elements[e].serialize())
            try:
                result.append(str(self.elements[e].serialize()))
            except:
                result.append(str(self.elements[e]))
        # import sys
        # sys.exit(0)
        # for val in self.elements.values():
        #     result.append(val.serialize())
        return "".join(result)
    def items(self):
        return self.elements
    def unserialize(self, data):
        # TODO: If reading is needed, this method will be more complex
        pass

    def __str__(self):
        output = 'FileElement (' + str(self.get_byte_length()) + ' bytes): {\n'
        for key, value in self.elements.items():
            output += f"\t{key}: {value}\n"
        output += "}"
        return output
