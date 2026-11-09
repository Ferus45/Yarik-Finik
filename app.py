
from flask import Flask, render_template_string

app = Flask(__name__)

slides = [
    {
        "emoji": "🌴",
        "title": "ЯРИК, КАПЕЦ!",
        "text": "Ты финик! И это уже доказано."
    },
    {
        "emoji": "😂",
        "title": "КТО ТАКОЙ ЯРИК?",
        "text": "Загадка природы и главный прикол."
    },
    {
        "emoji": "🥭",
        "title": "ФИНИКОВЫЙ УРОВЕНЬ",
        "text": "99% финик, 1% человек."
    },
    {
        "emoji": "🔥",
        "title": "СУПЕРСПОСОБНОСТИ",
        "text": "Умеет превращать любой день в цирк."
    },
    {
        "emoji": "👑",
        "title": "КОРОЛЬ ФИНИКОВ",
        "text": "Даже пальмы снимают перед ним шляпу."
    },
    {
        "emoji": "🤣",
        "title": "ВНИМАНИЕ!",
        "text": "Ярик рядом! Прячьте сухофрукты!"
    },
    {
        "emoji": "🏆",
        "title": "КОНЕЦ",
        "text": "Ярик, ты легенда! Оставайся фиником!"
    }
]

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ярик — ты финик!</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    color: white;
    background: linear-gradient(135deg, #18002e, #7020a0, #ed429b);
}

.container {
    width: 90%;
    max-width: 750px;
    min-height: 450px;
    padding: 40px 25px;
    text-align: center;
    background: rgba(255,255,255,0.14);
    border: 2px solid rgba(255,255,255,0.25);
    border-radius: 30px;
    box-shadow: 0 15px 50px #0005;
}

h1 {
    font-size: 36px;
}

.emoji {
    font-size: 100px;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}

.description {
    font-size: 23px;
    line-height: 1.5;
    min-height: 65px;
}

button {
    padding: 14px 25px;
    margin: 10px 5px;
    border: none;
    border-radius: 15px;
    background: #ffce42;
    color: #351044;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}

button:hover {
    transform: scale(1.08);
    background: white;
}

.counter {
    margin-top: 20px;
    opacity: 0.8;
}

.progress {
    height: 8px;
    margin-top: 20px;
    background: #ffffff40;
    border-radius: 10px;
    overflow: hidden;
}

.bar {
    height: 100%;
    width: 0;
    background: #ffce42;
    transition: width 0.3s;
}

@media (max-width: 500px) {
    h1 { font-size: 27px; }
    .emoji { font-size: 75px; }
    .description { font-size: 19px; }
}
</style>
</head>

<body>

<div class="container">
    <div class="emoji" id="emoji">🌴</div>

    <h1 id="title">ЯРИК, КАПЕЦ!</h1>

    <p class="description" id="description">
        Ты финик! И это уже доказано.
    </p>

    <button onclick="previousSlide()">⬅ Назад</button>
    <button onclick="nextSlide()">Далее ➡</button>

    <div class="counter" id="counter"></div>

    <div class="progress">
        <div class="bar" id="bar"></div>
    </div>
</div>

<script>
const slides = {{ slides | tojson }};
let current = 0;

function showSlide() {
    const slide = slides[current];

    document.getElementById("emoji").textContent = slide.emoji;
    document.getElementById("title").textContent = slide.title;
    document.getElementById("description").textContent = slide.text;

    document.getElementById("counter").textContent =
        "Слайд " + (current + 1) + " из " + slides.length;

    document.getElementById("bar").style.width =
        ((current + 1) / slides.length * 100) + "%";
}

function nextSlide() {
    current = (current + 1) % slides.length;
    showSlide();
}

function previousSlide() {
    current = (current - 1 + slides.length) % slides.length;
    showSlide();
}

document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowRight") nextSlide();
    if (event.key === "ArrowLeft") previousSlide();
});

showSlide();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, slides=slides)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
