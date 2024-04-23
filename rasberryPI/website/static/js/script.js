// script.js
console.log('JAVASCRIPT IST GELADEN LOL')



const socket = io('ws://127.0.0.1:5000');


socket.on('connect', () => {
    console.log('Connected to WebSocket server');
});

socket.on('minecraft_done', (data) => {
    console.log(data)
    let code = data.data
    document.getElementById('testField').innerHTML = code
    document.getElementById('minecraft_done').style.backgroundColor = 'green'
});

socket.on('minecraft_connected', (data) => {
    console.log(data)
    document.getElementById('minecraft_connected').style.backgroundColor = 'green';
});