import serial.tools.list_ports
import pyautogui
from PIL import Image
import time
from win32gui import GetWindowText, GetForegroundWindow


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []


hearts: int = 0
last_hearts: int = 10

# hearts screenshot location and size
heartsImg_x: int = 1008
heartsImg_y: int = 1323
heartsImg_length: int = 243       # Make sure image is right up against hearts
heartsImg_height: int = 27

for one in ports:
    portsList.append(str(one))

com = 5   # Select Com Port for Arduino

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()


def get_hearts() -> None:
    pyautogui.screenshot("hearts.png", region=(1008, 1323, 243, 27))


def rgb_of_pixel(x, y):
    im = Image.open("hearts.png").convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a


time.sleep(3)  # Start time

# 24 = how wide (in pixels each heart)
# 15 = a little more than half a heart (in pixels, to count half heart as full; make less than 12 to not count hearts)
# 10 = ends up in the top half (vertically, in pixels of image) of heart to avoid shading
while True:
    if "Minecraft" in GetWindowText(GetForegroundWindow()):
        get_hearts()
        hearts = 0
        mainHeartColor = rgb_of_pixel(24 - 15, 10)
        for i in range(10):
            heartColor = rgb_of_pixel((i + 1) * 24 - 15, 10)
            if heartColor == mainHeartColor:  # Code made by
                hearts += 1
            else:
                break
        if last_hearts != hearts:
            command = str(hearts)
            serialInst.write(command.encode('utf-8'))
            last_hearts = hearts
        time.sleep(1.2)  # doesn't work with lower time - probably an arduino (memory?) issue; feel free to experiment
