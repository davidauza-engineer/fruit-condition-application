from domains.domain import Domain
from PIL import Image as img


class Image(Domain):
    def __init__(self, path):
        self.path = path

    def is_valid(self):
        try:
            image = img.open(self.path)
        except:
            return False

        return image.format.lower() in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']
