from .FileRecord import FileRecord
from .LinkedStringBulider import LinkedStringBuilder
from .ImageHandler import ImageHandler
from .Record import Record
class MOBIFile:
    PARAGRAPH = 0
    H2 = 1
    H3 = 2
    IMAGE = 3
    PAGEBREAK = 4

    TOC_LINK = "_MOBI_TOC"
    START_LINK = "_START_TOC"

    def __init__(self):
        self.settings = {"title": "Unknown Title", "toc": True}
        self.parts = []
        self.images = []
        self.links = []

    def get_text_data(self):
        str = LinkedStringBuilder()
        str.append("<html>")
        str.append("<head>")
        self.add_guide(str)
        str.append("</head>")
        str.append("<body>")
        self.resolve_filepos(str, self.START_LINK)
        str.append("<h1>" + self.settings["title"] + "</h1>")
        entries = self.add_text(str)
        self.add_toc(str, entries)
        str.append("</body>")
        str.append("</html>")
        return str.build()

    def filepos(self, position):
        return str(position).rjust(10, "0")

    def add_filepos(self, str, name):
        str.add_link(name)
        str.append(self.filepos(0))

    def resolve_filepos(self, str, name):
        str.resolve_link(name, self.filepos(str.length()))

    def add_guide(self, str):
        str.append("<guide>")
        str.append("<reference title='CONTENT' type='toc' filepos=")
        self.add_filepos(str, self.TOC_LINK)
        str.append(" />")
        str.append("<reference title='CONTENT' type='start' filepos=")
        self.add_filepos(str, self.START_LINK)
        str.append(" />")
        str.append("</guide>")

    def add_text(self, str):
        entries = []
        for i in range(len(self.parts)):
            (type, data) = self.parts[i]
            id = "title_" + str(i)
            if type == self.PARAGRAPH:
                str.append("<p>" + data + "</p>")
            elif type == self.PAGEBREAK:
                str.append("<mbp:pagebreak></mbp:pagebreak>")
            elif type == self.H2:
                entries.append({"level": 2, "title": data, "id": id})
                self.resolve_filepos(str, id)
                str.append("<a name='" + id + "'></a><h2 id='" + id + "'>" + data + "</h2>")
            elif type == self.H3:
                entries.append({"level": 3, "title": data, "id": id})
                self.resolve_filepos(str, id)
                str.append("<a name='" + id + "'></a><h3 id='" + id + "'>" + data + "</h3>")
            elif type == self.IMAGE:
                str.append("<img recindex=" + str(data + 1).rjust(10, "0") + " />")
        return entries

    def add_toc(self, str, entries):
        self.resolve_filepos(str, self.TOC_LINK)
        str.append("<h2>Contents</h2>")
        str.append("<blockquote><table summary='Table of Contents'><col/><tbody>")
        for i in range(len(entries)):
            entry = entries[i]
            str.append("<tr><td><a href='#" + entry["id"] + "' filepos=")
            self.add_filepos(str, entry["id"])
            str.append(">" + entry["title"] + "</a></td></tr>")
        str.append("</tbody></b></table></blockquote><mbp:pagebreak/>")

    def get_images(self):
        return self.images

    def get_metadata(self):
        return self.settings

    def set(self, key, value):
        self.settings[key] = value

    def get(self, key):
        return self.settings[key]

    def append_paragraph(self, text):
        self.parts.append((self.PARAGRAPH, text))

    def append_chapter_title(self, title):
        self.parts.append((self.H2, title))

    def append_section_title(self, title):
        self.parts.append((self.H3, title))

    def append_page_break(self):
        self.parts.append((self.PAGEBREAK, None))

    def append_image(self, img):
        img_index = len(self.images)
        self.images.append(FileRecord(Record(ImageHandler.create_image(img))))
        self.parts.append((self.IMAGE, img_index))
