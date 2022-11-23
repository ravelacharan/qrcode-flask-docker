"""This is the driver file of the project"""
from qrcode_generator import generate_qr_code
from file_operations import get_current_working_directory, join_path, make_dir
from pil import save_image, watermark
from config import Config
from flask import Flask, request, send_file

app = Flask(__name__)


@app.route("/", methods=['Get'])
def index_get():
    form = f"<!DOCTYPE html>\
            <html>\
            <head>\
                <meta charset='utf-8'>\
                <meta http-equiv='X-UA-Compatible' content='IE=edge'>\
                <title>{Config.TITLE}</title>\
                <meta name='viewport' content='width=device-width, initial-scale=1'>\
                <link rel='stylesheet' type='text/css' media='screen' href='main.css'>\
                <script src='main.js'></script>\
                </head>\
                <body> \
                    <div style='display: flex; flex-direction: column; justify-content: center; align-items: center; align-content: center;'>\
                        <div>\
                            <h1>\
                                Wanna generate QR Code! Check below.\
                            </h1>\
                        </div>\
                        <div style='font-size:28px; border-radius: 5px; background-color: #f2f2f2; padding: 20px;'>\
                            <form method='POST' action='/'>\
                                <label for='qr-data'> QR Code Data: </label>\
                                <input required type='text' id='qr-data' name='qr-data' placeholder = 'https://google.com' style='width: 100%; padding: 12px 20px;margin: 8px 0;display: inline-block;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;'/><br/>\
                                <input type='submit' value='Generate' style='width: 100%;background-color: #4CAF50;color: white;padding: 14px 20px;margin: 8px 0;border: none;border-radius: 4px;cursor: pointer;'/>\
                            </form>\
                        </div>\
                        <p style='font-size:16px;'>Developed By: {Config.IMAGE_WATER_MARK}</p>\
                    </div>\
                </body>\
            </html>"

    return form


@app.route("/", methods=['POST'])
def index_post():
    """Driver function"""

    qr_data = request.form.get("qr-data") or Config.QR_CODE_DATA
    qrcode = generate_qr_code(qr_data)
    destination_path = join_path([get_current_working_directory(), Config.QR_CODE_FILE_PATH, Config.QR_CODE_FILE_NAME])

    for i in range(0, 1):
        while True:
            try:
                qrcode = watermark(qrcode)
                save_image(qrcode, destination_path)

                print("QR Code Generated Successfully!!!\n")
                print("File saved to the path ", destination_path)
            except FileNotFoundError:

                directory_path = join_path([get_current_working_directory(), Config.QR_CODE_FILE_PATH])
                make_dir(directory_path)
                continue

            break

    return send_file(destination_path, mimetype='image/png')
