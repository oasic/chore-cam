import time

import typer
import cv2

from app.actions import actions
from app.photo_grabber import PhotoGrabber
from app.identity_detector import IdentityDetector


# states
START = 'start'
ACTIVE = 'active'

def main():
    """
    Entry point into the application. Polls the webcam until 'q' key is pressed.
    * read photo
    * check for face
    * if face, then check classifier for who
    * if identity known, run actions and pass identity as dependency
    """
    state = START
    id_detector = IdentityDetector('model.pkl') # placeholder
    photo_grab = PhotoGrabber()
    prev_identity = None
    run_flag = True
    while run_flag:
        identity = id_detector.predict(photo_grab.get_photo())

        if prev_identity is None:
            prev_identity = identity

        if state == START:
            if identity is not None:
                state = ACTIVE
                for action in actions:
                  action.run(identity)
        else: # ACTIVE state
            # if identity change, wait 10s and return to START
            if identity != prev_identity:
                if should_exit(3_0000):
                    run_flag = False
                state = START

        if should_exit():
            run_flag = False

    photo_grab.release()
    #time.sleep(1)

def should_exit(wait_millis: int = 50):
    # wait for exit key press
    key = cv2.waitKey(wait_millis) & 0xFF
    return key == ord('q')


if __name__ == "__main__":
    typer.run(main)
