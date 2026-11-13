import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Varun's Birthday Surprise",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
header, footer, [data-testid="stToolbar"] {
    display: none !important;
}
.stApp {
    background: #0b1420;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

html_code = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    background: #0b1420;
    color: white;
    font-family: Arial, sans-serif;
    overflow-x: hidden;
}

.section {
    min-height: 100vh;
    padding: 45px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    text-align: center;
    position: relative;
    overflow: hidden;
}

#intro {
    background: radial-gradient(circle at top, #314c68, #101d2c 55%, #080f18);
}

.small-title {
    color: #a8bed2;
    letter-spacing: 5px;
    font-size: 12px;
    margin-bottom: 25px;
}

h1 {
    font-size: clamp(36px, 7vw, 75px);
    color: #edf3f8;
    letter-spacing: 2px;
    margin-bottom: 20px;
}

h2 {
    color: #a8bfd5;
    letter-spacing: 4px;
    font-size: clamp(20px, 4vw, 32px);
}

.description {
    max-width: 680px;
    color: #c1cedb;
    line-height: 2;
    font-size: 16px;
    margin: 25px auto;
}

button {
    background: linear-gradient(135deg, #496987, #263d55);
    border: 1px solid #a7bfd4;
    color: white;
    padding: 17px 30px;
    margin-top: 25px;
    border-radius: 5px;
    font-size: 13px;
    letter-spacing: 2px;
    cursor: pointer;
    transition: .3s;
}

button:hover {
    transform: scale(1.06);
    background: #5a7896;
}

#celebration {
    display: none;
    background: linear-gradient(180deg, #172d43, #0c1825);
    transition: background 1.5s;
}

#celebration.dark {
    background: #050a10;
}

.friendship {
    max-width: 650px;
    padding: 28px;
    margin: 25px 0;
    border: 1px solid #607c96;
    background: rgba(255,255,255,.045);
    border-radius: 12px;
    line-height: 2;
    color: #c4d1de;
}

.friendship h2 {
    font-size: 23px;
    margin-bottom: 12px;
}

.balloon {
    position: fixed;
    bottom: -120px;
    width: 45px;
    height: 58px;
    border-radius: 50%;
    z-index: 10;
    pointer-events: none;
    animation: fly 8s linear forwards;
}

.balloon:after {
    content: "";
    position: absolute;
    height: 65px;
    width: 1px;
    background: #a6b5c4;
    left: 50%;
    top: 58px;
}

@keyframes fly {
    to {
        transform: translateY(-125vh) rotate(25deg);
        opacity: 0;
    }
}

/* CONFETTI */

.confetti {
    position: fixed;
    top: -15px;
    width: 9px;
    height: 14px;
    z-index: 20;
    pointer-events: none;
    animation: confettiFall 5s linear forwards;
}

@keyframes confettiFall {
    to {
        transform: translateY(110vh) rotate(800deg);
        opacity: 0;
    }
}

/* CAKE */

.cake-area {
    position: relative;
    width: 330px;
    height: 310px;
    margin: 35px auto 5px;
    filter: drop-shadow(0 15px 25px rgba(0,0,0,.4));
}

.plate {
    position: absolute;
    bottom: 5px;
    left: 0;
    width: 330px;
    height: 22px;
    background: linear-gradient(#d7e0e8, #647c94);
    border-radius: 50%;
}

.bottom-cake {
    position: absolute;
    bottom: 25px;
    left: 25px;
    width: 280px;
    height: 85px;
    background: linear-gradient(90deg, #192f48, #3f5d7b, #192f48);
    border-radius: 8px 8px 18px 18px;
    border-bottom: 9px solid #101e30;
}

.bottom-cream {
    position: absolute;
    bottom: 103px;
    left: 25px;
    width: 280px;
    height: 20px;
    background: #d6e0e9;
    border-radius: 50%;
}

.middle-cake {
    position: absolute;
    bottom: 120px;
    left: 52px;
    width: 226px;
    height: 65px;
    background: linear-gradient(90deg, #344f6a, #607c96, #344f6a);
    border-radius: 8px 8px 5px 5px;
}

.middle-cream {
    position: absolute;
    bottom: 180px;
    left: 52px;
    width: 226px;
    height: 18px;
    background: #e1e7ed;
    border-radius: 50%;
}

.top-cake {
    position: absolute;
    bottom: 194px;
    left: 88px;
    width: 154px;
    height: 48px;
    background: linear-gradient(90deg, #263f58, #718ba3, #263f58);
    border-radius: 9px 9px 4px 4px;
}

.top-cream {
    position: absolute;
    bottom: 237px;
    left: 88px;
    width: 154px;
    height: 17px;
    background: #e4eaf0;
    border-radius: 50%;
}

.cake-decoration {
    position: absolute;
    bottom: 48px;
    left: 0;
    width: 100%;
    text-align: center;
    font-size: 12px;
    letter-spacing: 3px;
    color: #e5edf4;
}

.candles {
    position: absolute;
    bottom: 250px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 23px;
    z-index: 4;
}

.candle {
    position: relative;
    width: 10px;
    height: 43px;
    background: repeating-linear-gradient(
        45deg, #dce5ed 0 5px, #718da7 5px 10px
    );
    border-radius: 3px;
}

.flame {
    position: absolute;
    top: -24px;
    left: -3px;
    width: 16px;
    height: 23px;
    background: #ffcc57;
    border-radius: 50% 50% 50% 50%;
    box-shadow: 0 0 15px #ffb52f, 0 0 30px #ff9e27;
    animation: flicker .4s infinite alternate;
}

@keyframes flicker {
    to { transform: scale(1.2) rotate(7deg); }
}

#blow-button {
    max-width: 95%;
}

.smoke {
    position: absolute;
    top: -25px;
    left: -2px;
    width: 15px;
    height: 25px;
    border-radius: 50%;
    background: #d2dbe3;
    animation: smoke 1.3s forwards;
}

@keyframes smoke {
    to {
        transform: translateY(-50px) scale(2);
        opacity: 0;
    }
}

/* FINAL MESSAGE */

#final-message {
    display: none;
    max-width: 850px;
    padding: 30px 15px;
    animation: reveal 2s ease forwards;
}

@keyframes reveal {
    from {
        opacity: 0;
        transform: translateY(50px) scale(.85);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.final-heading {
    font-size: clamp(35px, 7vw, 68px);
    color: #e4edf6;
    line-height: 1.3;
    margin-bottom: 25px;
    text-shadow: 0 0 25px #7898b5;
}

.final-text {
    font-size: 17px;
    color: #bdcede;
    line-height: 2.1;
    margin: 25px auto;
}

.final-name {
    font-size: clamp(25px, 5vw, 43px);
    letter-spacing: 3px;
    color: white;
    margin-top: 30px;
}

.final-footer {
    color: #8ca9c4;
    letter-spacing: 4px;
    font-size: 12px;
    margin-top: 35px;
}

@media(max-width: 500px) {
    .cake-area {
        transform: scale(.85);
        margin-top: 10px;
        margin-bottom: -20px;
    }

    .description {
        font-size: 14px;
    }

    .friendship {
        padding: 20px;
    }
}
</style>
</head>

<body>

<section class="section" id="intro">


    <h1>HAPPY BIRTHDAY BOXER BOY! 🎂</h1>


    <p class="description">
         May this new chapter of your life bring you endless happiness,
         good health, success, and unforgettable memories.
         Keep shining and never stop chasing your dreams. ❤️
    </p>

    <button onclick="openSurprise()">
        OPEN MY SURPRISE
    </button>

</section>


<section class="section" id="celebration">


    <h1>THE CELEBRATION STARTS NOW</h1>

    <div class="friendship">

        <h2>A LITTLE NOTE FOR YOU</h2>

        Congratulations! You’re officially a year older—but don’t worry, you’re still not exactly "old." 😂 
        You’ve only been a part of my life for a short while, but even in that time, 
        I’ve realized what a good person you are, dudee. 
        I enjoy chatting with you, you little boxer boy. 😝 
        Enjoy your day, birthday boy! 🎂
        
        <br><br>
        Now, enough talking. It's time for cake!

    </div>

    <div class="small-title">MAKE THIS MOMENT COUNT</div>

    <div class="cake-area">

        <div class="candles">

            <div class="candle"><div class="flame"></div></div>
            <div class="candle"><div class="flame"></div></div>
            <div class="candle"><div class="flame"></div></div>
            <div class="candle"><div class="flame"></div></div>
            <div class="candle"><div class="flame"></div></div>

        </div>

        <div class="top-cream"></div>
        <div class="top-cake"></div>
        <div class="middle-cream"></div>
        <div class="middle-cake"></div>
        <div class="bottom-cream"></div>
        <div class="bottom-cake"></div>
        <div class="cake-decoration">HAPPY BIRTHDAY</div>
        <div class="plate"></div>

    </div>

    <h2>YOUR WISH IS WAITING</h2>

    <p class="description">
        Close your eyes, make a wish and get ready
        for a brand-new year of adventures!
    </p>

    <button id="blow-button" onclick="blowCandles()">
        MAKE A WISH AND BLOW OUT THE CANDLES, THEN PRESS THE BUTTON
    </button>

    <div id="final-message">

        <div class="final-heading">
            I HOPE ALL YOUR WISHES COME TRUE!
        </div>

        <div class="final-text">

            You can be sure that beautiful things are waiting
            for you.

            May this new chapter of your life bring you
            endless happiness, good health, success and
            unforgettable memories.

            Never lose hope, never stop dreaming and
            always keep smiling.

            No matter what life brings, keep moving forward
            and believe in yourself.

            You deserve the very best!

        </div>

        <div class="final-name">
            HAPPY BIRTHDAY,<br>
            VARUN SHARMA!
        </div>

        <div class="final-footer">
            MADE WITH FRIENDSHIP😁
        </div>

    </div>

</section>


<script>

function openSurprise() {

    document.getElementById("intro").style.display = "none";

    document.getElementById("celebration").style.display = "flex";

    window.scrollTo(0, 0);

    createBalloons();
    createConfetti();

}

function createBalloons() {

    const colors = [
        "#526f8c",
        "#a9bdcf",
        "#d8e2ec",
        "#344d68",
        "#718da8",
        "#b4c6d7"
    ];

    for (let i = 0; i < 40; i++) {

        setTimeout(() => {

            const balloon = document.createElement("div");

            balloon.className = "balloon";

            balloon.style.left = Math.random() * 95 + "vw";

            balloon.style.background =
                colors[Math.floor(Math.random() * colors.length)];

            balloon.style.animationDuration =
                (5 + Math.random() * 4) + "s";

            document.body.appendChild(balloon);

            setTimeout(() => balloon.remove(), 10000);

        }, i * 120);

    }

}

function createConfetti() {

    const colors = [
        "#dce6ef",
        "#91abc4",
        "#557895",
        "#ffffff",
        "#b4c8dc"
    ];

    for (let i = 0; i < 100; i++) {

        setTimeout(() => {

            const piece = document.createElement("div");

            piece.className = "confetti";

            piece.style.left = Math.random() * 100 + "vw";

            piece.style.background =
                colors[Math.floor(Math.random() * colors.length)];

            piece.style.animationDuration =
                (3 + Math.random() * 4) + "s";

            document.body.appendChild(piece);

            setTimeout(() => piece.remove(), 8000);

        }, i * 35);

    }

}

function blowCandles() {

    const flames = document.querySelectorAll(".flame");

    flames.forEach((flame) => {

        const smoke = document.createElement("div");

        smoke.className = "smoke";

        flame.parentElement.appendChild(smoke);

        flame.style.display = "none";

    });

    document.getElementById("blow-button").style.display = "none";

    document.getElementById("celebration").classList.add("dark");

    setTimeout(() => {

        document.getElementById("final-message").style.display = "block";

        createConfetti();

        document.getElementById("final-message").scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

    }, 1600);

}

</script>

</body>
</html>
"""

components.html(html_code, height=1500, scrolling=True)