# Socket-IO repository

This is a example to connect differents applications wrote on different programing languages using a comunication via websocket protocol. In this case, we use two applications: A server wrote in Python3 and a client wrote in NodeJS.

## Requirements
The source python depends:
- dnspython (1.16.0)
- eventlet (0.25.1)
- greenlet (0.4.15)
- monotonic (1.5)
- netifaces (0.10.6)
- pip (8.1.1)
- pkg-resources (0.0.0)
- python-engineio (3.9.3)
- python-socketio (4.3.1)
- setuptools (3.3)
- six (1.12.0)

This dependencies can be installed by the pip3, follow the command:

Create a virtual environment:
```sh
$ python3 -m venv .env
```

Active the virtual environment:
```sh
$ . .env/bin/activate
```
Install requirements by pip:

```sh
$ pip3 install -r requirements_socketio.txt
```

The clinet NodeJS essentially depends the external libraries:
- socket.io-client: ^2.3.0
- buffer: 5.4.3

This dependencies can be installed by the *npm*, follow the command:
Install the socket.io-client:

```sh
$ npm install socket.io-client
```
Install other dependencies via package.json file:
```sh
$ npm install package.json
```

## Usage
To execute server, open a new terminal and execute:
```sh
$ python3 serverPython3.py
```

To execute cliente, open a new terminal and execute:
```sh
$ node clientNodeJS.js
```

## About Socket.IO:
- Python: [python-socketio](https://github.com/miguelgrinberg/python-socketio)
- NodeJS: [socket.io-client](https://www.npmjs.com/package/socket.io-client)