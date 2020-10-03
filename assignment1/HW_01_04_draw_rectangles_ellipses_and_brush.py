import numpy as np
import cv2
import random
import itertools

# Global variables
mouse_is_pressed = False
drawing_modes = ['rectangles', 'ellipses', 'brush']
mouse_start_x = -1
mouse_start_y = -1
color = (255, 255, 255)

# Mouse event callback
def mouse_callback(event, x, y, flags, param):
    global mouse_is_pressed, mouse_start_x, mouse_start_y, color, img_color, pre_img, next_img, last_img

    # Left button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Flag on
        mouse_is_pressed = True

        # Record the mouse position
        mouse_start_x = x
        mouse_start_y = y

        # Pick a random color
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
    
    # Mouse dragged
    elif event == cv2.EVENT_MOUSEMOVE:
        if mouse_is_pressed:
            if drawing_mode is 'rectangles':
                # Make the image black
                img_color = next_img - pre_img
                # Restore the previous image
                img_color |= last_img
                # Draw a rectangle
                next_img = cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)
                # Store the image for the next callback
                pre_img = next_img  
            elif drawing_mode is 'ellipses':
                # Make the image black
                img_color = next_img - pre_img
                # Restore the previous image
                img_color |= last_img
                # Draw an ellipse
                cv2.ellipse(img_color, (mouse_start_x, mouse_start_y), (np.abs(mouse_start_x-x), np.abs(mouse_start_y-y)), 0, 0, 360, color, -1)
                # Store the image for the next callback
                pre_img = next_img
            elif drawing_mode is 'brush':
                # Brush
                cv2.circle(img_color, (x, y), 5, color, -1)
            
    # Left button released
    elif event == cv2.EVENT_LBUTTONUP:
        # Flag off
        mouse_is_pressed = False
        if drawing_mode is 'rectangles':
            # Draw a rectangle
            next_img = cv2.rectangle(img_color, (mouse_start_x, mouse_start_y), (x, y), color, -1)
            # Store the image when left button released
            last_img = next_img
        elif drawing_mode is 'ellipses':
            # Draw an ellipse
            next_img = cv2.ellipse(img_color, (mouse_start_x, mouse_start_y), (np.abs(mouse_start_x-x), np.abs(mouse_start_y-y)), 0, 0, 360, color, -1)
            # Store the image when left button released
            last_img = next_img
        elif drawing_mode is 'brush':
            # Brush
            cv2.circle(img_color, (x, y), 5, color, -1)

# Create a black image
rows = 480
cols = 640
img_color = np.zeros((rows, cols, 3), np.uint8)

# Store the images
pre_img = img_color
next_img = img_color
last_img = img_color

# Toggle
toggle = itertools.cycle(drawing_modes).__next__
drawing_mode = toggle()

# Create a window
winname = 'Mouse Events'
cv2.namedWindow(winname)

# Register the mouse callback function
cv2.setMouseCallback(winname, mouse_callback)

# Infinite loop
while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27: break
    elif key == ord('m'):
        drawing_mode = toggle()

cv2.destroyAllWindows()