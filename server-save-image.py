import eventlet
import socketio
from datetime import datetime
import time
import base64
import cv2
import io
import numpy as np

sio = socketio.Server()
app = socketio.WSGIApp(sio)

starting = False
ClientsOn = []

@sio.event
def connect(sid, environ):
    ClientsOn.append(sid)
    #sio.start_background_task(worker, sio, sid)    
    print('[PYTHON]: Server Socket ', sid, ' connected!')

@sio.event
def save_frame(sid, data):
    #ClientsOn.append(sid)
    #sio.start_background_task(worker, sio, sid)    

    base64_data = data["frame"]
    filename = data["path2save"]

    print('[PYTHON]: Server Socket ', sid, ' received!')
    print('[PYTHON]: Server Socket ', base64_data)

    imgdata = base64.b64decode(base64_data)
    with open(filename, 'wb') as f:
        f.write(imgdata)

@sio.event
def disconnect(sid):
    ClientsOn.remove(sid)
    print('[PYTHON]: Server Socket ', sid, ' disconneted!')

if __name__ == '__main__':
    #from gevent import monkey
    #monkey.patch_all()
    eventlet.wsgi.server(eventlet.listen(('localhost', 5000)), app)