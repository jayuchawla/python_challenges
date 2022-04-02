import enum
from tokenize import triple_quoted
from PIL import Image
import requests
from io import BytesIO


img = Image.open('wire.png')

PIXELS = list()
for x in range(img.width):
    pixel = img.getpixel((x,0))
    PIXELS.append(pixel)
# PIXELS = list(enumerate(PIXELS))



def get_pixels(N):
    pixels = list()
    for n in range(N,N//2,-1):
        spiral_n = list()
        # traverse right
        for x in range(N-n,n):
            spiral_n.append((x, N-n))
        # traverse down
        for y in range(N-n+1,n):
            spiral_n.append((n-1, y))
        # traverse left
        for x in range(n-2,N-n-1,-1):
            spiral_n.append((x, n-1))
        # traverse up
        for y in range(n-2,N-n,-1):
            spiral_n.append((N-n, y))
        pixels.append(spiral_n)
    return pixels
    
def spiral(img_size):
    im = Image.new("RGB", img_size, "#000000")
    spiral_pixels = get_pixels(img_size[0])
    
    original_pixel_index = 0
    for spiral_index in spiral_pixels:
        for pixel in spiral_index:
            im.putpixel(pixel, PIXELS[original_pixel_index])
            original_pixel_index+=1
    im.save('temp.jpg')

spiral((100,100))