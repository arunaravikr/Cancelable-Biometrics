import cv2
import numpy as np

# Load the two images to compare
img1 = cv2.imread('images/sap.bmp', 0)  # Load image in grayscale
img2 = cv2.imread('images/aruna1.bmp', 0)

# Resize the images to a fixed size for consistency
img1 = cv2.resize(img1, (300, 300))
img2 = cv2.resize(img2, (300, 300))

# Compute the Mean Squared Error (MSE) between the two images
mse = np.mean((img1 - img2) ** 2)

# Print the similarity score
if mse < 500:  # Set a threshold value to determine if the images are the same
    print("The fingerprint images are the same.")
else:
    print("The fingerprint images are not the same.")
