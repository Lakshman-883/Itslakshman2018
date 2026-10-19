
from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#050816">
<title>ItsLakshman2018 | Digital World</title>
<style>
*{box-sizing:border-box}
:root{--blue:#00eaff;--bg:#050816;--panel:#0b1530}
body{margin:0;background:var(--bg);color:#f2f7ff;font-family:Arial,sans-serif}
header{position:sticky;top:0;background:#030714;padding:16px 5%;border-bottom:1px solid #00eaff55;display:flex;justify-content:space-between;gap:15px;flex-wrap:wrap;z-index:5}
.logo,h2,h3{color:var(--blue)}
.logo{font-size:21px;font-weight:bold}
nav{display:flex;gap:13px;flex-wrap:wrap}
a{color:inherit;text-decoration:none}
nav a:hover{color:var(--blue)}
section{padding:40px 6%;scroll-margin-top:70px}
.hero{text-align:center;min-height:70vh;display:grid;place-items:center}
.hero h1{font-size:clamp(38px,8vw,76px);color:var(--blue);text-shadow:0 0 20px #00eaff66}
.hero p{line-height:1.8;color:#c3cce0}
.heading{text-align:center;color:var(--blue);margin-bottom:28px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));gap:18px}
.card{background:var(--panel);border:1px solid #00eaff44;border-radius:13px;padding:20px;margin-bottom:12px;min-width:0}
.card p{color:#c3cce0;line-height:1.6}
.btn{border:1px solid var(--blue);background:var(--blue);color:#001018;padding:11px 15px;margin:5px 2px;border-radius:7px;font-weight:bold;cursor:pointer}
.alt{background:transparent;color:var(--blue)}
input,select{width:100%;padding:12px;margin:8px 0;background:#050816;color:white;border:1px solid #00eaff66;border-radius:6px}
.result{color:#8dffb1;min-height:25px;overflow-wrap:anywhere;margin-top:12px}
canvas{display:block;max-width:100%;height:auto;margin:15px auto;border:1px solid var(--blue);background:linear-gradient(145deg,#071426,#02060c);box-shadow:0 12px 28px #0008,inset 0 0 18px #00eaff12;border-radius:10px}
.card{position:relative;transform-style:preserve-3d;box-shadow:0 12px 24px #0005,inset 0 1px #ffffff0a;transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease}
.card:hover{transform:perspective(900px) rotateX(1.2deg) translateY(-3px);border-color:#00eaff99;box-shadow:0 18px 32px #0008,0 0 18px #00eaff10}
.game3d{position:relative;isolation:isolate;box-shadow:inset 0 0 35px #00eaff12,0 12px 26px #0008}
.game3d:after{content:"3D REALTIME WORLD";position:absolute;z-index:2;top:7px;left:8px;font-size:9px;letter-spacing:1.5px;color:#d9fbff99;pointer-events:none;text-shadow:0 1px 4px #000}
.tile{box-shadow:inset 0 2px #ffffff12,0 4px 0 #050a16;transition:transform .12s,background .12s}
.tile:active{transform:translateY(2px)}
.btn{box-shadow:0 4px 0 #00121b,0 7px 14px #0005;transition:transform .12s,filter .12s}
.btn:active{transform:translateY(2px);box-shadow:0 2px 0 #00121b}
@media(max-width:520px){section{padding:28px 4%}.card{padding:15px}.game3d{height:230px}#road,#snake{width:min(100%,300px);height:auto}.btn{padding:12px 13px;min-height:42px}}
.game3d{width:100%;height:210px;border:1px solid #00eaff66;border-radius:8px;overflow:hidden;background:#02060c;margin:12px 0}
.game3d canvas{width:100%;height:100%;margin:0;border:0;display:block}
#memory{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;max-width:320px;margin:15px auto}
.tile{height:48px;background:#101a35;color:var(--blue);border:1px solid var(--blue);border-radius:6px;font-size:20px}
.terminal{background:#02050b;border:1px solid #00eaff66;padding:15px;border-radius:10px;font-family:monospace}
#out{height:180px;overflow:auto;white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.6}
.row{display:flex;gap:8px;align-items:center}
.row input{flex:1;min-width:0}
footer{text-align:center;padding:25px;border-top:1px solid #00eaff33;color:#9eacc7}
footer a{color:#00eaff}
kbd{border:1px solid #00eaff66;border-radius:4px;padding:2px 6px}
@media(max-width:600px){header{justify-content:center}nav{justify-content:center}section{padding:35px 5%}}
</style>
</head>
<body>
<header>
<a class="logo" href="#home">LAKSHMAN_2018</a>
<a class="btn" href="#3dgames">PLAY GAMES</a>
</header>

<section id="home" class="hero"><div>
<p>WELCOME TO MY DIGITAL WORLD</p>
<h1>ITS LAKSHMAN</h1>
<p>Creator | Gamer | Digital Explorer<br>Welcome to my futuristic neon universe.</p>
<a class="btn" href="#projects">EXPLORE PROJECTS</a>
<a class="btn alt" href="#games">PLAY GAMES</a>
</div></section>

<section id="about">
<h2 class="heading">ABOUT ME</h2>
<div class="card"><h3>Who Am I?</h3>
<p>Welcome to ItsLakshman2018 — a digital space for creativity, gaming and web projects.</p>
</div></section>

<section id="projects">
<h2 class="heading">MY PROJECTS</h2><div class="grid">
<div class="card"><h3>🌐 Portfolio</h3><p>Futuristic personal website.</p></div>
<div class="card"><h3>🎮 Gaming Zone</h3><p>Browser mini-games.</p></div>
<div class="card"><h3>🏎️ Racing Arena</h3><p>Avoid traffic and race.</p></div>
<div class="card"><h3>💻 Digital Terminal</h3><p>Try demo commands.</p></div>
</div></section>

<section id="games">
<h2 class="heading">🎮 GAMING ZONE</h2><div class="grid">
<div class="card"><h3>🔢 Number Guess</h3>
<p>Guess a number from 1 to 100.</p>
<input id="guess" type="number" min="1" max="100" placeholder="Enter number">
<button class="btn" onclick="guessGame()">GUESS</button>
<button class="btn alt" onclick="resetGuess()">RESET</button>
<div id="guessOut" class="result"></div></div>

<div class="card"><h3>✊ Rock Paper Scissors</h3>
<button class="btn" onclick="rps('Rock')">✊ Rock</button>
<button class="btn" onclick="rps('Paper')">✋ Paper</button>
<button class="btn" onclick="rps('Scissors')">✌️ Scissors</button>
<div id="rpsOut" class="result"></div></div>

<div class="card"><h3>⚡ Reflex Test</h3>
<p>Click when the button turns green.</p>
<button id="reflex" class="btn" onclick="reflexGame()">START TEST</button>
<div id="reflexOut" class="result"></div></div>

<div class="card"><h3>🧠 Memory Matrix</h3>
<p>Remember the highlighted tiles.</p>
<button class="btn" onclick="memoryStart()">START</button>
<div id="memory"></div><div id="memoryOut" class="result"></div></div>

<div class="card"><h3>🐍 Snake Game</h3>
<p>Use arrow keys or touch controls.</p>
<div style="perspective:900px;max-width:330px;margin:auto">
<canvas id="snake" width="300" height="300" style="transform:rotateX(5deg);transform-origin:center;box-shadow:0 18px 28px #0009,0 0 20px #00eaff18"></canvas>
</div>
<div style="text-align:center">
<button class="btn" onclick="snakeDir(0,-1)">⬆️</button><br>
<button class="btn" onclick="snakeDir(-1,0)">⬅️</button>
<button class="btn" onclick="snakeDir(0,1)">⬇️</button>
<button class="btn" onclick="snakeDir(1,0)">➡️</button><br>
<button class="btn alt" onclick="snakeStart()">RESTART</button>
</div>
<div id="snakeOut" class="result">Score: 0</div></div>
</div></section>
<section id="race">
<h2 class="heading">🏁 NEON RACING ARENA</h2>
<div class="card">
<h3>Choose Your Vehicle</h3>
<select id="vehicle">
<option value="bike">🏍️ Neon Bike</option>
<option value="car">🏎️ Super Car</option>
</select>
<button class="btn" onclick="raceStart()">START RACE</button>
<button class="btn alt" onclick="raceStop()">STOP</button>
<div style="perspective:850px;max-width:330px;margin:auto">
<canvas id="road" width="300" height="440" style="transform:rotateX(4deg);transform-origin:center;box-shadow:0 22px 32px #000a,0 0 22px #00eaff14"></canvas>
</div>
<div style="text-align:center">
<button class="btn" onclick="raceMove(-1)">⬅️ LEFT</button>
<button class="btn" onclick="raceMove(1)">RIGHT ➡️</button>
</div>
<div id="raceOut" class="result">Choose a vehicle and start.</div>
<p>Desktop: arrow keys. Mobile: use the buttons.</p>
</div>
</section>

<section id="3dgames">
<h2 class="heading">🕹️ 3D GAMING ZONE</h2>
<p style="text-align:center;color:#c3cce0">Play the 3D browser games.</p>
<div class="grid">

<div class="card">
<h3>🏃 Neon Runner 3D</h3>
<p>Switch lanes and dodge blocks.</p>
<div id="runner3d" class="game3d"></div>
<button class="btn" onclick="runnerMove(-1)">⬅️</button>
<button class="btn" onclick="runnerStart()">START / RESTART</button>
<button class="btn" onclick="runnerMove(1)">➡️</button>
<div id="runnerOut" class="result">Press start.</div>
</div>

<div class="card">
<h3>🧟 Zombie Survival 3D</h3>
<p>Click zombies to tag them.</p>
<div id="zombie3d" class="game3d"></div>
<button class="btn" onclick="zombieMove(-1,0)">⬅️</button>
<button class="btn" onclick="zombieMove(0,-1)">⬆️</button>
<button class="btn" onclick="zombieMove(0,1)">⬇️</button>
<button class="btn" onclick="zombieMove(1,0)">➡️</button>
<div id="zombieOut" class="result">Click a zombie to score.</div>
</div>

<div class="card">
<h3>🚗 3D Drift Drive</h3>
<p>Steer and avoid barriers.</p>
<div id="drive3d" class="game3d"></div>
<button class="btn" onclick="driveMove(-1)">⬅️ LEFT</button>
<button class="btn" onclick="driveMove(1)">RIGHT ➡️</button>
<div id="driveOut" class="result">Distance: 0</div>
</div>

<div class="card">
<h3>🚀 Space Blaster 3D</h3>
<p>Move your ship and fire.</p>
<div id="space3d" class="game3d"></div>
<button class="btn" onclick="spaceMove(-1)">⬅️</button>
<button class="btn" onclick="spaceShoot()">🔥 FIRE</button>
<button class="btn" onclick="spaceMove(1)">➡️</button>
<div id="spaceOut" class="result">Targets hit: 0</div>
</div>

</div>
</section>

<section id="terminal">
<h2 class="heading">💻 DIGITAL TERMINAL</h2>
<div class="terminal">
<div id="out">Welcome to Lakshman Terminal.
Type help to see available commands.</div>
<div class="row">
<span>&gt;</span>
<input id="cmd" placeholder="Type a command" autocomplete="off">
<button class="btn" onclick="command()">RUN</button>
</div>
</div>
<p>Commands: help, about, games, racing, date, browser, device, network, clear</p>
<p style="color:#9eacc7">Demo terminal only. It cannot execute real operating-system commands.</p>
</section>

<section id="settings">
<h2 class="heading">⚙️ GAMING CONTROL CENTER</h2>
<div class="card">
<p>Shared settings for the browser games. Graphics presets are best-effort and depend on device/browser support.</p>
<div class="grid">
<div>
<label for="gfxQuality">Graphics quality</label>
<select id="gfxQuality">
<option value="auto">Auto</option>
<option value="low">Low</option>
<option value="medium">Medium</option>
<option value="high">High</option>
<option value="ultra">Ultra</option>
</select>
</div>
<div>
<label for="masterVolume">Master volume (saved setting)</label>
<input id="masterVolume" type="range" min="0" max="1" step="0.05">
</div>
<div>
<label for="musicVolume">Music volume (saved setting)</label>
<input id="musicVolume" type="range" min="0" max="1" step="0.05">
</div>
<div>
<label for="sfxVolume">SFX volume (saved setting)</label>
<input id="sfxVolume" type="range" min="0" max="1" step="0.05">
</div>
</div>

<div class="grid">
<div class="card">
<h3>Player Progress</h3>
<p>Level: <strong id="playerLevel">1</strong></p>
<p>Total XP: <strong id="playerXP">0</strong></p>
</div>
<div class="card">
<h3>Save Status</h3>
<p id="saveStatus" class="result" aria-live="polite">Local save ready.</p>
<button class="btn" id="saveNow">SAVE NOW</button>
</div>
<div class="card">
<h3>Game Controls</h3>
<p>Use the in-game buttons or keyboard arrows. Press <kbd>P</kbd> to pause/resume the 3D simulation.</p>
<button class="btn" id="pauseToggle">PAUSE 3D GAMES</button>
<p id="pauseStatus" class="result">Games running</p>
</div>
</div>

<p style="color:#9eacc7">Local saves stay in this browser/device. Clearing browser data may erase progress. Audio sliders store preferences; actual sound playback must be connected to game audio assets separately.</p>
</div>
</section>

<section id="contact">
<h2 class="heading">CONTACT ME</h2>
<div class="card" style="text-align:center">
<h3>Let's Connect</h3>
<p>Follow my social media for updates.</p>
<a class="btn" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">INSTAGRAM</a>
</div>
</section>

<footer>
© <span id="year"></span> LAKSHMAN_2018 | Digital World ⚡
<br>
<p>
<a href="#home">Home</a> ·
<a href="#about">About</a> ·
<a href="#projects">Projects</a> ·
<a href="#games">Mini-games</a> ·
<a href="#race">Racing</a> ·
<a href="#3dgames">3D games</a> ·
<a href="#settings">Gaming settings</a> ·
<a href="#terminal">Terminal</a> ·
<a href="#contact">Contact</a>
</p>
</footer>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
const $ = id => document.getElementById(id);

let xp = 0;
let paused = false;
let guessTarget = Math.floor(Math.random() * 100) + 1;
let guessAttempts = 0;

if ($("year")) $("year").textContent = new Date().getFullYear();

function addXP(amount) {
  xp += Math.max(0, Number(amount) || 0);
  if ($("playerXP")) $("playerXP").textContent = xp;
  if ($("playerLevel")) {
    $("playerLevel").textContent = Math.floor(xp / 100) + 1;
  }
  saveProgress();
}

function saveProgress() {
  try {
    localStorage.setItem("lakshman_xp", String(xp));
  } catch (e) {}
}

function loadProgress() {
  try {
    xp = Math.max(0, Number(localStorage.getItem("lakshman_xp")) || 0);
  } catch (e) {
    xp = 0;
  }

  if ($("playerXP")) $("playerXP").textContent = xp;
  if ($("playerLevel")) {
    $("playerLevel").textContent = Math.floor(xp / 100) + 1;
  }
}

loadProgress();

// NUMBER GUESS GAME
function checkGuess() {
  const field = $("guessInput");
  const output = $("guessOut");
  if (!field || !output) return;

  const value = Number(field.value);

  if (!Number.isInteger(value) || value < 1 || value > 100) {
    output.textContent = "Enter a whole number from 1 to 100.";
    return;
  }

  guessAttempts++;

  if (value === guessTarget) {
    output.textContent =
      "Correct! Attempts: " + guessAttempts + ". New number started!";
    addXP(10);
    guessTarget = Math.floor(Math.random() * 100) + 1;
    guessAttempts = 0;
    field.value = "";
  } else {
    output.textContent = value < guessTarget
      ? "Too low! Try a higher number."
      : "Too high! Try a lower number.";
  }
}

// ROCK PAPER SCISSORS
function playRPS(choice) {
  const output = $("rpsOut");
  if (!output) return;

  const choices = ["rock", "paper", "scissors"];
  const computer = choices[Math.floor(Math.random() * choices.length)];

  if (choice === computer) {
    output.textContent = "Draw! Computer chose " + computer + ".";
  } else if (
    (choice === "rock" && computer === "scissors") ||
    (choice === "paper" && computer === "rock") ||
    (choice === "scissors" && computer === "paper")
  ) {
    output.textContent = "You win! Computer chose " + computer + ".";
    addXP(5);
  } else {
    output.textContent = "Computer wins! It chose " + computer + ".";
  }
}

// REFLEX GAME
let reflexTimer = null;
let reflexStartedAt = 0;
let reflexReady = false;

function reflexStart() {
  const output = $("reflexOut");
  if (!output) return;

  clearTimeout(reflexTimer);
  reflexReady = false;
  output.textContent = "Wait for GO...";

  reflexTimer = setTimeout(() => {
    reflexReady = true;
    reflexStartedAt = performance.now();
    output.textContent = "GO! Click the reflex button now!";
  }, 1000 + Math.random() * 3000);
}

function reflexClick() {
  const output = $("reflexOut");
  if (!output) return;

  if (!reflexReady) {
    clearTimeout(reflexTimer);
    output.textContent = "Too early! Press start and wait for GO.";
    return;
  }

  const elapsed = Math.round(performance.now() - reflexStartedAt);
  reflexReady = false;
  output.textContent = "Your reaction: " + elapsed + " ms";

  if (elapsed < 350) addXP(5);
}

// MEMORY GAME
let memoryPattern = [];
let memoryIndex = 0;

function memoryStart() {
  memoryPattern = Array.from(
    { length: 5 },
    () => Math.floor(Math.random() * 4) + 1
  );
  memoryIndex = 0;

  const output = $("memoryOut");
  if (output) {
    output.textContent = "Remember this sequence: " + memoryPattern.join(" ");
  }
}

function memoryGuess(value) {
  const output = $("memoryOut");
  if (!output || memoryPattern.length === 0) return;

  if (Number(value) !== memoryPattern[memoryIndex]) {
    output.textContent = "Wrong sequence! Press start to try again.";
    memoryPattern = [];
    memoryIndex = 0;
    return;
  }

  memoryIndex++;

  if (memoryIndex === memoryPattern.length) {
    output.textContent = "Excellent! You remembered the sequence!";
    addXP(10);
    memoryPattern = [];
  } else {
    output.textContent =
      "Correct! Next number: " + (memoryIndex + 1) + " of " +
      memoryPattern.length;
  }
}

// PAUSE CONTROL
function setPaused(value) {
  paused = Boolean(value);
  if ($("pauseStatus")) {
    $("pauseStatus").textContent = paused ? "Games paused" : "Games running";
  }
  if ($("pauseToggle")) {
    $("pauseToggle").textContent = paused
      ? "RESUME 3D GAMES"
      : "PAUSE 3D GAMES";
  }
}

if ($("pauseToggle")) {
  $("pauseToggle").addEventListener("click", () => setPaused(!paused));
}

document.addEventListener("keydown", event => {
  if (event.key.toLowerCase() === "p" && !event.repeat) {
    setPaused(!paused);
  }
});
// SNAKE GAME
const snakeCanvas = $("snakeCanvas");
const snakeCtx = snakeCanvas ? snakeCanvas.getContext("2d") : null;

let snake = [{ x: 8, y: 8 }];
let snakeFood = { x: 12, y: 12 };
let snakeVelocity = { x: 1, y: 0 };
let snakeScore = 0;
let snakeLoop = null;
const snakeCell = 15;
const snakeSize = 20;

function snakeDir(dx, dy) {
  if (dx === -snakeVelocity.x && dy === -snakeVelocity.y) return;
  snakeVelocity = { x: dx, y: dy };
}

function snakeStart() {
  clearInterval(snakeLoop);
  snake = [{ x: 8, y: 8 }];
  snakeVelocity = { x: 1, y: 0 };
  snakeScore = 0;
  snakeFood = {
    x: Math.floor(Math.random() * snakeSize),
    y: Math.floor(Math.random() * snakeSize)
  };

  if ($("snakeOut")) $("snakeOut").textContent = "Score: 0";
  snakeDraw();
  snakeLoop = setInterval(snakeStep, 150);
}

function snakeStep() {
  if (paused) return;

  const head = {
    x: snake[0].x + snakeVelocity.x,
    y: snake[0].y + snakeVelocity.y
  };

  if (
    head.x < 0 || head.y < 0 ||
    head.x >= snakeSize || head.y >= snakeSize ||
    snake.some(part => part.x === head.x && part.y === head.y)
  ) {
    clearInterval(snakeLoop);
    if ($("snakeOut")) {
      $("snakeOut").textContent = "Game over! Score: " + snakeScore;
    }
    return;
  }

  snake.unshift(head);

  if (head.x === snakeFood.x && head.y === snakeFood.y) {
    snakeScore++;
    snakeFood = {
      x: Math.floor(Math.random() * snakeSize),
      y: Math.floor(Math.random() * snakeSize)
    };
    if ($("snakeOut")) {
      $("snakeOut").textContent = "Score: " + snakeScore;
    }
    if (snakeScore % 5 === 0) addXP(5);
  } else {
    snake.pop();
  }

  snakeDraw();
}

function snakeDraw() {
  if (!snakeCtx) return;

  snakeCtx.fillStyle = "#07111e";
  snakeCtx.fillRect(0, 0, snakeCanvas.width, snakeCanvas.height);

  const cellW = snakeCanvas.width / snakeSize;
  const cellH = snakeCanvas.height / snakeSize;

  snakeCtx.fillStyle = "#ff477e";
  snakeCtx.fillRect(
    snakeFood.x * cellW,
    snakeFood.y * cellH,
    cellW - 1,
    cellH - 1
  );

  snake.forEach((part, index) => {
    snakeCtx.fillStyle = index === 0 ? "#00f5ff" : "#20bfa9";
    snakeCtx.fillRect(
      part.x * cellW,
      part.y * cellH,
      cellW - 1,
      cellH - 1
    );
  });
}

// RACING GAME
const roadCanvas = $("road");
const roadCtx = roadCanvas ? roadCanvas.getContext("2d") : null;

let raceLane = 1;
let raceRunning = false;
let raceFrame = null;
let raceDistance = 0;
let raceObstacles = [];
let raceLastTime = 0;

function raceMove(direction) {
  raceLane = Math.max(0, Math.min(2, raceLane + direction));
}

function raceStart() {
  raceStop();
  raceLane = 1;
  raceDistance = 0;
  raceObstacles = [];
  raceRunning = true;
  raceLastTime = 0;

  if ($("raceOut")) $("raceOut").textContent = "Race started!";
  raceFrame = requestAnimationFrame(raceTick);
}

function raceStop() {
  raceRunning = false;
  if (raceFrame !== null) cancelAnimationFrame(raceFrame);
  raceFrame = null;
  if ($("raceOut")) {
    $("raceOut").textContent = "Race stopped. Distance: " +
      Math.floor(raceDistance);
  }
}

function raceTick(time) {
  if (!raceRunning) return;

  if (!raceLastTime) raceLastTime = time;
  const dt = Math.min((time - raceLastTime) / 16.67, 3);
  raceLastTime = time;

  if (!paused) {
    raceDistance += dt;
    if (Math.random() < 0.025 * dt) {
      raceObstacles.push({
        lane: Math.floor(Math.random() * 3),
        y: -30
      });
    }

    raceObstacles.forEach(obstacle => obstacle.y += 3 * dt);
    raceObstacles = raceObstacles.filter(
      obstacle => obstacle.y < (roadCanvas ? roadCanvas.height : 440) + 30
    );

    const hit = raceObstacles.some(
      obstacle => obstacle.lane === raceLane &&
        obstacle.y > 350 && obstacle.y < 410
    );

    if (hit) {
      raceRunning = false;
      if ($("raceOut")) {
        $("raceOut").textContent =
          "Collision! Distance: " + Math.floor(raceDistance);
      }
      addXP(Math.floor(raceDistance / 20));
      raceDraw();
      return;
    }
  }

  raceDraw();

  if ($("raceOut")) {
    $("raceOut").textContent = "Distance: " + Math.floor(raceDistance);
  }

  raceFrame = requestAnimationFrame(raceTick);
}

function raceDraw() {
  if (!roadCtx || !roadCanvas) return;

  const w = roadCanvas.width;
  const h = roadCanvas.height;

  roadCtx.fillStyle = "#10182b";
  roadCtx.fillRect(0, 0, w, h);

  roadCtx.fillStyle = "#26334b";
  roadCtx.fillRect(30, 0, w - 60, h);

  roadCtx.strokeStyle = "#e4e9ff";
  roadCtx.lineWidth = 3;
  roadCtx.setLineDash([20, 20]);

  roadCtx.beginPath();
  roadCtx.moveTo(w / 2 - 40, 0);
  roadCtx.lineTo(w / 2 - 40, h);
  roadCtx.moveTo(w / 2 + 40, 0);
  roadCtx.lineTo(w / 2 + 40, h);
  roadCtx.stroke();
  roadCtx.setLineDash([]);

  raceObstacles.forEach(obstacle => {
    const x = w / 2 + (obstacle.lane - 1) * 80;
    roadCtx.fillStyle = "#ff426e";
    roadCtx.fillRect(x - 13, obstacle.y, 26, 35);
  });

  const carX = w / 2 + (raceLane - 1) * 80;
  roadCtx.fillStyle = $("vehicle")?.value === "bike"
    ? "#00f5ff" : "#ffcf4a";
  roadCtx.fillRect(carX - 15, h - 65, 30, 45);
}

if (roadCanvas) raceDraw();

document.addEventListener("keydown", event => {
  if (event.key === "ArrowLeft") {
    raceMove(-1);
    snakeDir(-1, 0);
  }
  if (event.key === "ArrowRight") {
    raceMove(1);
    snakeDir(1, 0);
  }
  if (event.key === "ArrowUp") snakeDir(0, -1);
  if (event.key === "ArrowDown") snakeDir(0, 1);
});
// 3D GAME SETUP
const scenes3d = {};
let threeAnimationId = null;

function create3DGame(id, color = 0x00eaff) {
  const container = $(id);
  if (!container || !window.THREE) {
    if (container) {
      container.textContent = "3D graphics unavailable. Check your internet connection.";
    }
    return null;
  }

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x07111e);

  const camera = new THREE.PerspectiveCamera(
    60,
    Math.max(container.clientWidth, 1) /
      Math.max(container.clientHeight || 220, 1),
    0.1,
    100
  );
  camera.position.set(0, 2.5, 7);
  camera.lookAt(0, 0, 0);

  let renderer;
  try {
    renderer = new THREE.WebGLRenderer({ antialias: true });
  } catch (error) {
    container.textContent = "WebGL is not supported by this browser.";
    return null;
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(
    Math.max(container.clientWidth, 240),
    Math.max(container.clientHeight || 220, 220)
  );
  container.replaceChildren(renderer.domElement);

  scene.add(new THREE.HemisphereLight(0xffffff, 0x24304a, 2));

  const light = new THREE.DirectionalLight(0xffffff, 2);
  light.position.set(3, 5, 4);
  scene.add(light);

  const floor = new THREE.Mesh(
    new THREE.PlaneGeometry(12, 20),
    new THREE.MeshStandardMaterial({
      color: 0x142238,
      roughness: 0.9
    })
  );
  floor.rotation.x = -Math.PI / 2;
  floor.position.y = -1;
  scene.add(floor);

  const geometry = new THREE.BoxGeometry(1, 1, 1);
  const material = new THREE.MeshStandardMaterial({
    color,
    metalness: 0.35,
    roughness: 0.35
  });

  const player = new THREE.Mesh(geometry, material);
  player.position.y = 0;
  scene.add(player);

  const objects = [];

  for (let i = 0; i < 5; i++) {
    const obstacle = new THREE.Mesh(
      new THREE.BoxGeometry(0.65, 0.65, 0.65),
      new THREE.MeshStandardMaterial({
        color: i % 2 ? 0xff477e : 0x8b5cf6
      })
    );
    obstacle.position.set(
      (Math.random() - 0.5) * 4,
      -0.3,
      -i * 2 - 1
    );
    scene.add(obstacle);
    objects.push(obstacle);
  }

  const game = {
    scene,
    camera,
    renderer,
    player,
    objects,
    score: 0,
    x: 0,
    running: false,
    last: 0
  };

  scenes3d[id] = game;

  function resize() {
    if (!container.isConnected) return;
    const width = Math.max(container.clientWidth, 240);
    const height = Math.max(container.clientHeight || 220, 220);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  }

  if (window.ResizeObserver) {
    const observer = new ResizeObserver(resize);
    observer.observe(container);
    game.observer = observer;
  } else {
    window.addEventListener("resize", resize);
  }

  return game;
}

function animate3D() {
  threeAnimationId = requestAnimationFrame(animate3D);

  Object.values(scenes3d).forEach(game => {
    if (!game || !game.renderer) return;

    if (!paused && game.running) {
      game.player.rotation.y += 0.015;

      game.objects.forEach(object => {
        object.rotation.x += 0.01;
        object.rotation.y += 0.02;
      });
    }

    game.renderer.render(game.scene, game.camera);
  });
}

// RUNNER
function runnerStart() {
  const game = scenes3d.runner3d;
  if (!game) return;

  game.running = true;
  game.score = 0;

  if ($("runnerOut")) $("runnerOut").textContent = "Runner started!";
}

function runnerMove(direction) {
  const game = scenes3d.runner3d;
  if (!game) return;

  game.x = Math.max(-2, Math.min(2, game.x + direction));
  game.player.position.x = game.x;

  if ($("runnerOut")) {
    game.score++;
    $("runnerOut").textContent = "Moves: " + game.score;
  }
}

// ZOMBIE TAG GAME
let zombieScore = 0;

function zombieMove(dx, dz) {
  const game = scenes3d.zombie3d;
  if (!game) return;

  game.player.position.x = Math.max(
    -3,
    Math.min(3, game.player.position.x + dx)
  );
  game.player.position.z += dz;
}

function zombieTag() {
  zombieScore++;
  if ($("zombieOut")) {
    $("zombieOut").textContent = "Zombies tagged: " + zombieScore;
  }
  addXP(1);
}

// DRIVE GAME
let driveDistance = 0;

function driveMove(direction) {
  const game = scenes3d.drive3d;
  if (!game) return;

  game.player.position.x = Math.max(
    -2.5,
    Math.min(2.5, game.player.position.x + direction)
  );

  driveDistance++;
  if ($("driveOut")) {
    $("driveOut").textContent = "Distance: " + driveDistance;
  }
}

// SPACE GAME
let spaceScore = 0;

function spaceMove(direction) {
  const game = scenes3d.space3d;
  if (!game) return;

  game.player.position.x = Math.max(
    -3,
    Math.min(3, game.player.position.x + direction)
  );
}

function spaceShoot() {
  const game = scenes3d.space3d;
  if (!game) return;

  spaceScore++;
  if ($("spaceOut")) {
    $("spaceOut").textContent = "Targets hit: " + spaceScore;
  }
  addXP(2);
}

// INITIALIZE 3D GAMES
function init3DGames() {
  if (!window.THREE) return;

  create3DGame("runner3d", 0x00eaff);
  create3DGame("zombie3d", 0x67b56b);
  create3DGame("drive3d", 0xffcf4a);
  create3DGame("space3d", 0x9b5cff);

  if (!threeAnimationId) animate3D();
}

// TERMINAL COMMANDS
function command() {
  const input = $("cmd");
  const output = $("out");
  if (!input || !output) return;

  const text = input.value.trim().toLowerCase();
  input.value = "";

  const commands = {
    help: "Commands: help, about, games, racing, date, browser, device, network, clear",
    about: "Lakshman Digital World — browser gaming project.",
    games: "Available: Snake, Number Guess, RPS, Reflex, Memory and 3D demos.",
    racing: "Open Racing Arena to start a race.",
    date: new Date().toLocaleString(),
    browser: navigator.userAgent,
    device: screen.width + " × " + screen.height,
    network: navigator.onLine ? "Browser reports online." : "Browser reports offline."
  };

  if (text === "clear") {
    output.textContent = "";
  } else {
    output.textContent += "\n> " + text + "\n" +
      (commands[text] || "Unknown command. Type help.");
  }
}

if ($("cmd")) {
  $("cmd").addEventListener("keydown", event => {
    if (event.key === "Enter") command();
  });
}

// SETTINGS SAVE / LOAD
function saveSettings() {
  const settings = {};

  ["gfxQuality", "masterVolume", "musicVolume", "sfxVolume"].forEach(id => {
    if ($(id)) settings[id] = $(id).value;
  });

  try {
    localStorage.setItem("lakshman_settings", JSON.stringify(settings));
    if ($("saveStatus")) $("saveStatus").textContent = "Settings saved.";
  } catch (error) {
    if ($("saveStatus")) $("saveStatus").textContent = "Unable to save in this browser.";
  }
}

function loadSettings() {
  try {
    const settings = JSON.parse(
      localStorage.getItem("lakshman_settings") || "{}"
    );

    Object.keys(settings).forEach(id => {
      if ($(id)) $(id).value = settings[id];
    });
  } catch (error) {
    // Keep default settings if saved data is unavailable.
  }
}

if ($("saveNow")) $("saveNow").addEventListener("click", saveSettings);

loadSettings();

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", init3DGames, { once: true });
} else {
  init3DGames();
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
 
