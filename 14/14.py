import enum
from tokenize import triple_quoted
from PIL import Image
import requests
from io import BytesIO

# # response = requests.get('http://www.pythonchallenge.com/pc/return/wire.png')

# # print(pixels[9999])
# # print(pixels[99])
# # print(pixels[98])
# # print(pixels[98])
# # print(pixels[97])

# # remove red pixels
# temp = list()
# for pixel in pixels:
#     temp.append(pixel) if pixel[1][0] < 200 else None
# pixels = temp

# # remove white/gray pixels
# temp = list()
# for pixel in pixels:
#     temp.append(pixel) if pixel[1][0] <= 80 else None
# pixels = temp

# # darkest pixels
# temp = list()
# for pixel in pixels:
#     temp.append(pixel) if pixel[1][0] <= 70 else None
# pixels = temp

# print(pixels)
# print(pixels[-1])

# s_p = sorted(pixels, key=lambda x: x[1][0])

# print(s_p[0])
# print(len(pixels))
# pixels_filtered = list()
# for x in range(img.width):

#     pixels.append(img.getpixel((x,0)))

# print(len(pixels))
# print(pixels[100:200])
# print(list(enumerate(pixels[:100])))

# pixels_enum = list(enumerate(pixels))
# bars = list()
# current_elem = 0
# bars.append(list())

# for pixel in pixels_enum:
#     if pixel[1][0] >= 70 and pixel[1][0] < 80:
#         if len(bars[current_elem]) == 0:
#             bars[current_elem].append(pixel)
#     elif len(bars[current_elem]) > 0:
#         current_elem += 1
#         bars.append(list())

# # for bar in bars:
#     # print(len(bar))
# print(bars)

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
            # print(pixel)
            # print(PIXELS[original_pixel_index])
            im.putpixel(pixel, PIXELS[original_pixel_index])
            # im[pixel[0], pixel[1]] = PIXELS[original_pixel_index]
            original_pixel_index+=1
    
        # traverse right
        # for x in range(0:)
    im.save('temp.jpg')

spiral((100,100))
# print(list(range(5,1,-1)))
# print(get_pixels(100))