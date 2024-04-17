// script.js
const socket = io('ws://localhost:8765');
socket.on('connect', () => {
    console.log('Connected to WebSocket server');
});

socket.on('update_button_color', (data) => {
    // Update button color based on received message
    if (data.color === 'green') {
        document.getElementById('test').style.backgroundColor = 'green';
    }
});

// Send a message to Flask to request a button color change
socket.emit('change_button_color', { color: 'green' });
