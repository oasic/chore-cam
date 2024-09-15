import cv2


class PhotoGrabber:
    """A class to extract photos from a webcam"""

    def __init__(self):
        self.capture = cv2.VideoCapture(0) # initialize webcam

    def get_photo(self):
        ret, frame = self.capture.read()

        if not ret:
            print("Error: Failed to capture image.")
            return None

        # Display the frame
        cv2.imshow('Webcam', frame)
        return frame


    def release(self):
        # Release the webcam and close windows
        self.capture.release()
        cv2.destroyAllWindows()

