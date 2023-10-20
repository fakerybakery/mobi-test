from .PalmRecord import PalmRecord
from .Prc import Prc
from .CharacterEntities import CharacterEntities
from .RecordFactory import RecordFactory
from .Settings import Settings


class MOBI:
    def __init__(self):
        self.source = None
        self.images = []
        self.optional = {}
        self.img_counter = 0
        self.debug = False
        self.prc = None

    def get_title(self):
        if "title" in self.optional:
            return self.optional["title"]
        return None

    def set_content_provider(self, content):
        self.set_options(content.get_meta_data())
        self.set_images(content.get_images())
        self.set_data(content.get_text_data())

    def set_file_source(self, file_path):
        with open(file_path, "rb") as file:
            self.set_data(file.read())

    def set_data(self, data):
        # data = data.decode('utf-8')
        data = CharacterEntities.convert(data)
        # data = data.encode('utf-8')
        # self.source = data.decode('utf-8').encode('ISO-8859-1', 'ignore')
        self.source = data
        self.prc = None

    def set_images(self, data):
        self.images = data
        self.prc = None

    def set_options(self, options):
        self.optional = options
        self.prc = None

    def prepare_prc(self):
        if self.source is None:
            raise Exception("No data set")

        if self.prc is not None:
            return self.prc

        data = self.source
        data_len = len(data)

        settings = Settings(self.optional)
        record_factory = RecordFactory(settings)
        data_records = record_factory.create_records(data)
        num_records = len(data_records)
        mobi_header = PalmRecord(settings, data_records, num_records, data_len, len(self.images))
        data_records.insert(0, mobi_header)
        data_records.extend(self.images)
        data_records.append(record_factory.create_flis_record())
        data_records.append(record_factory.create_fcis_record(data_len))
        data_records.append(record_factory.create_eof_record())

        self.prc = Prc(settings, data_records)
        return self.prc

    def save(self, filename):
        prc = self.prepare_prc()
        prc.save(filename)

    def download(self, name):
        prc = self.prepare_prc()
        data = prc.serialize()
        length = len(data)

        if self.debug:
            return

        # # In Python, you typically return the file content and set the appropriate HTTP headers using a web framework.
        # # Below is a simplified example of returning the file content as a response.

        # # Assuming you're using a web framework like Flask, you can do:
        # from flask import Flask, Response

        # app = Flask(__name__)

        # @app.route("/download")
        # def download_mobi():
        #     response = Response(data, content_type="application/x-mobipocket-ebook")
        #     response.headers["Content-Disposition"] = f'attachment; filename="{name}"'
        #     response.headers["Content-Transfer-Encoding"] = "binary"
        #     response.headers["Accept-Ranges"] = "bytes"
        #     response.headers["Cache-Control"] = "private"
        #     response.headers["Pragma"] = "private"
        #     response.headers["Expires"] = "Mon, 26 Jul 1997 05:00:00 GMT"
        #     response.headers["Content-Length"] = str(length)
        #     return response

        # app.run()

# if __name__ == "__main__":
#     mobi = MOBI()

#     # Example usage:
#     # mobi.set_file_source("path/to/your/file.html")
#     # mobi.set_options({"title": "Insert title here", "author": "Author"})
#     # mobi.save("output.mobi")
#     # mobi.download("output.mobi")
