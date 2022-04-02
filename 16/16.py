from PIL import Image
img = Image.open('mozart.jpg')

pixels = list()
for y in range(img.height):
    for x in range(img.width):
        pixel = img.getpixel((x,y))
        pixels.append(pixel)

# 8 bit color used!!!!!!!!!!
pink_dashes_in_line = list()
pink_dashes = list()
for y in range(img.height):
    l = list()
    for x in range(img.width):
        if x < img.width - 6:
            pixel = img.getpixel((x,y))
            if img.getpixel((x+1,y)) == img.getpixel((x+2,y)) == img.getpixel((x+3,y)) == img.getpixel((x+4,y)) == img.getpixel((x+5,y)):
                pink_dashes.append((x,y))
                l.append((x,y))
    pink_dashes_in_line.append(l)

import numpy as np
pixels_shift = list()
im = Image.new("P", (640,480), "#000000")
for row_index in range(len(pink_dashes_in_line)):
    new_pixel = pink_dashes_in_line[row_index][0]
    row_data = np.array(pixels[row_index*img.width:row_index*img.width+img.width])
    row_data_shift = np.roll(row_data, -new_pixel[0])
    pixels_shift.append(row_data_shift.tolist())

for y in range(im.height):
    for x in range(im.width):
        im.putpixel((x,y), pixels_shift[y][x])

im.save('temp.gif')