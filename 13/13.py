import imp
import PIL

#negative transformation function
def neg_trans(img):

  #get width and height of image
  width,height=img.size

  #traverse through pixels
  for x in range(width):
    for y in range(height):

      pixel_color=img.getpixel((x,y))

      #if image is RGB, subtract individual RGB values
      if type(pixel_color) == tuple: 

        #s=(L-1)-r
        red_pixel=256-1-pixel_color[0]
        green_pixel=256-1-pixel_color[1]
        blue_pixel=256-1-pixel_color[2]

        #replace the pixel 
        img.putpixel((x,y),(red_pixel,green_pixel,blue_pixel))
      
      #if image is greyscale, subtract pixel intensity
      else:

        #s=(L-1)-r
        pixel_color=256-1-pixel_color 

        #replace the pixel
        img.putpixel((x,y),pixel_color)
  return img

# from PIL import Image
# img = Image.open('disprop.jpg')
# neg_img = neg_trans(img)
# neg_img.save('RGB.jpg')

import xmlrpc.client
conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(conn.phone('Bert'))