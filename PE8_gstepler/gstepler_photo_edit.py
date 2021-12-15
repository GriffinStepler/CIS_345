# Griffin Stepler, CIS345, iCourse, PE8
import cv2
from PIL import Image

filename = 'lights1.jpg'
img = cv2.imread(filename)

# showing user image
cv2.namedWindow('My Image')
cv2.moveWindow('My Image', 900, 400)
cv2.imshow('My Image', img)
cv2.waitKey(0)

# creating color variations of image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
color3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
color4 = cv2.cvtColor(img, cv2.COLORMAP_HOT)

# displaying altered images to user, pausing for input
cv2.imshow('Gray Image', gray)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('gray_'+filename, gray)

cv2.imshow('HLS Image', hls)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('hls_' + filename, hls)

cv2.imshow('Cool Map', color3)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('coolmap_'+filename, color3)

cv2.imshow('Hot Map', color4)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('hotmap_'+filename, color4)

# clear screen
cv2.destroyAllWindows()

thumb_nail_size = (128, 128)
thumb_name = 'thumbnail_'+filename

try:
    pic = Image.open(filename)
    pic.thumbnail(thumb_nail_size)
    pic.save(thumb_name, "JPEG")
except IOError:
    print(f'Cannot create thumbnail for {filename}')