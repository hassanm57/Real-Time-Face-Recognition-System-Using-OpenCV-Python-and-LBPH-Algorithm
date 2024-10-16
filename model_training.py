import cv2
import numpy as np
from PIL import Image
import os

# Initialize the recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

def getImageID(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for imagePath in imagePaths:
        # Open the image and convert to grayscale
        faceImage = Image.open(imagePath).convert('L')
        # Resize the image to a standard size (e.g., 200x200)
        faceImage = faceImage.resize((200, 200), Image.LANCZOS)
        # Convert the image to a numpy array
        faceNP = np.array(faceImage, 'uint8')
        # Get the ID from the filename
        id = int(os.path.split(imagePath)[-1].split(".")[0])
        # Append the face and ID to the lists
        faces.append(faceNP)
        ids.append(id)
        # Display the image for verification
        cv2.imshow("Training", faceNP)
        cv2.waitKey(1)
    return ids, faces

ids, facedata = getImageID(path)



# Ensure the IDs are in the correct format
ids = np.array(ids, dtype=np.int32)

# Train the recognizer
recognizer.train(facedata, ids)
recognizer.write("Trainer.yml")
cv2.destroyAllWindows()
print("Training Complete")
