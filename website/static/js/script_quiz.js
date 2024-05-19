// Fragen für das Quiz
var questions = [
  {
      question: "Welche der folgenden Datenstrukturen verwendet den Last-In-First-Out (LIFO) Ansatz?",
      options: ["a) Warteschlange (Queue)", "b) Stapel (Stack)", "c) Baum (Tree)", "d) Liste (List)"],
      answer: "b"
  },
  {
      question: "Was ist ein DNS?",
      options: ["a) Ein Dienst, der die Übertragung von Daten zwischen Computern ermöglicht", "b) Ein Protokoll zur sicheren Datenübertragung im Internet", "c) Ein System zur Umwandlung von Domainnamen in IP-Adressen", "d) Eine Hardwarekomponente eines Computers"],
      answer: "c"
  },
  {
      question: "Welches der folgenden Protokolle wird typischerweise für die sichere Übertragung von Daten im Internet verwendet, insbesondere für E-Commerce-Transaktionen?",
      options: ["a) HTTP", "b) FTP", "c) SMTP", "d) HTTPS"],
      answer: "d"
  },
  {
      question: "Was ist ein Compiler?",
      options: ["a) Eine Hardwarekomponente, die Daten in einem Computer speichert", "b) Ein Programm, das Quellcode in Maschinencode übersetzt", "c) Ein Protokoll zur drahtlosen Netzwerkverbindung", "d) Eine Sicherheitssoftware, die Computersysteme vor Viren schützt"],
      answer: "b"
  },
  {
      question: "Welcher Datenstrukturentyp wird typischerweise verwendet, um Daten in einer FIFO (First-In-First-Out) Reihenfolge zu speichern?",
      options: ["a) Stapel (Stack)", "b) Warteschlange (Queue)", "c) Baum (Tree)", "d) Liste (List)"],
      answer: "b"
  },
  {
      question: "Was ist ein 'Heap' in Bezug auf Computerspeicher?",
      options: ["a) Ein Bereich im Speicher, der für temporäre Dateien verwendet wird", "b) Eine Datenstruktur zur Speicherung von Elementen in einer geordneten Folge", "c) Ein Bereich im Speicher, der dynamisch allozierten Speicherplatz enthält", "d) Ein Bereich im Speicher, der für den Kernel des Betriebssystems reserviert ist"],
      answer: "c"
  },
  {
      question: "Was ist der Zweck eines VPN (Virtual Private Network) in einem Netzwerk?",
      options: ["a) Um die Geschwindigkeit der Internetverbindung zu erhöhen", "b) Um den Zugriff auf regionale Inhalte im Internet zu ermöglichen", "c)  Um eine sichere Verbindung über ein öffentliches Netzwerk herzustellen", "d) Um die Anzahl der gleichzeitigen Benutzer im Netzwerk zu erhöhen"],
      answer: "c"
  },
  {
      question: "Welches der folgenden Netzwerkprotokolle wird typischerweise für die Übertragung von E-Mails verwendet?",
      options: ["a) HTTP", "b) FTP", "c) SMTP", "d) SSH"],
      answer: "c"
  }
];

// Initialisiert den Index der aktuellen Frage und die Anzahl der richtigen Antworten
var currentQuestionIndex = 0;
var correctAnswers = 0;

// Startet das Quiz
function startQuiz() {
  // Versteckt den Startbildschirm und zeigt den Fragen-Container
  document.getElementById('start-screen').style.display = 'none';
  document.getElementById('question-container').style.display = 'flex';
  showQuestion();
}

// Zeigt die aktuelle Frage und ihre Antwortmöglichkeiten an
function showQuestion() {
  var question = questions[currentQuestionIndex];
  document.getElementById('question').innerHTML = question.question;
  var optionsHTML = '';
  // Erzeugt die Antwortoptionen als Buttons
  for (var i = 0; i < question.options.length; i++) {
      optionsHTML += '<button class="option" onclick="checkAnswer(\'' + question.options[i] + '\')">' + question.options[i] + '</button>';
  }
  document.getElementById('options').innerHTML = optionsHTML;
  // Versteckt die Benachrichtigung und den "Weiter"-Button
  document.getElementById('notification').style.display = 'none';
  document.getElementById('next-button').style.display = 'none';
}

// Überprüft die ausgewählte Antwort
function checkAnswer(selectedAnswer) {
  var question = questions[currentQuestionIndex];
  var selectedOption = selectedAnswer.split(")")[0]; // Extrahiert den Buchstaben der Antwort
  // Überprüft, ob die Antwort richtig ist
  if (selectedOption === question.answer) {
      correctAnswers++;
      event.target.classList.add("correct"); // Markiert die Antwort als richtig
      showNotification("Richtig!", true);
  } else {
      event.target.classList.add("incorrect"); // Markiert die Antwort als falsch
      showNotification("Falsch! Die richtige Antwort ist: " + question.answer.toUpperCase(), false);
  }
  disableOptions(); // Deaktiviert alle Antwortoptionen
  document.getElementById('next-button').style.display = 'block'; // Zeigt den "Weiter"-Button
}

// Deaktiviert alle Antwortoptionen
function disableOptions() {
  var options = document.getElementsByClassName('option');
  for (var i = 0; i < options.length; i++) {
      options[i].setAttribute("disabled", true);
  }
}

// Zeigt eine Benachrichtigung an
function showNotification(message, isCorrect) {
  var notification = document.getElementById('notification');
  notification.innerHTML = message;
  notification.style.display = 'block';
  // Setzt die Farbe der Benachrichtigung je nach Richtigkeit der Antwort
  notification.style.color = isCorrect ? '#28a745' : '#dc3545';
}

// Zeigt die nächste Frage oder das Ergebnis an, wenn alle Fragen beantwortet sind
function nextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
      showQuestion();
  } else {
      showResult();
  }
}

// Zeigt das Ergebnis des Quiz an
function showResult() {
  var resultMessage = "";
  // Setzt die Ergebnisnachricht je nach Anzahl der richtigen Antworten
  if (correctAnswers >= 5) {
      resultMessage = "Herzlichen Glückwunsch! Die 5 Systeme werden wieder hochgefahren.";
  } else {
      resultMessage = "Leider konnten die Systeme nicht hochgefahren werden. Starte das Quiz von vorne.";
  }
  // Fügt die Anzahl der richtigen Antworten zur Ergebnisnachricht hinzu
  resultMessage += "<br>Du hast " + correctAnswers + " von " + questions.length + " Fragen richtig beantwortet!";
  document.getElementById('result-message').innerHTML = resultMessage;
  document.getElementById('result-message').style.display = 'block';
  // Versteckt den Fragen-Container
  document.getElementById('question-container').style.display = 'none'; 
  
  // Dynamisch den Button für das Neustarten des Quiz oder "Zum Cockpit" erstellen
  var buttonContainer = document.getElementById('button-container');
  buttonContainer.innerHTML = ''; // Löscht vorherige Buttons
  var actionButton = document.createElement('button');
  actionButton.className = 'action-button';

  // Setzt den Buttontext und die Funktion je nach Anzahl der richtigen Antworten
  if (correctAnswers >= 5) {
      actionButton.textContent = 'Zum Cockpit';
      actionButton.onclick = null; // Entfernt jegliche Funktion
  } else {
      actionButton.textContent = 'Neues Quiz starten';
      actionButton.onclick = restartQuiz;
  }

  // Fügt den neuen Button dem Container hinzu
  buttonContainer.appendChild(actionButton);
}

// Startet das Quiz neu
function restartQuiz() {
  // Setzt den Index der aktuellen Frage und die Anzahl der richtigen Antworten zurück
  currentQuestionIndex = 0;
  correctAnswers = 0;
  // Versteckt die Ergebnisnachricht
  document.getElementById('result-message').style.display = 'none';
  // Zeigt den Startbildschirm wieder an
  document.getElementById('start-screen').style.display = 'block';
  // Versteckt den Fragen-Container
  document.getElementById('question-container').style.display = 'none';
  // Löscht den Inhalt des Button-Containers
  document.getElementById('button-container').innerHTML = ''; 
}
