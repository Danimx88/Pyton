"""compresor de imagenes"""
from PIL import image # python3 -m pip install Pillow

import os

downloadsFolder = "/User/danielr/Downloads"

if __name__ == ""__main__":
  for filename in os.listdor(downloadsFolder):
      name, extension = os.path.splitext(downloadsFolder + filename)


    if extension in [".jpg", ".jpeg", ".png"]:
      picture = image.open(downloadsFolder + filename)
      picture.save(downloadsFolder + "compressed_" +filename, optimize=True, quality=55)
