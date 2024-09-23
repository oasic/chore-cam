import os
import time

import typer
import cv2

from app.actions import actions
from app.photo_grabber import PhotoGrabber
from app.identity_detector import IdentityDetector

app = typer.Typer()

# states
START = 'start'
ACTIVE = 'active'

@app.command()
def photos(directory: str):
    """
    Saves 1 photo every 1/2 seconds in the given directory till 20 photos are saved
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory {directory}")
    if directory.endswith('/'):
        directory = directory[:-1]
    photo_grab = PhotoGrabber()
    photo_grab.debug = False
    i = 0
    while i < 20:
        filename = f'{directory}/photo_{i}.jpg'
        cv2.imwrite(filename, photo_grab.get_photo())
        if should_exit(500):
            break

        i+=1
    photo_grab.release()

@app.command()
def run():
    """
    Entry point into the application. Press 'q' to quit.
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
    # typer.run(main)
    app()
