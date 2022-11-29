from domains.domain import Domain
from PIL import Image as img
from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd() + "/assets"


class Image(Domain):
    def __init__(self, path):
        self.path = path

    def is_valid(self):
        try:
            image = img.open(self.path)
        except:
            return False

        return image.format.lower() in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']

    def detect_objects(self):
        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath(os.path.join(execution_path, 'resnet50_coco_best_v2.1.0.h5'))
        detector.loadModel()
        detections, extracted_images = detector.detectObjectsFromImage(
            input_image=os.path.join(execution_path, self.path),
            output_image_path=os.path.join(execution_path, 'result.jpg'),
            extract_detected_objects=True
        )
        return detections, extracted_images
