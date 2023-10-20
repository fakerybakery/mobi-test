class LinkedStringBuilder:
    def __init__(self):
        self.length = 0
        self.partSize = []
        self.parts = []
        self.links = {}
        self.resolutions = {}

    def addLink(self, name):
        self.links[name] = self.length

    def resolveLink(self, name, value):
        self.resolutions[name] = value

    def append(self, string):
        string_length = len(string)
        self.length += string_length
        self.partSize.append(string_length)
        self.parts.append(string)

    def replace(self, from_, to, replacement):
        part_start = 0
        part_end = 0
        for i in range(len(self.partSize)):
            part_end += self.partSize[i]
            if part_end > from_:
                if part_end < to:
                    self.replace(part_end, to, replacement[part_end - from_:])
                    replacement = replacement[:part_end - from_]
                    to = part_end

                cur = list(self.parts[i])
                for j in range(to - from_):
                    cur[from_ - part_start + j] = replacement[j]

                self.parts[i] = ''.join(cur)
                return True

            part_start = part_end

        raise Exception("Couldn't replace string (target longer than source?)")

    def length(self):
        return self.length

    def processLinks(self):
        for name, value in self.resolutions.items():
            if name in self.links:
                start = self.links[name]
                self.replace(start, start + len(value), value)
                del self.resolutions[name]

    def build(self):
        self.processLinks()
        return ''.join(self.parts)
