import eventlet
import socketio
from datetime import datetime
import time
import base64

with open('pikachu.png', 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read())

sio = socketio.Server()
app = socketio.WSGIApp(sio)

starting = False
def worker(sio, sid):
    global encoded_string,ClientsOn 
    while sid in ClientsOn:
        print('[PYTHON]: Sending data to '+str(sid))
        #sio.emit('responseClient', {'data':' Hi '+str(sid)+'! It is '+datetime.now().strftime("%Y%m%d%H%M%S")},room=sid)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        message = {'frame':encoded_string, 
                    'infractionType':1, 
                    'datetime':timestamp};
        
        sio.emit('responseClient', message, room=sid)
        sio.sleep(5) 

ClientsOn = []
@sio.event
def connect(sid, environ):
    ClientsOn.append(sid)
    sio.start_background_task(worker, sio, sid)    
    print('[PYTHON]: Socket ', sid, ' connected!')
    
@sio.event
def disconnect(sid):
    ClientsOn.remove(sid)
    print('[PYTHON]: Socket ', sid, ' disconneted!')

if __name__ == '__main__':
    #from gevent import monkey
    #monkey.patch_all()
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)