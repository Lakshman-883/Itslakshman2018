
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
<input id="guessInput" type="number" min="1" max="100" placeholder="Enter number">
<button class="btn" onclick="checkGuess()">GUESS</button>
<button class="btn alt" onclick="resetGuess()">RESET</button>
<div id="guessOut" class="result"></div></div>

<div class="card"><h3>✊ Rock Paper Scissors</h3>
<button class="btn" onclick="playRPS('rock')">✊ Rock</button>
<button class="btn" onclick="playRPS('paper')">✋ Paper</button>
<button class="btn" onclick="playRPS('scissors')">✌️ Scissors</button>
<div id="rpsOut" class="result"></div></div>

<div class="card"><h3>⚡ Reflex Test</h3>
<p>Click when the button turns green.</p>
<button id="reflex" class="btn" onclick="reflexStart()">START TEST</button>
<div id="reflexOut" class="result"></div></div>

<div class="card"><h3>🧠 Memory Matrix</h3>
<p>Remember the highlighted tiles.</p>
<button class="btn" onclick="memoryStart()">START</button>
<div id="memory"></div><div id="memoryOut" class="result"></div></div>

<div class="card"><h3>🐍 Snake Game</h3>
<p>Use arrow keys or touch controls.</p>
<div style="perspective:900px;max-width:330px;margin:auto">
<canvas id="snakeCanvas" width="300" height="300" style="transform:rotateX(5deg);transform-origin:center;box-shadow:0 18px 28px #0009,0 0 20px #00eaff18"></canvas>
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
<p>Move close to a zombie and press TAG.</p>
<div id="zombie3d" class="game3d"></div>
<button class="btn" onclick="zombieMove(-1,0)">⬅️</button>
<button class="btn" onclick="zombieMove(0,-1)">⬆️</button>
<button class="btn" onclick="zombieMove(0,1)">⬇️</button>
<button class="btn" onclick="zombieMove(1,0)">➡️</button><button class="btn alt" onclick="zombieTag()">🧟 TAG</button>
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
  memoryPattern = Array.from({ length: 5 }, () => Math.floor(Math.random() * 16));
  memoryIndex = 0;
  const grid = $("memory"), output = $("memoryOut");
  if (!grid || !output) return;
  grid.replaceChildren();
  for (let i = 0; i < 16; i++) {
    const tile = document.createElement("button");
    tile.type = "button"; tile.className = "tile"; tile.textContent = "•";
    tile.setAttribute("aria-label", "Tile " + (i + 1));
    tile.addEventListener("click", () => memoryGuess(i)); grid.appendChild(tile);
  }
  output.textContent = "Watch the pattern...";
  const tiles = [...grid.children]; let n = 0;
  const showNext = () => {
    tiles.forEach(t => { t.style.background = "#101a35"; t.style.color = "#00eaff"; });
    if (n >= memoryPattern.length) { output.textContent = "Now repeat the pattern by tapping the tiles."; return; }
    const tile = tiles[memoryPattern[n++]]; tile.style.background = "#8dffb1"; tile.style.color = "#061018";
    setTimeout(showNext, 650);
  };
  setTimeout(showNext, 350);
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
    snakeFood.x * cellW + 2,
    snakeFood.y * cellH + 2,
    cellW - 4,
    cellH - 4
  );

  snake.forEach((part, index) => {
    snakeCtx.fillStyle = index === 0 ? "#00eaff" : "#00a8cc";
    snakeCtx.shadowColor = "#00eaff";
    snakeCtx.shadowBlur = index === 0 ? 10 : 3;
    snakeCtx.beginPath();
    snakeCtx.roundRect(
      part.x * cellW + 1,
      part.y * cellH + 1,
      cellW - 2,
      cellH - 2,
      4
    );
    snakeCtx.fill();
  });

  snakeCtx.shadowBlur = 0;
}

// KEYBOARD CONTROLS
document.addEventListener("keydown", event => {
  const keys = {
    ArrowUp: [0, -1],
    ArrowDown: [0, 1],
    ArrowLeft: [-1, 0],
    ArrowRight: [1, 0]
  };

  if (keys[event.key] && document.activeElement?.tagName !== "INPUT") {
    event.preventDefault();
    snakeDir(...keys[event.key]);
  }
});

snakeDraw();

// RACING GAME
const road = $("road");
const roadCtx = road ? road.getContext("2d") : null;
let raceRunning = false;
let raceFrame = null;
let raceLane = 1;
let raceDistance = 0;
let raceObstacles = [];
let raceLastTime = 0;

function raceStart() {
  raceStop();
  raceRunning = true;
  raceLane = 1;
  raceDistance = 0;
  raceObstacles = [];
  raceLastTime = performance.now();
  if ($("raceOut")) $("raceOut").textContent = "Race started!";
  raceFrame = requestAnimationFrame(raceLoop);
}

function raceStop() {
  raceRunning = false;
  if (raceFrame) cancelAnimationFrame(raceFrame);
  raceFrame = null;
}

function raceMove(direction) {
  raceLane = Math.max(0, Math.min(2, raceLane + direction));
}

function raceLoop(now) {
  if (!raceRunning || !roadCtx) return;

  const dt = Math.min((now - raceLastTime) / 1000, 0.05);
  raceLastTime = now;

  if (!paused) {
    raceDistance += dt * 10;

    if (Math.random() < dt * 1.2) {
      raceObstacles.push({
        lane: Math.floor(Math.random() * 3),
        y: -30
      });
    }

    raceObstacles.forEach(o => o.y += dt * 180);
    raceObstacles = raceObstacles.filter(o => o.y < road.height + 40);

    if (raceObstacles.some(o => o.lane === raceLane && o.y > 350 && o.y < 405)) {
      raceStop();
      if ($("raceOut")) {
        $("raceOut").textContent = "Crash! Distance: " + Math.floor(raceDistance);
      }
      return;
    }
  }

  raceDraw();
  if ($("raceOut")) {
    $("raceOut").textContent =
      "Distance: " + Math.floor(raceDistance) +
      " | Vehicle: " + $("vehicle").value;
  }

  raceFrame = requestAnimationFrame(raceLoop);
}

function raceDraw() {
  if (!roadCtx) return;
  const w = road.width, h = road.height;
  roadCtx.fillStyle = "#101925";
  roadCtx.fillRect(0, 0, w, h);

  roadCtx.fillStyle = "#263747";
  roadCtx.fillRect(25, 0, w - 50, h);

  roadCtx.strokeStyle = "#00eaff";
  roadCtx.lineWidth = 3;
  roadCtx.strokeRect(25, 0, w - 50, h);

  roadCtx.strokeStyle = "#d6e4ee";
  roadCtx.lineWidth = 2;
  roadCtx.setLineDash([22, 18]);
  roadCtx.lineDashOffset = -raceDistance * 5;
  roadCtx.beginPath();
  roadCtx.moveTo(25 + (w - 50) / 3, 0);
  roadCtx.lineTo(25 + (w - 50) / 3, h);
  roadCtx.moveTo(25 + 2 * (w - 50) / 3, 0);
  roadCtx.lineTo(25 + 2 * (w - 50) / 3, h);
  roadCtx.stroke();
  roadCtx.setLineDash([]);

  raceObstacles.forEach(o => {
    const x = 25 + (o.lane + 0.5) * (w - 50) / 3;
    roadCtx.fillStyle = "#ff477e";
    roadCtx.shadowColor = "#ff477e";
    roadCtx.shadowBlur = 12;
    roadCtx.fillRect(x - 13, o.y, 26, 35);
  });

  roadCtx.shadowBlur = 0;
  const playerX = 25 + (raceLane + 0.5) * (w - 50) / 3;
  roadCtx.fillStyle = $("vehicle")?.value === "bike" ? "#00eaff" : "#ffd166";
  roadCtx.shadowColor = roadCtx.fillStyle;
  roadCtx.shadowBlur = 15;

  if ($("vehicle")?.value === "bike") {
    roadCtx.beginPath();
    roadCtx.ellipse(playerX, h - 65, 9, 24, 0, 0, Math.PI * 2);
    roadCtx.fill();
    roadCtx.fillStyle = "#eafcff";
    roadCtx.fillRect(playerX - 4, h - 88, 8, 12);
  } else {
    roadCtx.fillRect(playerX - 16, h - 88, 32, 50);
    roadCtx.fillStyle = "#071426";
    roadCtx.fillRect(playerX - 11, h - 81, 22, 12);
  }
  roadCtx.shadowBlur = 0;
}

// TERMINAL
function command() {
  const field = $("cmd");
  const out = $("out");
  if (!field || !out) return;

  const input = field.value.trim().toLowerCase();
  field.value = "";

  const commands = {
    help: "Commands: help, about, games, racing, date, browser, device, network, clear",
    about: "LAKSHMAN_2018 — Digital World.",
    games: "Available: Number Guess, RPS, Reflex, Memory, Snake, Runner, Zombie, Drive, Space.",
    racing: "Neon Racing Arena: use arrow buttons to change lanes.",
    date: new Date().toLocaleString(),
    browser: navigator.userAgent,
    device: navigator.platform || "Device information unavailable",
    network: navigator.onLine ? "Browser reports online." : "Browser reports offline."
  };

  if (input === "clear") {
    out.textContent = "";
  } else {
    out.textContent += "\n> " + input + "\n" +
      (commands[input] || "Unknown command. Type help.");
  }
  out.scrollTop = out.scrollHeight;
}

if ($("cmd")) {
  $("cmd").addEventListener("keydown", event => {
    if (event.key === "Enter") command();
  });
}

// SETTINGS AND LOCAL SAVE
function saveSettings() {
  try {
    localStorage.setItem("lakshman_settings", JSON.stringify({
      quality: $("gfxQuality")?.value || "auto",
      master: $("masterVolume")?.value || "1",
      music: $("musicVolume")?.value || "0.5",
      sfx: $("sfxVolume")?.value || "0.8"
    }));
    if ($("saveStatus")) $("saveStatus").textContent = "Settings and progress saved.";
  } catch (e) {
    if ($("saveStatus")) $("saveStatus").textContent = "Browser storage unavailable.";
  }
}

try {
  const settings = JSON.parse(localStorage.getItem("lakshman_settings") || "{}");
  if ($("gfxQuality")) $("gfxQuality").value = settings.quality || "auto";
  if ($("masterVolume")) $("masterVolume").value = settings.master ?? "1";
  if ($("musicVolume")) $("musicVolume").value = settings.music ?? "0.5";
  if ($("sfxVolume")) $("sfxVolume").value = settings.sfx ?? "0.8";
} catch (e) {}

if ($("saveNow")) {
  $("saveNow").addEventListener("click", saveSettings);
}

["gfxQuality", "masterVolume", "musicVolume", "sfxVolume"].forEach(id => {
  if ($(id)) $(id).addEventListener("change", saveSettings);
});

// BASIC THREE.JS SCENE SETUP
const scenes3D = {};

function createScene(id, background = 0x050816) {
  const host = $(id);
  if (!host || !window.THREE) {
    if (host) host.textContent = "3D graphics could not load. Check your internet connection.";
    return null;
  }

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(background);
  scene.fog = new THREE.Fog(background, 10, 45);

  const camera = new THREE.PerspectiveCamera(
    60,
    host.clientWidth / Math.max(host.clientHeight, 1),
    0.1,
    100
  );
  camera.position.set(0, 4, 9);
  camera.lookAt(0, 0, 0);

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
  renderer.setSize(host.clientWidth, host.clientHeight);
  renderer.shadowMap.enabled = true;
  host.replaceChildren(renderer.domElement);

  scene.add(new THREE.HemisphereLight(0xbfefff, 0x11152b, 2));
  const light = new THREE.DirectionalLight(0xffffff, 2);
  light.position.set(4, 8, 5);
  light.castShadow = true;
  scene.add(light);

  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(40, 40),
    new THREE.MeshStandardMaterial({ color: 0x101b2c, roughness: 0.9 })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -0.06;
  ground.receiveShadow = true;
  scene.add(ground);

  const data = { host, scene, camera, renderer, objects: [], active: true };
  scenes3D[id] = data;
  return data;
}

function makeCharacter(scene, color = 0x00eaff) {
  const group = new THREE.Group();
  const bodyMat = new THREE.MeshStandardMaterial({ color, roughness: 0.45 });
  const skinMat = new THREE.MeshStandardMaterial({ color: 0xffc49b, roughness: 0.8 });
  const darkMat = new THREE.MeshStandardMaterial({ color: 0x15223a, roughness: 0.7 });

  function sphere(radius, x, y, z, material) {
    const mesh = new THREE.Mesh(
      new THREE.SphereGeometry(radius, 16, 12),
      material
    );
    mesh.position.set(x, y, z);
    mesh.castShadow = true;
    group.add(mesh);
    return mesh;
  }

  function capsule(radius, length, x, y, z, material) {
    const mesh = new THREE.Mesh(
      new THREE.CapsuleGeometry(radius, length, 4, 8),
      material
    );
    mesh.position.set(x, y, z);
    mesh.castShadow = true;
    group.add(mesh);
    return mesh;
  }

  capsule(0.28, 0.62, 0, 1.05, 0, bodyMat);
  sphere(0.25, 0, 1.72, 0, skinMat);
  sphere(0.29, 0, 1.84, 0.01, darkMat);
  capsule(0.10, 0.42, -0.34, 1.04, 0, skinMat);
  capsule(0.10, 0.42, 0.34, 1.04, 0, skinMat);
  capsule(0.12, 0.45, -0.15, 0.40, 0, darkMat);
  capsule(0.12, 0.45, 0.15, 0.40, 0, darkMat);
  group.position.y = 0;
  scene.add(group);
  return group;
}

function makeRoad(scene) {
  const roadMesh = new THREE.Mesh(
    new THREE.PlaneGeometry(6, 45),
    new THREE.MeshStandardMaterial({ color: 0x202a39, roughness: 0.9 })
  );
  roadMesh.rotation.x = -Math.PI / 2;
  roadMesh.position.set(0, 0, -10);
  scene.add(roadMesh);

  for (let x of [-1, 1]) {
    const line = new THREE.Mesh(
      new THREE.BoxGeometry(0.035, 0.02, 45),
      new THREE.MeshBasicMaterial({ color: 0x00eaff })
    );
    line.position.set(x, 0.02, -10);
    scene.add(line);
  }
}

// RUNNER 3D
const runner = createScene("runner3d", 0x071326);
let runnerPlayer = null;
let runnerLane = 0;
let runnerRunning = false;
let runnerScore = 0;
let runnerLast = 0;
let runnerObstacles = [];

if (runner) {
  makeRoad(runner.scene);
  runner.camera.position.set(0, 4.5, 8);
  runner.camera.lookAt(0, 1, -4);
  runnerPlayer = makeCharacter(runner.scene);
  runnerPlayer.position.z = 3;
}

function runnerMove(direction) {
  runnerLane = Math.max(-1, Math.min(1, runnerLane + direction));
}

function runnerStart() {
  runnerRunning = true;
  runnerScore = 0;
  runnerLane = 0;
  runnerObstacles.forEach(o => runner.scene.remove(o));
  runnerObstacles = [];
  if (runnerPlayer) runnerPlayer.position.x = 0;
  runnerLast = performance.now();
  if ($("runnerOut")) $("runnerOut").textContent = "Run started!";
}

function runnerSpawnObstacle() {
  if (!runner) return;
  const mesh = new THREE.Mesh(
    new THREE.DodecahedronGeometry(0.55, 1),
    new THREE.MeshStandardMaterial({ color: 0xff477e, roughness: 0.45, metalness: 0.2 })
  );
  mesh.position.set((Math.floor(Math.random() * 3) - 1) * 2, 0.65, -18);
  mesh.castShadow = true;
  runner.scene.add(mesh);
  runnerObstacles.push(mesh);
}

// ZOMBIE 3D
const zombie = createScene("zombie3d", 0x0d160e);
let zombiePlayer = null;
let zombieTarget = null;
let zombieScore = 0;

if (zombie) {
  zombie.camera.position.set(0, 5, 10);
  zombie.camera.lookAt(0, 0.7, 0);
  zombiePlayer = makeCharacter(zombie.scene, 0x44cc77);
  zombieTarget = makeCharacter(zombie.scene, 0x8fae44);
  zombiePlayer.position.set(-2, 0, 2);
  zombieTarget.position.set(2, 0, -1);
}

function zombieMove(dx, dz) {
  if (!zombiePlayer) return;
  zombiePlayer.position.x = Math.max(-4, Math.min(4, zombiePlayer.position.x + dx));
  zombiePlayer.position.z = Math.max(-3, Math.min(4, zombiePlayer.position.z + dz));
}

function zombieTag() {
  if (!zombiePlayer || !zombieTarget) return;
  const distance = zombiePlayer.position.distanceTo(zombieTarget.position);
  if (distance < 1.8) {
    zombieScore++;
    if ($("zombieOut")) $("zombieOut").textContent = "Zombie tagged! Score: " + zombieScore;
    addXP(5);
    zombieTarget.position.set(Math.random() * 6 - 3, 0, -Math.random() * 3);
  } else if ($("zombieOut")) {
    $("zombieOut").textContent = "Move closer to the zombie first!";
  }
}

// DRIVE 3D
const drive = createScene("drive3d", 0x141923);
let drivePlayer = null;
let driveDistance = 0;
let driveLast = 0;
let driveObstacles = [];

if (drive) {
  makeRoad(drive.scene);
  drive.camera.position.set(0, 5, 9);
  drive.camera.lookAt(0, 0, -4);

  drivePlayer = new THREE.Group();
  const carBody = new THREE.Mesh(
    new THREE.BoxGeometry(1.1, 0.35, 1.8),
    new THREE.MeshStandardMaterial({ color: 0xff3355, metalness: 0.5, roughness: 0.3 })
  );
  carBody.position.y = 0.5;
  drivePlayer.add(carBody);

  const cabin = new THREE.Mesh(
    new THREE.BoxGeometry(0.7, 0.4, 0.8),
    new THREE.MeshStandardMaterial({ color: 0x87eaff, metalness: 0.4, roughness: 0.2 })
  );
  cabin.position.set(0, 0.85, -0.1);
  drivePlayer.add(cabin);
  drive.scene.add(drivePlayer);
  drivePlayer.position.z = 3;
}

function driveMove(direction) {
  if (!drivePlayer) return;
  drivePlayer.position.x = Math.max(-2, Math.min(2, drivePlayer.position.x + direction * 0.7));
}

function driveSpawn() {
  if (!drive) return;
  const mesh = new THREE.Mesh(
    new THREE.OctahedronGeometry(0.6, 0),
    new THREE.MeshStandardMaterial({ color: 0xffbb44 })
  );
  mesh.position.set((Math.floor(Math.random() * 3) - 1) * 1.6, 0.6, -20);
  drive.scene.add(mesh);
  driveObstacles.push(mesh);
}

// SPACE 3D
const space = createScene("space3d", 0x020411);
let spacePlayer = null;
let spaceTargets = [];
let spaceShots = [];
let spaceHits = 0;

if (space) {
  space.scene.fog = new THREE.Fog(0x020411, 12, 50);
  space.camera.position.set(0, 3, 10);
  space.camera.lookAt(0, 0, -5);

  const ship = new THREE.Group();
  const hull = new THREE.Mesh(
    new THREE.ConeGeometry(0.45, 1.4, 8),
    new THREE.MeshStandardMaterial({ color: 0x00eaff, metalness: 0.65, roughness: 0.25 })
  );
  hull.rotation.x = -Math.PI / 2;
  ship.add(hull);

  const wingMat = new THREE.MeshStandardMaterial({ color: 0x346bff, metalness: 0.4 });
  for (const side of [-1, 1]) {
    const wing = new THREE.Mesh(new THREE.BoxGeometry(0.75, 0.08, 0.35), wingMat);
    wing.position.set(side * 0.45, 0, 0.15);
    ship.add(wing);
  }
  space.scene.add(ship);
  spacePlayer = ship;
  spacePlayer.position.z = 4;

  for (let i = 0; i < 35; i++) {
    const star = new THREE.Mesh(
      new THREE.SphereGeometry(0.035, 6, 6),
      new THREE.MeshBasicMaterial({ color: 0xffffff })
    );
    star.position.set(Math.random() * 18 - 9, Math.random() * 9 - 4, -Math.random() * 35);
    space.scene.add(star);
  }
}

function spaceMove(direction) {
  if (!spacePlayer) return;
  spacePlayer.position.x = Math.max(-4, Math.min(4, spacePlayer.position.x + direction * 0.6));
}

function spaceShoot() {
  if (!space || !spacePlayer) return;
  const shot = new THREE.Mesh(
    new THREE.SphereGeometry(0.12, 8, 8),
    new THREE.MeshBasicMaterial({ color: 0x00eaff })
  );
  shot.position.copy(spacePlayer.position);
  shot.position.y += 0.1;
  space.scene.add(shot);
  spaceShots.push(shot);
}

// GAME ANIMATION LOOP
let lastFrame = performance.now();

function animate3D(now) {
  requestAnimationFrame(animate3D);
  const dt = Math.min((now - lastFrame) / 1000, 0.05);
  lastFrame = now;

  Object.values(scenes3D).forEach(data => {
    if (!data || !data.active) return;
    if (!paused) {
      data.objects.forEach(obj => {
        if (obj.rotation) obj.rotation.y += dt;
      });
    }
    data.renderer.render(data.scene, data.camera);
  });

  if (paused) return;

  // Runner
  if (runner && runnerRunning) {
    runnerPlayer.position.x += (runnerLane * 2 - runnerPlayer.position.x) * Math.min(1, dt * 8);
    runnerScore += dt * 10;

    if (Math.random() < dt * 0.9) runnerSpawnObstacle();

    runnerObstacles.forEach(o => {
      o.position.z += dt * 8;
      o.rotation.x += dt;
      o.rotation.y += dt * 1.8;
    });

    runnerObstacles = runnerObstacles.filter(o => {
      if (o.position.z > 5) {
        runner.scene.remove(o);
        return false;
      }
      if (Math.abs(o.position.x - runnerPlayer.position.x) < 0.8 &&
          Math.abs(o.position.z - runnerPlayer.position.z) < 1) {
        runnerRunning = false;
        if ($("runnerOut")) $("runnerOut").textContent = "Collision! Score: " + Math.floor(runnerScore);
        return true;
      }
      return true;
    });

    if ($("runnerOut")) $("runnerOut").textContent = "Score: " + Math.floor(runnerScore);
  }

  // Drive
  if (drive) {
    driveDistance += dt * 5;
    if (Math.random() < dt * 0.65) driveSpawn();

    driveObstacles.forEach(o => o.position.z += dt * 7);
    driveObstacles = driveObstacles.filter(o => {
      if (o.position.z > 5) {
        drive.scene.remove(o);
        return false;
      }
      if (Math.abs(o.position.x - drivePlayer.position.x) < 0.8 &&
          Math.abs(o.position.z - drivePlayer.position.z) < 1) {
        driveDistance = 0;
        if ($("driveOut")) $("driveOut").textContent = "Crash! Press a direction to recover.";
        drivePlayer.position.x = 0;
        return false;
      }
      return true;
    });

    if ($("driveOut")) $("driveOut").textContent = "Distance: " + Math.floor(driveDistance);
  }

  // Space shots and targets
  if (space) {
    if (Math.random() < dt * 0.5) {
      const target = new THREE.Mesh(
        new THREE.IcosahedronGeometry(0.45, 1),
        new THREE.MeshStandardMaterial({ color: 0xff477e, emissive: 0x550011 })
      );
      target.position.set(Math.random() * 7 - 3.5, Math.random() * 2 - 1, -22);
      space.scene.add(target);
      spaceTargets.push(target);
    }

    spaceTargets.forEach(target => {
      target.position.z += dt * 5;
      target.rotation.x += dt;
      target.rotation.y += dt * 2;
    });

    spaceShots.forEach(shot => shot.position.z -= dt * 15);

    spaceShots = spaceShots.filter(shot => {
      if (shot.position.z < -25) {
        space.scene.remove(shot);
        return false;
      }

      const hit = spaceTargets.findIndex(target =>
        shot.position.distanceTo(target.position) < 0.7
      );

      if (hit >= 0) {
        space.scene.remove(shot);
        space.scene.remove(spaceTargets[hit]);
        spaceTargets.splice(hit, 1);
        spaceHits++;
        if ($("spaceOut")) $("spaceOut").textContent = "Targets hit: " + spaceHits;
        addXP(2);
        return false;
      }
      return true;
    });
  }

  // Animated scenery
  if (runner) runner.scene.children.forEach(o => {
    if (o.geometry && o.geometry.type === "PlaneGeometry" && o.rotation.x === -Math.PI / 2) {
      o.position.z += dt * 2;
      if (o.position.z > 10) o.position.z = -15;
    }
  });
}

requestAnimationFrame(animate3D);

// RESIZE
window.addEventListener("resize", () => {
  Object.values(scenes3D).forEach(data => {
    const w = Math.max(1, data.host.clientWidth);
    const h = Math.max(1, data.host.clientHeight);
    data.camera.aspect = w / h;
    data.camera.updateProjectionMatrix();
    data.renderer.setSize(w, h);
  });
});

// GLOBAL KEYBOARD
document.addEventListener("keydown", event => {
  if (event.key === "ArrowLeft") {
    raceMove(-1);
    runnerMove(-1);
    driveMove(-1);
    spaceMove(-1);
  }
  if (event.key === "ArrowRight") {
    raceMove(1);
    runnerMove(1);
    driveMove(1);
    spaceMove(1);
  }
});

</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
