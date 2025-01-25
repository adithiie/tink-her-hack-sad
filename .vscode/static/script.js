

//script.js code
function checkAnswer(word) {
    let feedback = document.getElementById('feedback');
    if (word === 'happy') {
        feedback.textContent = "Correct! 'Ebullient' means happy!";
    } else {
        feedback.textContent = "Try again!";
    }
}

function submitGuess() {
    let userGuess = document.getElementById('userGuess').value;
    let feedback = document.getElementById('feedback');
    
    if (userGuess.toLowerCase() === 'vivacious') {
        feedback.textContent = "Correct! 'Vivacious' means full of life!";
    } else {
        feedback.textContent = "Wrong! Try again!";
    }
}