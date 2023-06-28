from PIL import Image, ImageDraw, ImageFont
import random
from faker import Faker
import os


def get_hand_writting_font():
  src_dir = './font/handwritting'
  font_files = list(
    filter(lambda file: os.path.isfile(file), 
    map(lambda file: "{0}/{1}".format(src_dir, file), 
        os.listdir(src_dir))
  ))  
  index = random.randint(0, len(font_files)-1)
  # print(font_files, index)
  return font_files[index]

def draw_border(img):
  (w, h) = img.size
  boxs = [
    [(5, 5), (w - 5, h - 5)],
    [(10, 10), (w - 10, h - 10)]
  ]
  imgDraw = ImageDraw.Draw(img)
  hex_color = "#0E2954"
  color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))
  for box in boxs:
    imgDraw.rectangle(box, outline=color , width=2)

  


def generater_img(name, job, company, address, image_width = 400, image_height = 150):
  # Define the image size and color
  
  image_color = (0, 0, 0, 1)
  # Create a new image with the specified size and color
  image = Image.new('RGBA', (image_width, image_height), image_color)
  draw_border(image)
  font_path = get_hand_writting_font()
  
  font_size = 20
  font = ImageFont.truetype(font_path, font_size)
  imgDraw = ImageDraw.Draw(image)
  imgDraw.text((20, 20), name, font=font, fill="#0E2954")
  font = ImageFont.truetype(font_path, font_size-4)
  imgDraw.text((20, 42), job, font=font, fill="#0E2954")
  font = ImageFont.truetype(font_path, font_size-8)
  imgDraw.text((20, 54), company, font=font, fill="#0E2954")
  imgDraw.text((20, 70), address, font=font, fill="#0E2954")

  # Save the image to a file
  image.save('generated_image.png')

def main():
  fake = Faker()
  name = fake.name()
  address = "{0}, {1}-{2}".format(fake.street_address(), fake.city(), "3243")
  generater_img(name=name, job=fake.job(), company=fake.company(), address=address)

if __name__ == "__main__":
  main()