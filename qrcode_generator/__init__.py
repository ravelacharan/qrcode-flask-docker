"""This file contains qrcode generator functions"""

from qrcode import QRCode
from qrcode.image.pil import PilImage


def generate_qr_code(data: str) -> PilImage:
    """Generate a QR code Image"""

    qrcode = QRCode(version=1, box_size=10, border=5)
    qrcode.add_data(data)
    qrcode.make(fit=True)

    return qrcode.make_image(fill="black", back_color="white")
