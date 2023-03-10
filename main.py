import cv2
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import torch

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Create Tkinter window
root = tk.Tk()
root.title("TEST 1")

# Create label for displaying video feed
label = tk.Label(root)
label.pack()


def update_video_feed():
    # Read frame from webcam
    ret, frame = cap.read()

    if ret:
        # Convert OpenCV BGR image to PIL RGB image
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)

        # Convert PIL image to Tkinter PhotoImage
        photo = ImageTk.PhotoImage(image)

        # Update label with new video frame
        label.config(image=photo)
        label.image = photo

    # Schedule next update
    label.after(10, update_video_feed)

# Start updating video feed
update_video_feed()

# Run the GUI event loop
root.mainloop()

# Release video capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
