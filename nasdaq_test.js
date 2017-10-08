var WebSocket = require('ws');
var ws = new WebSocket("ws://34.214.11.52/stream?symbol=NDAQ&start=20170101&end=20170201");

process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', function(message) {
  message = message.trim();
  console.log("Hello")
  console.log(ws.send(message, console.log.bind(null, 'Sent : ', message)));
  console.log("F")
});

ws.on('message', function(message) {
  console.log('Received: ' + message);
});

ws.on('close', function(code) {
  console.log('Disconnected: ' + code);
});

ws.on('error', function(error) {
  console.log('Error: ' + error.code);
});