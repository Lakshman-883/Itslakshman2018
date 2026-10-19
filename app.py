
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
footer{text-align:center;padding:25px;border-top:1px solid #00eaff33;color:#9eacc7}footer a{color:#00eaff}kbd{border:1px solid #00eaff66;border-radius:4px;padding:2px 6px}
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
<div style="perspective:900px;max-width:330px;margin:auto"><canvas id="snake" width="300" height="300" style="transform:rotateX(5deg);transform-origin:center;box-shadow:0 18px 28px #0009,0 0 20px #00eaff18"></canvas></div>
<div style="text-align:center">
<button class="btn" onclick="snakeDir(0,-1)">⬆️</button><br>
<button class="btn" onclick="snakeDir(-1,0)">⬅️</button>
<button class="btn" onclick="snakeDir(0,1)">⬇️</button>
<button class="btn" onclick="snakeDir(1,0)">➡️</button><br>
<button class="btn alt" onclick="snakeStart()">RESTART</button>
</div><div id="snakeOut" class="result">Score: 0</div></div>
</div></section>

<section id="race">
<h2 class="heading">🏁 NEON RACING ARENA</h2><div class="card">
<h3>Choose Your Vehicle</h3>
<select id="vehicle"><option value="bike">🏍️ Neon Bike</option><option value="car">🏎️ Super Car</option></select>
<button class="btn" onclick="raceStart()">START RACE</button>
<button class="btn alt" onclick="raceStop()">STOP</button>
<div style="perspective:850px;max-width:330px;margin:auto"><canvas id="road" width="300" height="440" style="transform:rotateX(4deg);transform-origin:center;box-shadow:0 22px 32px #000a,0 0 22px #00eaff14"></canvas></div>
<div style="text-align:center">
<button class="btn" onclick="raceMove(-1)">⬅️ LEFT</button>
<button class="btn" onclick="raceMove(1)">RIGHT ➡️</button>
</div>
<div id="raceOut" class="result">Choose a vehicle and start.</div>
<p>Desktop: arrow keys. Mobile: use the buttons.</p>
</div></section>

<section id="3dgames">
<h2 class="heading">🕹️ 3D GAMING ZONE</h2>
<p style="text-align:center;color:#c3cce0">Play the 3D browser games.</p>
<div class="grid">
<div class="card"><h3>🏃 Neon Runner 3D</h3>
<p>Switch lanes and dodge blocks.</p><div id="runner3d" class="game3d"></div>
<button class="btn" onclick="runnerMove(-1)">⬅️</button>
<button class="btn" onclick="runnerStart()">START / RESTART</button>
<button class="btn" onclick="runnerMove(1)">➡️</button>
<div id="runnerOut" class="result">Press start.</div></div>

<div class="card"><h3>🧟 Zombie Survival 3D</h3>
<p>Click zombies to tag them.</p><div id="zombie3d" class="game3d"></div>
<button class="btn" onclick="zombieMove(-1,0)">⬅️</button>
<button class="btn" onclick="zombieMove(0,-1)">⬆️</button>
<button class="btn" onclick="zombieMove(0,1)">⬇️</button>
<button class="btn" onclick="zombieMove(1,0)">➡️</button>
<div id="zombieOut" class="result">Click a zombie to score.</div></div>

<div class="card"><h3>🚗 3D Drift Drive</h3>
<p>Steer and avoid barriers.</p><div id="drive3d" class="game3d"></div>
<button class="btn" onclick="driveMove(-1)">⬅️ LEFT</button>
<button class="btn" onclick="driveMove(1)">RIGHT ➡️</button>
<div id="driveOut" class="result">Distance: 0</div></div>

<div class="card"><h3>🚀 Space Blaster 3D</h3>
<p>Move your ship and fire.</p><div id="space3d" class="game3d"></div>
<button class="btn" onclick="spaceMove(-1)">⬅️</button>
<button class="btn" onclick="spaceShoot()">🔥 FIRE</button>
<button class="btn" onclick="spaceMove(1)">➡️</button>
<div id="spaceOut" class="result">Targets hit: 0</div></div>
</div></section>

<section id="terminal">
<h2 class="heading">💻 DIGITAL TERMINAL</h2><div class="terminal">
<div id="out">Welcome to Lakshman Terminal.
Type help to see available commands.</div>
<div class="row"><span>&gt;</span>
<input id="cmd" placeholder="Type a command" autocomplete="off">
<button class="btn" onclick="command()">RUN</button></div>
</div>
<p>Commands: help, about, games, racing, date, browser, device, network, clear</p>
<p style="color:#9eacc7">Demo terminal only. It cannot execute real operating-system commands.</p>
</section>

<section id="settings">
<h2 class="heading">⚙️ GAMING CONTROL CENTER</h2>
<div class="card">
<p>Shared settings for the browser games. Graphics presets are best-effort and depend on device/browser support.</p>
<div class="grid">
<div><label for="gfxQuality">Graphics quality</label><select id="gfxQuality"><option value="auto">Auto</option><option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option><option value="ultra">Ultra</option></select></div>
<div><label for="masterVolume">Master volume (saved setting)</label><input id="masterVolume" type="range" min="0" max="1" step="0.05"></div>
<div><label for="musicVolume">Music volume (saved setting)</label><input id="musicVolume" type="range" min="0" max="1" step="0.05"></div>
<div><label for="sfxVolume">SFX volume (saved setting)</label><input id="sfxVolume" type="range" min="0" max="1" step="0.05"></div>
</div>
<div class="grid">
<div class="card"><h3>Player Progress</h3><p>Level: <strong id="playerLevel">1</strong></p><p>Total XP: <strong id="playerXP">0</strong></p></div>
<div class="card"><h3>Save Status</h3><p id="saveStatus" class="result" aria-live="polite">Local save ready.</p><button class="btn" id="saveNow">SAVE NOW</button></div>
<div class="card"><h3>Game Controls</h3><p>Use the in-game buttons or keyboard arrows. Press <kbd>P</kbd> to pause/resume the 3D simulation.</p><button class="btn" id="pauseToggle">PAUSE 3D GAMES</button><p id="pauseStatus" class="result">Games running</p></div>
</div>
<p style="color:#9eacc7">Local saves stay in this browser/device. Clearing browser data may erase progress. Audio sliders store preferences; actual sound playback must be connected to game audio assets separately.</p>
</div></section>

<section id="contact">
<h2 class="heading">CONTACT ME</h2><div class="card" style="text-align:center">
<h3>Let's Connect</h3><p>Follow my social media for updates.</p>
<a class="btn" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">INSTAGRAM</a>
</div></section>

<footer>© <span id="year"></span> LAKSHMAN_2018 | Digital World ⚡<br><p><a href="#home">Home</a> · <a href="#about">About</a> · <a href="#projects">Projects</a> · <a href="#games">Mini-games</a> · <a href="#race">Racing</a> · <a href="#3dgames">3D games</a> · <a href="#settings">Gaming settings</a> · <a href="#terminal">Terminal</a> · <a href="#contact">Contact</a></p></footer>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
// 3D game animation loop
let paused3D=false;
const gameClock=new THREE.Clock();

function animate3D(){
 requestAnimationFrame(animate3D);
 const dt=Math.min(gameClock.getDelta(),.05);

 Object.values(scenes3d).forEach(w=>{
  if(!w||!w.renderer||!w.scene||!w.camera)return;
  if(!paused3D&&typeof w.tick==="function")w.tick(dt);
  w.renderer.render(w.scene,w.camera);
 });
}
animate3D();

// Pause/resume 3D simulations
function toggle3DPause(){
 paused3D=!paused3D;
 const button=$("pauseToggle");
 const status=$("pauseStatus");

 if(button)button.textContent=paused3D?"RESUME 3D GAMES":"PAUSE 3D GAMES";
 if(status)status.textContent=paused3D?"Games paused":"Games running";
}

if($("pauseToggle")){
 $("pauseToggle").addEventListener("click",toggle3DPause);
}

document.addEventListener("keydown",e=>{
 if(e.key.toLowerCase()==="p"&&!["INPUT","TEXTAREA","SELECT"].includes(document.activeElement.tagName)){
  toggle3DPause();
 }
});

// Graphics quality preference
if($("gfxQuality")){
 $("gfxQuality").addEventListener("change",()=>{
  const quality=$("gfxQuality").value;
  const pixelRatio=quality==="low"?1:
                   quality==="medium"?1.25:
                   quality==="high"?1.75:
                   quality==="ultra"?2:
                   Math.min(window.devicePixelRatio||1,1.5);

  Object.values(scenes3d).forEach(w=>{
   if(w&&w.renderer){
    w.renderer.setPixelRatio(pixelRatio);
    w.renderer.setSize(w.host.clientWidth||300,w.host.clientHeight||210);
   }
  });
 });
}
// Terminal commands
function command(){
 const input=$("cmd");
 const output=$("out");
 if(!input||!output)return;

 const cmd=input.value.trim().toLowerCase();
 input.value="";
 if(!cmd)return;

 const commands={
  help:"Available commands: help, about, games, racing, date, browser, device, network, clear",
  about:"LAKSHMAN_2018 — Welcome to my Digital World!",
  games:"Available games: Mini-games, Racing Arena, Neon Runner, Zombie Survival, Drift Drive and Space Blaster.",
  racing:"Racing Arena: Use the left and right arrow buttons to avoid obstacles.",
  date:new Date().toLocaleString(),
  browser:"Browser: "+navigator.userAgent,
  device:"Screen: "+screen.width+" × "+screen.height,
  network:navigator.onLine?"Network status: Online":"Network status: Offline"
 };

 if(cmd==="clear"){
  output.textContent="Terminal cleared. Type help to see commands.";
  return;
 }

 output.textContent+="\n\n> "+cmd+"\n"+(commands[cmd]||"Unknown command. Type help to see available commands.");
}

// Terminal Enter key
if($("cmd")){
 $("cmd").addEventListener("keydown",e=>{
  if(e.key==="Enter")command();
 });
}

// Update footer year
if($("year"))$("year").textContent=new Date().getFullYear();

// Settings defaults
const settingsDefaults={
 gfxQuality:"auto",
 masterVolume:"0.8",
 musicVolume:"0.5",
 sfxVolume:"0.8"
};

function loadSettings(){
 Object.entries(settingsDefaults).forEach(([id,value])=>{
  const el=$(id);
  if(!el)return;
  try{
   el.value=localStorage.getItem("lakshman_"+id)||value;
  }catch(err){
   el.value=value;
  }
 });
}

function saveSettings(){
 Object.keys(settingsDefaults).forEach(id=>{
  const el=$(id);
  if(!el)return;
  try{
   localStorage.setItem("lakshman_"+id,el.value);
  }catch(err){}
 });

 if($("saveStatus"))$("saveStatus").textContent="Settings saved on this device.";
}

loadSettings();

["gfxQuality","masterVolume","musicVolume","sfxVolume"].forEach(id=>{
 const el=$(id);
 if(el){
  el.addEventListener("change",saveSettings);
  el.addEventListener("input",()=>{
   if(id!=="gfxQuality")saveSettings();
  });
 }
});

if($("saveNow"))$("saveNow").addEventListener("click",saveSettings);
// Player progress and XP
let playerXP=0;
let playerLevel=1;

function addXP(amount){
 playerXP+=Math.max(0,Number(amount)||0);
 playerLevel=Math.floor(playerXP/100)+1;

 if($("playerXP"))$("playerXP").textContent=playerXP;
 if($("playerLevel"))$("playerLevel").textContent=playerLevel;

 saveProgress();
}

function saveProgress(){
 try{
  localStorage.setItem("lakshman_playerXP",String(playerXP));
  localStorage.setItem("lakshman_playerLevel",String(playerLevel));
 }catch(err){}
}

function loadProgress(){
 try{
  playerXP=Math.max(0,Number(localStorage.getItem("lakshman_playerXP"))||0);
  playerLevel=Math.floor(playerXP/100)+1;
 }catch(err){
  playerXP=0;
  playerLevel=1;
 }

 if($("playerXP"))$("playerXP").textContent=playerXP;
 if($("playerLevel"))$("playerLevel").textContent=playerLevel;
}

loadProgress();

// Online/offline indicator
window.addEventListener("online",()=>{
 if($("saveStatus"))$("saveStatus").textContent="Internet connected.";
});

window.addEventListener("offline",()=>{
 if($("saveStatus"))$("saveStatus").textContent="Offline. Local games remain available.";
});

// Finish page initialization
window.addEventListener("load",()=>{
 if($("year"))$("year").textContent=new Date().getFullYear();
 console.log("LAKSHMAN_2018 Digital World loaded.");
});
