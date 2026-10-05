const emailInput = document.getElementById("emailInput");
const checkButton = document.getElementById("checkButton");
const prediction = document.getElementById("prediction");
const confidence = document.getElementById("confidence");
const resultText = document.querySelector(".result-text");
const result = document.getElementById("result");

// Backend API
const API_URL = "http://127.0.0.1:8000/predict";

checkButton.addEventListener("click", async () => {

    const email = emailInput.value.trim();

    if (email === "") {
        alert("Please enter an email.");
        return;
    }

    prediction.textContent = "Checking...";
    confidence.textContent = "--";
    resultText.textContent = "Analyzing your email...";
    result.dataset.state = "checking";

    checkButton.disabled = true;
    checkButton.innerHTML = 'Analyzing... <span aria-hidden="true">↗</span>';

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                email: email
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        prediction.textContent = data.prediction;
        const confidenceValue = Number(data.confidence);
        const confidencePercent = Number.isFinite(confidenceValue)
            ? Math.min(100, Math.max(0, confidenceValue * 100))
            : 0;
        confidence.textContent = confidencePercent.toFixed(2) + "%";

        if (data.prediction.toLowerCase() === "spam") {
            result.dataset.state = "spam";
            resultText.textContent = "This message matches common spam patterns.";
        } else {
            result.dataset.state = "ham";
            resultText.textContent = "This message appears to be legitimate.";
        }

    } catch (error) {

        console.error("Error:", error);

        prediction.textContent = "Error";
        confidence.textContent = "--";
        result.dataset.state = "error";
        resultText.textContent = "Unable to connect to the server.";

        alert("Could not connect to the FastAPI backend.");

    } finally {

        checkButton.disabled = false;
        checkButton.innerHTML = 'Analyze message <span aria-hidden="true">↗</span>';
    }
});
