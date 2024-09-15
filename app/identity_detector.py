

class IdentityDetector:
    """
    Uses an image classifier to predict an identity for a given image. 
    The classifier and the identities must be trained. Info on this process
    yet to come...
    """

    def __init__(self, model_path):
        self.model_path = model_path

    def predict(self, image) -> str:
        return "JOHN DOE" # TODO: build and use classifier
