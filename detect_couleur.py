import pymouse
import pyscreenshot as ImageGrab

if __name__=='__main__':
    mouse = pymouse.PyMouse()
    print "Mouse position : "
    print(mouse.position())
    image = ImageGrab.grab()
    print image.getpixel((mouse.position()[0],mouse.position()[1]))
