
//function that runs when the whole page has loaded and calls setGame()
window.onload= function (){
  document.getElementById('start-button').addEventListener('click', function() {
    mytimer();
    this.removeEventListener("click", arguments.callee)
  });
}


// flask 
document.addEventListener("DOMContentLoaded", () => {
  const socket = io();


  socket.on('change_button_color', () => {
      const button = document.getElementById('minecraft_done');
      button.style.backgroundColor = 'green';
  });

  socket.on('rfid_scanned', (data) => {
    console.log("S")

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

