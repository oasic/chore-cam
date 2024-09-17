import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector

class PhotoGrabber:
    """A class to extract photos from a webcam"""

    def __init__(self):
        self.capture = cv2.VideoCapture(0) # initialize webcam
        # Initialize the FaceDetector object
        # minDetectionCon: Minimum detection confidence threshold
        # modelSelection: 0 for short-range detection (2 meters), 1 for long-range detection (5 meters)
        self.detector = FaceDetector(minDetectionCon=0.5, modelSelection=0)
        self.debug = True

    def get_photo(self):
        success, img = self.capture.read()

        if not success:
            print("Error: Failed to capture image.")
            return None

        # Detect faces in the image
        # img: Updated image
        # bboxs: List of bounding boxes around detected faces
        img, bboxs = self.detector.findFaces(img, draw=False)

        # Check if any face is detected
        if self.debug and bboxs:
            # Loop through each bounding box
            for bbox in bboxs:
                # bbox contains 'id', 'bbox', 'score', 'center'

                # ---- Get Data  ---- #
                center = bbox["center"]
                x, y, w, h = bbox['bbox']
                score = int(bbox['score'][0] * 100)

                # ---- Draw Data  ---- #
                cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)
                cvzone.putTextRect(img, f'{score}%', (x, y - 10))
                cvzone.cornerRect(img, (x, y, w, h))

        # Display the frame
        cv2.imshow('Webcam', img)
        return img


    def release(self):
        # Release the webcam and close windows
        self.capture.release()
        cv2.destroyAllWindows()

