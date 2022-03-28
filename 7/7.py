from urllib import response
from PIL import Image
import requests
from io import BytesIO
import numpy as np

response = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
img = Image.open(BytesIO(response.content))

middle_row = [img.getpixel((x, img.height/2)) for x in range(img.width)]

middle_row_same_rgb = [pixel for pixel in middle_row if pixel[0] == pixel[1] == pixel[2]]
middle_row_same_rgb_single = [r for r,g,b,a in middle_row_same_rgb]
ord_list = list(map(chr, middle_row_same_rgb_single))
ord_list.insert(0, 's')
ord_list.insert(0, 's')
print(''.join(ord_list[::7]))

next_puzzle = [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_puzzle_chr = [chr(num) for num in next_puzzle]
print(''.join(next_puzzle_chr))