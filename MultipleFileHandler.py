from .ImageHandler import ImageHandler
class MultipleFileHandler:
    def __init__(self):
        self.files = []
        self.images = []
        self.metadata = {}
        self.toc = []

    def add_page(self, contents, title=""):
        if title:
            # TODO: Add to TOC (and add a way of generating it)
            contents = f"<h2>{title}</h2>{contents}<mbp:pagebreak>"

        pos = 0

        if self.toc:
            last_toc = self.toc[-1]
            last_file = self.files[-1]
            pos = last_toc["pos"] + len(last_file) + 1

        self.files.append(contents)
        self.toc.append({"title": title, "pos": pos})

    def add_image(self, image_contents):
        self.images.append(image_contents)
        return len(self.images) - 1

    def add_image_from_url(self, url):
        image = ImageHandler.download_image(url)  # Assuming ImageHandler is defined elsewhere
        if image is False:
            return False
        return self.add_image(image)

    def set_metadata(self, key, value):
        self.metadata[key] = value

    def get_text_data(self):
        data = "\n".join(self.files)
        begin = "<html><head><guide><reference title='CONTENT' type='toc' filepos=0000000000 /></guide></head><body>"
        before_toc = begin + data

        toc_pos = len(before_toc)

        toc = self.generate_toc(len(begin))

        custom_begin = f"<html><head><guide><reference title='CONTENT' type='toc' filepos={self.force_length(toc_pos, 10)} /></guide></head><body>"
        data = custom_begin + data + toc + "</body></html>"
        return data

    def force_length(self, n, l):
        str_n = str(n)
        cur = len(str_n)
        while cur < l:
            str_n = "0" + str_n
            cur += 1
        return str_n

    def generate_toc(self, base=0):
        toc = "<h2>Contents</h2>"
        toc += "<blockquote><table summary='Table of Contents'><b><col/><col/><tbody>"
        for i, entry in enumerate(self.toc):
            position = entry["pos"] + base
            toc += f"<tr><td>{i + 1}.</td><td><a filepos={position}>{entry['title']}</a></td></tr>"
        toc += "</tbody></b></table></blockquote>"
        return toc

    def get_images(self):
        return self.images

    def get_metadata(self):
        return self.metadata
