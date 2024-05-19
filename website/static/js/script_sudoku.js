// Variable, um die ausgewählte Zahl zu speichern
var numSelected = null;

// Variable, um die ausgewählte Kachel zu speichern
var tileSelected = null;

// Variable, um die Anzahl der Fehler zu speichern
var errors = 0;

// Startkonfiguration für das Sudoku-Brett
var board = [
    "-874916-5",
    "241-68379",
    "56-3274-8",
    "7-861-234",
    "123--459-",
    "-9625--87",
    "93-17685-",
    "6758-2941",
    "8-29457-3"
];

// Lösung für das Sudoku-Brett
var solution = [
    "387491625",
    "241568379",
    "569327418",
    "758619234",
    "123784596",
    "496253187",
    "934176852",
    "675832941",
    "812945763"
];

// Funktion, die ausgeführt wird, wenn die gesamte Seite geladen ist, und setGame() aufruft
window.onload = function () {
    setGame();
};

// Funktion, um das Spiel einzurichten
function setGame() {
    // Fehler auf 0 setzen
    errors = 0;

    // Ausgewählte Zahl und Kachel zurücksetzen
    numSelected = null;

    // Fehlermeldung auf "Errors: 0" setzen
    document.getElementById("errors").innerText = "Errors: 0";

    // Spielcontainer anzeigen und Endbildschirm ausblenden
    document.getElementById("game-container").style.display = "block";
    document.getElementById("end-screen").style.display = "none";

    // Zahlenauswahl und Sudoku-Brett leeren
    document.getElementById("digits").innerHTML = "";
    document.getElementById("board").innerHTML = "";

    // Zahlen 1-9 als Spieloptionen erstellen
    for (let i = 1; i <= 9; i++) {
        let number = document.createElement("div");
        number.id = i;
        number.innerText = i;
        number.addEventListener("click", selectNumber);
        number.classList.add("number");
        document.getElementById("digits").appendChild(number);
    }

    // Sudoku-Brett 9x9 erstellen
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            let tile = document.createElement("div");
            tile.id = r.toString() + "-" + c.toString();

            if (board[r][c] != "-") {
                tile.innerText = board[r][c];
                tile.classList.add("tile-start");
            }

            if (r == 2 || r == 5) {
                tile.classList.add("horizontal-line");
            }

            if (c == 2 || c == 5) {
                tile.classList.add("vertical-line");
            }

            tile.addEventListener("click", selectTile);
            tile.classList.add("tile");
            document.getElementById("board").append(tile);
        }
    }
}

// Funktion, um eine Zahl auszuwählen
function selectNumber() {
    if (numSelected != null) {
        numSelected.classList.remove("number-selected");
    }
    numSelected = this;
    numSelected.classList.add("number-selected");
}

// Funktion, um eine Kachel auszuwählen
function selectTile() {
    if (numSelected) {
        if (this.innerText != "") {
            return;
        }

        let coords = this.id.split("-");
        let r = parseInt(coords[0]);
        let c = parseInt(coords[1]);

        if (solution[r][c] == numSelected.id) {
            this.innerText = numSelected.id;
            checkCompletion();
        } else {
            errors += 1;
            document.getElementById("errors").innerText = "Errors: " + errors;
            if (errors == 3) {
                showEndScreen(false);
            }
        }
    }
}

// Funktion, um zu überprüfen, ob das Spiel abgeschlossen ist
function checkCompletion() {
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (document.getElementById(r + "-" + c).innerText == "") {
                return;
            }
        }
    }
    showEndScreen(true);
}

// Funktion, um den Endbildschirm anzuzeigen
function showEndScreen(success) {
    document.getElementById("game-container").style.display = "none";
    document.getElementById("end-screen").style.display = "block";
    if (success) {
        // Nachricht für den Erfolg anzeigen
        document.getElementById("end-message").innerText = 
    	"Herzlichen Glückwunsch!\n" + 
	"Das System 8 wurde erfolgreich wiederhergestellt.\n" +
	"\n" + 
    	"Um die Daten zu sichern, öffnen Sie die Kamera\n" + 
	"und halten Sie Ihren Daumen für 3 Sekunden hoch 👍,\n" +
    	"um sich zu verifizieren.\n" +
	"\n" + 
	"\n" + 
	"Gehe nun zurück zum Cockpit";
        // Schaltfläche mit Text "Zum Cockpit" und deaktivierter Funktionalität anzeigen
        document.getElementById("end-button").innerText = "Zum Cockpit";
        document.getElementById("end-button").onclick = null; // Button-Funktionalität deaktivieren
    } else {
        // Nachricht für das Scheitern anzeigen
        document.getElementById("end-message").innerText = 
	"\n" + 
	"\n" + 
	"Leider konnte das fehlerhafte System nicht wiederhergestellt werden.\n" + 
	"Versuche es erneut!";
        // Schaltfläche mit Text "Neustart" und Funktion zum Neustarten des Spiels anzeigen
        document.getElementById("end-button").innerText = "Neustart";
        document.getElementById("end-button").onclick = function() {
            restartGame();
        };
    }
}

// Funktion, um das Spiel neu zu starten
function restartGame() {
    setGame();
}

