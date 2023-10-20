from PIL import Image, ImageOps
import requests
from io import BytesIO


class ImageHandler:
    @staticmethod
    def download_image(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP request errors

            img_data = response.content
            img = Image.open(BytesIO(img_data))

            return ImageHandler.create_image(img)
        except Exception as e:
            return False

    @staticmethod
    def create_image(img):
        try:
            grayscale_img = ImageOps.grayscale(img)

            img_byte_array = BytesIO()
            grayscale_img.save(img_byte_array, format="JPEG")
            image_data = img_byte_array.getvalue()

            return image_data
        except Exception as e:
            return False
