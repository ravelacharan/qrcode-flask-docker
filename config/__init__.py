"""This file conatians project configuration details"""
import os


class Config:
    """QR Code generator config"""

    TEXT_FONT = "font/Open_Sans/OpenSans-VariableFont_wdth,wght.ttf"
    IMAGE_WATER_MARK = "Charan Ravela"
    TITLE="QR Code Generator"
    QR_CODE_FILE_NAME = os.environ.get("QR_CODE_FILE_NAME")
    QR_CODE_FILE_PATH = os.environ.get("QR_CODE_FILE_PATH")
    QR_CODE_DATA = os.environ.get("QR_CODE_DATA")
