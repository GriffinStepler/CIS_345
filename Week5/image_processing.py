import cv2  # opencv modules
from PIL import Image, ImageFilter  # classes from pillow

filename = '../PE8_gstepler/lights.jpg'
'''
img = cv2.imread(filename)

cv2.namedWindow('My Image')
cv2.moveWindow('My Image', 900, 400)
cv2.imshow('My Image', img)
cv2.waitKey(0)  # this delays the close until a keypress is registered

# grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray)
key = cv2.waitKey(0)
# saving grayscale version of the image 
if key == ord('s'):
    cv2.imwrite('gray_'+filename, gray)
'''

img = Image.open(filename)
# img.show()
sharp = img.filter(ImageFilter.SHARPEN)
# sharp.show()
blur = img.filter(ImageFilter.BLUR)
# blur.show()

img.thumbnail((128, 128))
img.save('thumb_'+filename)

small = img.resize((16,16))
small.save('small_'+filename)
small.show()
