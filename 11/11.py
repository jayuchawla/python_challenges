import numpy as np
from io import BytesIO
import requests
from PIL import Image

response = requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg')
# img = Image.open(BytesIO(response.content))
img = Image.open('cave.jpg')

even = list()
odd = list()
for y in range(0, img.height, 2):
    for x in range(0, img.width, 2):
        even.append(img.getpixel((x,y)))
        odd.append(img.getpixel((x+1,y+1)))

print(img.size)
print(len(even))
print(len(odd))

even_2d = list()
for row in range(0, len(even), int(img.width/2)):
    even_2d.append(even[row:row+int(img.width/2)])
even_2d = np.array(even_2d, dtype=np.uint8)
new_image = Image.fromarray(even_2d)
new_image.save('new_even.png')

odd_2d = list()
for row in range(0, len(odd), int(img.width/2)):
    odd_2d.append(odd[row:row+int(img.width/2)])
odd_2d = np.array(odd_2d, dtype=np.uint8)
new_image = Image.fromarray(odd_2d)
new_image.save('new_odd.png')
