
//function that runs when the whole page has loaded and calls setGame()
window.onload= function (){
  document.getElementById('start-button').addEventListener('click', function() {
    mytimer();
    const gaugeElement = document.querySelector(".gauge"); 
    setGaugeValue(gaugeElement, 0)

    // Send request to Flask server
    fetch('/hub', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ "type": "game", "value": "started" })
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
    
    this.removeEventListener("click", arguments.callee)
  });

  document.getElementById('send-data').addEventListener('click', () => {
    const data = document.getElementById('data-input').value;
    fetch('/hub', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"type": "lamps", "value": data })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById("data-lamps-div").style.visibility = "hidden"
            console.log('Operation was successful');
        } else if (data.status === 'failed') {
          document.getElementById("wrong").style.visibility = "visible"
            console.error('Operation failed');
        } else {
            // Handle other status or unexpected response
            console.warn('Unexpected response:', data);
        }
    })
    .catch(error => {
        // Handle network errors or errors in the fetch process
        console.error('Error occurred:', error);
    });
  });
}




// flask 
document.addEventListener("DOMContentLoaded", () => {
  const socket = io();


  socket.on('minecraft_done', () => {
    console.log("MINECRARFT")
    const gaugeElement = document.querySelector(".gauge"); 
    setGaugeValue(gaugeElement, .25)
  });

  socket.on('lamps_start', () => {
    const input_div = document.getElementById("data-lamps-div");
    input_div.style.visibility = "visible"
  });

  socket.on('lamps_done', () => {
    const gaugeElement = document.querySelector(".gauge"); 
    setGaugeValue(gaugeElement, .5)
    const input_div = document.getElementById("data-lamps-div");
    input_div.style.visibility = "hidden"
  });

  socket.on('quiz_done', () => {
    const gaugeElement = document.querySelector(".gauge"); 
    setGaugeValue(gaugeElement, .75)
  });

  socket.on('sudoku_done', () => {
    const gaugeElement = document.querySelector(".gauge"); 
    setGaugeValue(gaugeElement, 1)
  });

  socket.on('rfid_scanned', (data) => {
    if (data.open === 'quiz') {
      window.open('/quiz', '_blank').focus();
    } else if (data.open === 'sudoku') {
      window.open('/sudoku', '_blank').focus();
      console.log('Received data for another game:', data.open);
    } else if (data.open === 'scratch') {
      window.open('https://scratch.mit.edu/projects/1013763026/fullscreen/', '_blank').focus();
      console.log('Received data for another game:', data.open);
    }
  });


});


//progress bar
function setGaugeValue(gauge, value) {
    
  //value is between 0 and 1
  //invalid values
  if (value < 0 || value > 1) {
    return;
  }
  //to set rotation of actual fill
  gauge.querySelector(".gauge__fill").style.transform = `rotate(${
    value / 2 //turn between 0 and 0.5, 0.5 turn means 100% fill -->divide by 2
  }turn)`;


  gauge.querySelector(".gauge__cover").textContent = `${Math.round( //rounding value
    value * 100 //for example value 0.25 means 25% progress
  )}%`; //to have % sign 
}


//Timer
function mytimer(){
  document.getElementById("start-button").style.visibility = "hidden";

  //set the time for the timer
  var timeleft=1200; //20 minutes in seconds

  //progress bar:
  var progressBar=document.getElementById("timer");

        //make downloadTimer() function
        //setInterval() to make the function run every second (1000 milliseconds)
        var downloadTimer = setInterval(function() {
            if(timeleft <= 0) {
                //stops executing downloadTimer
                clearInterval(downloadTimer);

                //to display the output to users:
                //text content of element with ID "countdown" changed:
                //.getElementById: to "grab" HTML-element by its ID
                //.innerHTML: changes text content within this element
                document.getElementById("countdown-text").innerHTML="TIME UP!";
            } else {
    
                //Remaining minutes:
                var minutes= Math.floor(timeleft/60);
                //remaining seconds
                var seconds= timeleft%60;
                
                document.getElementById("countdown-text").innerHTML="noch ausreichend für " + minutes +" Minuten und "+ seconds + " Sekunden";
                
                //update progress bar: 
                progressBar.value=timeleft;
            }
            timeleft -= 1;

        },1000);
        

}

