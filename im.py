from PIL import Image, ImageDraw, ImageFont
import random

import os


def get_hand_writting_font():
  src_dir = './font/handwritting'
  font_files = list(
    filter(lambda file: os.path.isfile(file), 
    map(lambda file: "{0}/{1}".format(src_dir, file), 
        os.listdir(src_dir))
  ))  
  index = random.randint(0, len(font_files)-1)
  print(font_files, index)
  return font_files[index]

def draw_border(img):
  (w, h) = img.size
  boxs = [
    [(10, 10), (w - 10, h - 10)],
    [(25, 25), (w - 25, h - 25)]
  ]
  imgDraw = ImageDraw.Draw(img)
  hex_color = "#0E2954"
  color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
  for box in boxs:
    imgDraw.rectangle(box, outline=color , width=5)

  


def generater_img(image_width = 400, image_height = 300):
  # Define the image size and color
  
  image_color = (0, 0, 0, 1)
  # Create a new image with the specified size and color
  image = Image.new('RGBA', (image_width, image_height), image_color)
  draw_border(image)
  font_path = get_hand_writting_font()
  
  font_size = 100
  font = ImageFont.truetype(font_path, font_size)
  imgDraw = ImageDraw.Draw(image)
  imgDraw.text((40, 40), "hi all hjghj", font=font, fill="#0E2954")

  # Save the image to a file
  image.save('generated_image.png')

generater_img()