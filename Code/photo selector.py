import os
import PIL
from os import listdir
from PIL import Image

folder_dir = "C:/Users/anhhu/OneDrive/Documents/PerfectIB/IB Mathematics/Worksheet Generator"

codes = ["A0112", "A0312", "A0213"]
question = []

for i in range(len(codes)):
    question.append(codes[i] + ".png")


# question = ["A0112.png", "A0312.png", "A0213.png"]

for images in os.listdir(folder_dir):
    if images in question:
        img = Image.open(images)
        img.show()
