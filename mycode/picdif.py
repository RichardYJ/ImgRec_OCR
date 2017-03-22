import Image
import ImageChops

im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')

diff = ImageChops.difference(im1, im2).getbbox()
print 'is: ' + str(diff)#a + b +