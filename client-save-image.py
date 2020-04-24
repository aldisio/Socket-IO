import time
import socketio
import cv2
import base64
from datetime import datetime

sio = socketio.Client(engineio_logger=True)
start_timer = None

def send_frame():
    global start_timer
    image = cv2.imread('pikachu.png')
    retval, buffer = cv2.imencode('.jpg', image)
    imgbase64 = base64.b64encode(buffer).decode("utf-8")

    start_timer = time.time()
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = 'log_server/'+timestamp+'_image.jpg'

    message = {'frame': imgbase64, 'path2save': filename}
    sio.emit('save_frame', message)
    print('[PYTHON]: Client Socket: Sent to server')

@sio.event
def connect():
    print('[PYTHON]: Client Socket: connected to server')
    send_frame()

@sio.event
def confirm_from_server():
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    sio.sleep(1)
    send_ping()

if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.wait()