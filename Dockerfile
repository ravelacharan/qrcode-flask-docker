FROM python:3.12.0a1-buster
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    adduser flaskscript
ENV PATH="/home/flaskscript/.local/bin:${PATH}"
ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=8080
ENV FLASK_DEBUG=TRUE
ENV QR_CODE_FILE_NAME="generated_qrcode.png"
ENV QR_CODE_FILE_PATH="static"
ENV QR_CODE_DATA="https://hub.docker.com/repository/docker/charanravela54/qrcode"
WORKDIR /home/flaskscript
COPY --chown=flaskscript:flaskscript . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["runuser", "-u", "flaskscript", "--", "python3", "-m", "flask", "run", "--host=0.0.0.0"]
