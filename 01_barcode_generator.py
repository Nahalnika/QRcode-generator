import pyqrcode
import png
from pyqrcode import QRCode

# put the address of the thing that you want to make a QR code of
address = "https://www.canva.com/bg_bg/?emailConfirmed=true"
url = pyqrcode.create(address)
url.png("Canva.png", scale=8)