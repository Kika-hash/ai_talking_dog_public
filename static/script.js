function askQuestion() {
    var questionInput = document.getElementById("questionInput").value;
    var answerDisplay = document.getElementById("answerDisplay");
}

function clearQuestion() {
    document.getElementById("questionInput").value = "";
    document.getElementById("answerDisplay").innerHTML = "";
    window.location.href = "/";
}