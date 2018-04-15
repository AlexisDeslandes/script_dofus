import sys
import pyscreenshot as ImageGrab

image = ImageGrab.grab()
x = int(sys.argv[1])
y = int(sys.argv[2])
print image.getpixel((x,y))
