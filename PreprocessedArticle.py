import json
import io
from PIL import Image
import requests

class PreprocessedArticle:
    def __init__(self, text_data, image_links, metadata):
        self.text = text_data
        self.metadata = metadata
        self.images = self.download_images(image_links)

    @staticmethod
    def create_from_json(json_str):
        data = json.loads(json_str)
        return PreprocessedArticle(data["text"], data["images"], data["metadata"])

    def get_text_data(self):
        return self.text

    def get_images(self):
        return self.images

    def get_metadata(self):
        return self.metadata

    def download_images(self, links):
        images = {}
        img_counter = 0

        for link in links:
            response = requests.get(link)
            img_file = Image.open(io.BytesIO(response.content))

            if img_file.mode != "RGB":
                img_file = img_file.convert("RGB")

            img_buffer = io.BytesIO()
            img_file.save(img_buffer, format="JPEG")
            img_data = img_buffer.getvalue()
            img_buffer.close()

            images[img_counter] = img_data
            img_counter += 1

        return images
