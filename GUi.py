import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

# Function to capture image from camera
def capture_image():
    ret, frame = cap.read()  # Capture frame from camera
    if ret:
        # Convert BGR image to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Resize the frame to fit the display
        frame = cv2.resize(frame, (320, 240))
        # Convert the frame to ImageTk format
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        # Display the captured image
        label_captured.config(image=photo)
        label_captured.image = photo  # Keep a reference to avoid garbage collection

# Function to process the captured image
def process_image():
    ret, frame = cap.read()  # Capture frame from camera
    if ret:
        # Convert BGR image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply median blur to remove noise
        blur = cv2.medianBlur(gray, 7)
        # Apply adaptive thresholding
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        # Convert the thresholded image to color
        frame_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
        
        # Combine original and processed images side by side
        combined_image = np.hstack((frame, frame_edge))
        
        # Convert the combined image to ImageTk format
        photo = ImageTk.PhotoImage(image=Image.fromarray(combined_image))
        # Display the combined image
        label_processed.config(image=photo)
        label_processed.image = photo  # Keep a reference to avoid garbage collection

# Create main Tkinter window
root = tk.Tk()
root.title("Image Capture and Processing")

# Create labels for displaying captured and processed images
label_captured = tk.Label(root)
label_captured.grid(row=0, column=0, padx=10, pady=10)
label_processed = tk.Label(root)
label_processed.grid(row=0, column=1, padx=10, pady=10)

# Create buttons for capturing and processing images
btn_capture = tk.Button(root, text="Capture Image", command=capture_image)
btn_capture.grid(row=1, column=0, padx=10, pady=10)
btn_process = tk.Button(root, text="Process Image", command=process_image)
btn_process.grid(row=1, column=1, padx=10, pady=10)

# Open the camera
cap = cv2.VideoCapture(0)

# Start the Tkinter event loop
root.mainloop()

# Release the camera
cap.release()
