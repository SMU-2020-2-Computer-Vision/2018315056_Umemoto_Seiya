import cv2
import os

# Get the path to the current file
print(dir())
# print(os.path.abspath(__))
cwd = os.path.dirname(os.path.abspath(__file__))
print(cwd)

# Change the working directory
os.chdir(cwd)

# Load an image
img = cv2.imread('messi5.jpg')
print(type(img), img.ndim, img.shape, img.size, img.dtype)

if img is None:
    print("Error: no image found!")

else:

    # Display the image in a window
    cv2.imshow('image', img)

    # Wait for a key to be pressed
    cv2.waitKey(1000)

    # Destroy all windows
    cv2.destroyAllWindows()