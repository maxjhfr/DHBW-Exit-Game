document.addEventListener("DOMContentLoaded", () => {
    const socket = io();


    socket.on('change_button_color', () => {
        const button = document.getElementById('minecraft_done');
        button.style.backgroundColor = 'green';
    });

    socket.on('rfid_scanned', () => {
        
    });



    //event listener when send button gets hit and sends message to flask
    document.getElementById('send-data').addEventListener('click', () => {
        const data = document.getElementById('data-input').value;
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ data: data })
        });
    });

    
});
