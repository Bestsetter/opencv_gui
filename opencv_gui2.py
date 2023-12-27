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

    def rotate(self, angle):
        (h, w) = self.image.shape[:2]
        center = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated_image = cv2.warpAffine(self.image, M, (w, h))
        self.show_image('Rotated Image', rotated_image)

    def flip(self, flip_code):
        flipped_image = cv2.flip(self.image, flip_code)
        self.show_image('Flipped Image', flipped_image)

    def resize(self, width, height):
        resized_image = cv2.resize(self.image, (width, height))
        self.show_image('Resized Image', resized_image)

if __name__ == "__main__":
    editor = ImageEditor()
    editor.crop(50, 50, 250, 250)
    editor.rotate(45)
    editor.flip(1)
    editor.resize(300, 300)