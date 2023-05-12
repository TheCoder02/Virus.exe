#notifications library, runs notifications

from plyer import *
from PIL import Image
import pyautogui
from Graphics import *
import socket

"""
def targetScreen():
   im = Image.open("6-0Win.png")
   im.show()   
   im2 = Image.open("dunkedon.png")
   im2.show()
   im3 = Image.open("obama.png")
   im3.show()
   im4 = Image.open("davy1kill.png")
   im4.show()
   im5= Image.open("")
   im5.show()
   im6 = Image.open()
"""
   
   
   
def ip():
   hostname = socket.gethostname()
   ip_address = socket.gethostbyname(hostname)
   print(f"Hostname: {hostname}")
   print(f"IP Address: {ip_address}")


def virusClick():
   notification.notify(
      title = 'Target Sale',
      message = 'Don\'t miss these weekly ad deals.',
      app_icon = 'amc.ico',
      timeout = 10,
   )

