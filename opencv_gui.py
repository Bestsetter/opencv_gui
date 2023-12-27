import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

class ImageEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.image_path = filedialog.askopenfilename()
        self.image = cv2.imread(self.image_path)

    def show_image(self, title, image):
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def crop(self, start_y, start_x, end_y, end_x):
        cropped_image = self.image[start_y:end_y, start_x:end_x]
        self.show_image('Cropped Image', cropped_image)

if __name__ == "__main__":
    editor = ImageEditor()
    editor.crop(50, 50, 250, 250)