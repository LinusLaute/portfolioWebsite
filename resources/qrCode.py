import qrcode
from qrcode.image.svg import SvgPathImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://llautenschlager.me/')
qr.make(fit=True)

# Create white QR code on transparent background
img = qr.make_image(
    image_factory=SvgPathImage,
    fill_color="white",  # QR pattern in white
    back_color="transparent"  # Transparent background
)

img.save('qr_white.svg')