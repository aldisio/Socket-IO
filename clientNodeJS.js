//AM: Import dependencies
var io = require('socket.io-client');
var socket = io('http://localhost:5000',{transports: [ 'websocket' ], origins:'localhost:* http://localhost:* http://www.localhost:*'});
var Buffer = require('buffer').Buffer;
var fs = require('fs');

var count = 0; // AM: Received files counter

//AM: Connection event
socket.on('connect', function () {
    console.log('[NODEJS]: Socket['+socket.id+'] connected!');
});

//AM: Disconnection event
socket.on('disconnect', (reason) => {
    console.log('Disconnect!')
    console.log(reason)
    if (reason === 'io server disconnect') {
        // the disconnection was initiated by the server, you need to reconnect manually
        socket.connect();
    }
});

socket.on('responseClient', function (data) {  
    console.log('[NODEJS]: Receiving data...'); 

    // AM: Save frame image to disk
    var buff = new Buffer.from(data.frame.toString(), 'base64');
    fs.writeFile("out_node_1/frame_"+count+".png" , buff, function(err){
    if (err){
        return console.log(err);}
        console.log('[NODEJS]: The frame was saved!');
    });

    // AM: Save json to disk
    var message = {infractionType: data.infractionType, datetime: data.datetime};
    var json = JSON.stringify(message);
    fs.writeFile('out_node_1/JSON_'+count+'.json', json, 'utf8', function(err){
    if (err){
        return console.log(err);}
        console.log('[NODEJS]: The JSON was saved!');
    });

    count = count+1;
});
