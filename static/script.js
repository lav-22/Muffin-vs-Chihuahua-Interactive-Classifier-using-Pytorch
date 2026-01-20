let correct = correct;
let wrong = wrong;


async function predict() {
    const imageInput = document.getElementById("imageInput");
    if (!imageInput) return alert ("Upload an Image");

    const formData = new FormData();
    formData.append("image", imageInput.files[0]);

    const response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    console.log("Prediction from Flask:", data.prediction);

    document.getElementById("predictionText").innerText =
        "Prediction: " + data.prediction;
    document.getElementById("feedback").style.display = "block";

}

async function sendFeedback(isCorrect) {
const response = await fetch("/feedback", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ correct: isCorrect})
    });

    const data = await response.json();

    correct = data.correct;
    wrong = data.wrong;

    document.getElementById("correct").innerText = correct;
    document.getElementById("wrong").innerText = wrong;
    document.getElementById("accuracy").innerText =
        (data.accuracy * 100).toFixed(2) + "%";

}
