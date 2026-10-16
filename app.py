from flask import Flask, render_template_string, jsonify, request
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#050816">
<title>itslakshman2018 | Digital World</title>

<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--blue:#00eaff;--purple:#9d4edd;--bg:#050816;--panel:rgba(10,20,45,.9);--text:#f2f7ff}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:Arial,sans-serif;overflow-x:hidden}
#matrix{position:fixed;inset:0;width:100%;height:100%;opacity:.12;z-index:-1;pointer-events:none}
a{color:inherit;text-decoration:none}
header{position:sticky;top:0;z-index:50;background:rgba(3,7,20,.96);border-bottom:1px solid #00eaff55;padding:15px 5%;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:15px}
.logo{font-size:22px;font-weight:900;color:var(--blue);text-shadow:0 0 15px var(--blue)}
nav{display:flex;flex-wrap:wrap;gap:13px}
nav a{font-size:12px;font-weight:bold}
nav a:hover{color:var(--blue)}
section{padding:65px 7%;scroll-margin-top:75px}
.hero{min-height:78vh;display:flex;align-items:center;justify-content:center;text-align:center}
.hero h1{font-size:clamp(36px,8vw,75px);color:var(--blue);text-shadow:0 0 25px #00eaff66;margin:15px 0}
.hero p{color:#c0cbe1;font-size:17px;line-height:1.8}
.badge{display:inline-block;border:1px solid var(--blue);color:var(--blue);border-radius:25px;padding:8px 16px;font-size:12px}
.btn{display:inline-block;background:var(--blue);color:#001018;padding:11px 17px;margin:7px 3px;border:0;border-radius:7px;font-weight:bold;cursor:pointer}
.btn:hover{box-shadow:0 0 18px #00eaff77}
.secondary{background:transparent;color:var(--blue);border:1px solid var(--blue)}
.heading{color:var(--blue);text-align:center;font-size:30px;margin-bottom:28px}
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px}
.card{background:var(--panel);border:1px solid #00eaff33;border-radius:13px;padding:22px;transition:.25s;min-width:0}
.card:hover{border-color:var(--blue);transform:translateY(-3px)}
.card h3{color:var(--blue);margin-bottom:12px}
.card p{color:#c3cce0;line-height:1.7}
.small-text{color:#9eacc7;font-size:13px;line-height:1.7}
input,select{background:#080e20;color:white;border:1px solid #00eaff66;border-radius:6px;padding:11px;width:100%;margin:8px 0;outline:none}
.game-result{min-height:28px;margin:12px 0;color:#8dffb1;line-height:1.6;overflow-wrap:anywhere}
.memory-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:7px;max-width:340px;margin:15px auto}
.memory-tile{height:50px;border:1px solid var(--blue);background:#101a35;color:var(--blue);font-size:22px;border-radius:7px;cursor:pointer}
#snakeCanvas{display:block;width:100%;max-width:300px;height:auto;margin:15px auto;background:#02060c;border:1px solid var(--blue)}
#raceCanvas{display:block;width:100%;max-width:600px;height:auto;margin:15px auto;background:#080d18;border:1px solid var(--blue);border-radius:8px;touch-action:pan-y}
.race-controls{display:flex;justify-content:center;gap:15px;flex-wrap:wrap}
.race-controls .btn{min-width:110px;font-size:18px;touch-action:manipulation}
.terminal{background:#02050b;border:1px solid #00eaff66;border-radius:10px;padding:18px;font-family:monospace;color:#8dffb1}
.terminal-output{height:200px;overflow-y:auto;white-space:pre-wrap;line-height:1.6;font-size:13px;overflow-wrap:anywhere}
.terminal-row{display:flex;gap:8px;align-items:center}
.terminal-row input{flex:1;min-width:0;font-family:monospace}
footer{padding:25px;text-align:center;border-top:1px solid #00eaff33;color:#8d9ab3;font-size:12px}
@media(max-width:600px){header{justify-content:center}nav{justify-content:center;gap:11px}section{padding:48px 5%}.hero{min-height:65vh}.heading{font-size:26px}}
</style>
</head>
<body>

<canvas id="matrix"></canvas>

<header>
<a href="#home" class="logo">LAKSHMAN_2018</a>
<nav>
<a href="#home">HOME</a>
<a href="#about">ABOUT</a>
<a href="#projects">PROJECTS</a>
<a href="#gaming">GAMING</a>
<a href="#racing">RACING</a>
<a href="#terminal">TERMINAL</a>
<a href="#contact">CONTACT</a>
</nav>
</header>

<section class="hero" id="home">
<div>
<div class="badge">WELCOME TO MY DIGITAL WORLD</div>
<h1>ITS LAKSHMAN</h1>
<p>Creator | Gamer | Digital Explorer<br>Welcome to my futuristic neon universe.</p>
<a href="#projects" class="btn">EXPLORE PROJECTS</a>
<a href="#gaming" class="btn secondary">PLAY GAMES</a>
</div>
</section>

<section id="about">
<h2 class="heading">ABOUT ME</h2>
<div class="card">
<h3>Who Am I?</h3>
<p>Welcome to ItsLakshman2018 — my personal digital space for creativity, gaming and web projects. Explore the website and try the interactive games.</p>
</div>
</section>

<section id="projects">
<h2 class="heading">MY PROJECTS</h2>
<div class="card-grid">
<div class="card"><h3>🌐 Portfolio</h3><p>A futuristic personal website with a neon design.</p></div>
<div class="card"><h3>🎮 Gaming Zone</h3><p>Browser-based mini-games you can play here.</p></div>
<div class="card"><h3>🏎️ Racing Arena</h3><p>Choose a vehicle, avoid traffic and beat your distance.</p></div>
<div class="card"><h3>💻 Digital Terminal</h3><p>Explore the available terminal commands.</p></div>
</div>
</section>

<section id="gaming">
<h2 class="heading">🎮 GAMING ZONE</h2>
<div class="card-grid">

<div class="card">
<h3>🔢 Number Guess</h3>
<p>Guess the secret number from 1 to 100.</p>
<input id="guessInput" type="number" min="1" max="100" placeholder="Enter number">
<button class="btn" onclick="guessNumber()">GUESS</button>
<button class="btn secondary" onclick="resetGuess()">RESET</button>
<div id="guessResult" class="game-result"></div>
</div>

<div class="card">
<h3>✊ Rock Paper Scissors</h3>
<p>Play against the computer.</p>
<button class="btn" onclick="playRPS('Rock')">✊ Rock</button>
<button class="btn" onclick="playRPS('Paper')">✋ Paper</button>
<button class="btn" onclick="playRPS('Scissors')">✌️ Scissors</button>
<div id="rpsResult" class="game-result"></div>
<p id="rpsScore" class="small-text">You: 0 | Computer: 0</p>
</div>

<div class="card">
<h3>⚡ Reflex Test</h3>
<p>Wait for green, then click as quickly as possible.</p>
<button id="reflexButton" class="btn" onclick="reflexClick()">START TEST</button>
<div id="reflexResult" class="game-result"></div>
</div>

<div class="card">
<h3>🧠 Memory Matrix</h3>
<p>Remember the highlighted tiles and repeat the pattern.</p>
<button class="btn" onclick="startMemory()">START</button>
<div id="memoryGrid" class="memory-grid"></div>
<div id="memoryResult" class="game-result"></div>
</div>

<div class="card">
<h3>🐍 Snake Game</h3>
<p>Use arrow keys or buttons to control the snake.</p>
<canvas id="snakeCanvas" width="300" height="300"></canvas>
<div style="text-align:center">
<button class="btn" onclick="setSnakeDirection(0,-1)">⬆️</button><br>
<button class="btn" onclick="setSnakeDirection(-1,0)">⬅️</button>
<button class="btn" onclick="setSnakeDirection(0,1)">⬇️</button>
<button class="btn" onclick="setSnakeDirection(1,0)">➡️</button><br>
<button class="btn secondary" onclick="startSnake()">RESTART</button>
</div>
<div id="snakeScore" class="game-result">Score: 0</div>
</div>

</div>
</section>

<section id="racing">
<h2 class="heading">🏁 NEON RACING ARENA</h2>
<div class="card">
<h3>Choose Your Vehicle</h3>
<select id="vehicleSelect">
<option value="bike">🏍️ Neon Bike</option>
<option value="car">🏎️ Super Car</option>
</select>
<p class="small-text">Avoid traffic and travel as far as possible.</p>
<div style="text-align:center">
<button class="btn" onclick="startRace()">START RACE</button>
<button class="btn secondary" onclick="stopRace()">STOP</button>
</div>
<canvas id="raceCanvas" width="600" height="650"></canvas>
<div class="race-controls">
<button class="btn" id="leftRace">⬅️ LEFT</button>
<button class="btn" id="rightRace">RIGHT ➡️</button>
</div>
<div id="raceStatus" class="game-result">Choose a vehicle and press START RACE.</div>
<p class="small-text">Computer: use ← and → arrow keys. Mobile: use LEFT and RIGHT buttons.</p>
</div>
</section>

<section id="terminal">
<h2 class="heading">💻 DIGITAL TERMINAL</h2>
<div class="terminal">
<div id="terminalOutput" class="terminal-output">Welcome to Lakshman Terminal.
Type help to see available commands.</div>
<div class="terminal-row">
<span>&gt;</span>
<input id="terminalInput" type="text" placeholder="Type a command..." autocomplete="off">
<button class="btn" onclick="runCommand()">RUN</button>
</div>
</div>
<p class="small-text" style="margin-top:12px">Try: help, about, games, racing, ip, location, browser, device, network</p>
</section>

<section id="contact">
<h2 class="heading">CONTACT ME</h2>
<div class="card" style="text-align:center">
<h3>Let's Connect</h3>
<p>Follow my social media for updates, gaming and new projects.</p>
<a class="btn" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">INSTAGRAM</a>
</div>
</section>

<footer>© <span id="year"></span> ItsLakshman2018 | Digital World ⚡</footer>

<script>
// MATRIX BACKGROUND
const matrixCanvas=document.getElementById("matrix");
const matrixCtx=matrixCanvas.getContext("2d");
let matrixColumns=[];
const matrixFont=15;

function resizeMatrix(){
 matrixCanvas.width=window.innerWidth;
 matrixCanvas.height=window.innerHeight;
 matrixColumns=Array.from({length:Math.ceil(matrixCanvas.width/matrixFont)},()=>Math.random()*matrixCanvas.height/matrixFont);
}
function drawMatrix(){
 matrixCtx.fillStyle="rgba(5,8,22,0.12)";
 matrixCtx.fillRect(0,0,matrixCanvas.width,matrixCanvas.height);
 matrixCtx.fillStyle="#00eaff";
 matrixCtx.font=matrixFont+"px monospace";
 const chars="01LAKSHMANアイウエオ";
 matrixColumns.forEach((y,i)=>{
  matrixCtx.fillText(chars[Math.floor(Math.random()*chars.length)],i*matrixFont,y*matrixFont);
  matrixColumns[i]=(y*matrixFont>matrixCanvas.height&&Math.random()>.975)?0:y+.6;
 });
}
resizeMatrix();
window.addEventListener("resize",resizeMatrix);
setInterval(drawMatrix,55);

// NUMBER GUESS
let secretNumber=Math.floor(Math.random()*100)+1;
let guessCount=0;
function guessNumber(){
 const input=document.getElementById("guessInput");
 const value=Number(input.value);
 const result=document.getElementById("guessResult");
 if(!input.value||value<1||value>100){result.textContent="Enter a number from 1 to 100.";return;}
 guessCount++;
 if(value===secretNumber)result.textContent="🎉 Correct! Attempts: "+guessCount;
 else if(value<secretNumber)result.textContent="⬆️ Too low! Try higher.";
 else result.textContent="⬇️ Too high! Try lower.";
}
function resetGuess(){
 secretNumber=Math.floor(Math.random()*100)+1;
 guessCount=0;
 document.getElementById("guessInput").value="";
 document.getElementById("guessResult").textContent="New number generated!";
}

// ROCK PAPER SCISSORS
let rpsYou=0,rpsComputer=0;
function playRPS(choice){
 const options=["Rock","Paper","Scissors"];
 const computer=options[Math.floor(Math.random()*3)];
 let message;
 if(choice===computer)message="Draw!";
 else if((choice==="Rock"&&computer==="Scissors")||(choice==="Paper"&&computer==="Rock")||(choice==="Scissors"&&computer==="Paper")){message="You win!";rpsYou++;}
 else{message="Computer wins!";rpsComputer++;}
 document.getElementById("rpsResult").textContent="You: "+choice+" | Computer: "+computer+" | "+message;
 document.getElementById("rpsScore").textContent="You: "+rpsYou+" | Computer: "+rpsComputer;
}

// REFLEX TEST
let reflexState="idle",reflexTimer=null,reflexStart=0;
function reflexClick(){
 const button=document.getElementById("reflexButton");
 const result=document.getElementById("reflexResult");
 if(reflexState==="idle"){
  reflexState="waiting";button.textContent="WAIT FOR GREEN...";button.style.background="#d62828";button.style.color="white";
  result.textContent="Don't click until the button turns green!";
  reflexTimer=setTimeout(()=>{
   reflexState="ready";reflexStart=performance.now();button.textContent="CLICK NOW!";button.style.background="#00d26a";button.style.color="#001018";
  },1500+Math.random()*3000);
 }else if(reflexState==="waiting"){
  clearTimeout(reflexTimer);reflexState="idle";button.textContent="TRY AGAIN";button.style.background="";button.style.color="";
  result.textContent="Too early! Wait for green.";
 }else{
  const elapsed=Math.round(performance.now()-reflexStart);
  reflexState="idle";button.textContent="PLAY AGAIN";button.style.background="";button.style.color="";
  result.textContent="⚡ Reaction time: "+elapsed+" ms";
 }
}

// MEMORY MATRIX
let memoryPattern=[],memoryUser=[],memoryLocked=false;
function startMemory(){
 const grid=document.getElementById("memoryGrid");
 grid.innerHTML="";memoryPattern=[];memoryUser=[];memoryLocked=true;
 for(let i=0;i<16;i++){
  const b=document.createElement("button");b.className="memory-tile";b.textContent="·";b.dataset.index=i;
  b.onclick=()=>memoryPick(i);grid.appendChild(b);
 }
 while(memoryPattern.length<4){const n=Math.floor(Math.random()*16);if(!memoryPattern.includes(n))memoryPattern.push(n);}
 const tiles=grid.querySelectorAll("button");
 memoryPattern.forEach((index,order)=>{
  setTimeout(()=>{
   tiles[index].textContent="★";tiles[index].style.background="#00eaff";tiles[index].style.color="#001018";
   setTimeout(()=>{tiles[index].textContent="·";tiles[index].style.background="";tiles[index].style.color="";},500);
  },order*650);
 });
 document.getElementById("memoryResult").textContent="Remember the pattern!";
 setTimeout(()=>{memoryLocked=false;document.getElementById("memoryResult").textContent="Now tap the same tiles.";},4*650+600);
}
function memoryPick(index){
 if(memoryLocked||memoryUser.includes(index))return;
 memoryUser.push(index);
 const tiles=document.querySelectorAll("#memoryGrid button");
 if(memoryPattern.includes(index)){
  tiles[index].textContent="✓";tiles[index].style.background="#00b86b";tiles[index].style.color="#001018";
  if(memoryUser.length===memoryPattern.length){memoryLocked=true;document.getElementById("memoryResult").textContent="🎉 Perfect memory! You won!";}
 }else{
  tiles[index].textContent="✕";tiles[index].style.background="#d62828";memoryLocked=true;
  document.getElementById("memoryResult").textContent="Game over! Try again.";
 }
}

// SNAKE
const snakeCanvas=document.getElementById("snakeCanvas");
const snakeCtx=snakeCanvas.getContext("2d");
const snakeCell=15;
let snake=[],snakeFood={},snakeDirection={x:1,y:0},snakeNextDirection={x:1,y:0},snakePoints=0,snakeTimer=null,snakeOver=false;

function startSnake(){
 clearInterval(snakeTimer);
 snake=[{x:10,y:10},{x:9,y:10},{x:8,y:10}];
 snakeDirection={x:1,y:0};snakeNextDirection={x:1,y:0};snakePoints=0;snakeOver=false;
 placeSnakeFood();drawSnake();
 document.getElementById("snakeScore").textContent="Score: 0";
 snakeTimer=setInterval(moveSnake,120);
}
function placeSnakeFood(){
 const max=snakeCanvas.width/snakeCell;
 do{snakeFood={x:Math.floor(Math.random()*max),y:Math.floor(Math.random()*max)};}
 while(snake.some(p=>p.x===snakeFood.x&&p.y===snakeFood.y));
}
function setSnakeDirection(x,y){
 if(x===-snakeDirection.x&&y===-snakeDirection.y)return;
 snakeNextDirection={x,y};
}
function moveSnake(){
 if(snakeOver)return;
 snakeDirection=snakeNextDirection;
 const head={x:snake[0].x+snakeDirection.x,y:snake[0].y+snakeDirection.y};
 const max=snakeCanvas.width/snakeCell;
 if(head.x<0||head.y<0||head.x>=max||head.y>=max||snake.some(p=>p.x===head.x&&p.y===head.y)){
  snakeOver=true;clearInterval(snakeTimer);drawSnake();
  document.getElementById("snakeScore").textContent="Game Over! Score: "+snakePoints;return;
 }
 snake.unshift(head);
 if(head.x===snakeFood.x&&head.y===snakeFood.y){snakePoints++;placeSnakeFood();document.getElementById("snakeScore").textContent="Score: "+snakePoints;}
 else snake.pop();
 drawSnake();
}
function drawSnake(){
 snakeCtx.fillStyle="#02060c";snakeCtx.fillRect(0,0,snakeCanvas.width,snakeCanvas.height);
 snakeCtx.fillStyle="#ff476f";snakeCtx.fillRect(snakeFood.x*snakeCell,snakeFood.y*snakeCell,snakeCell-2,snakeCell-2);
 snake.forEach((p,i)=>{snakeCtx.fillStyle=i===0?"#00eaff":"#00a8cc";snakeCtx.fillRect(p.x*snakeCell,p.y*snakeCell,snakeCell-2,snakeCell-2);});
 if(snakeOver){snakeCtx.fillStyle="white";snakeCtx.font="bold 22px Arial";snakeCtx.textAlign="center";snakeCtx.fillText("GAME OVER",snakeCanvas.width/2,snakeCanvas.height/2);}
}
document.addEventListener("keydown",event=>{
 const keys={ArrowUp:[0,-1],ArrowDown:[0,1],ArrowLeft:[-1,0],ArrowRight:[1,0]};
 if(keys[event.key]&&document.activeElement.tagName!=="INPUT"&&document.activeElement.tagName!=="SELECT"){
  event.preventDefault();setSnakeDirection(...keys[event.key]);
 }
});
startSnake();

// RACING GAME (2D)
const raceCanvas=document.getElementById("raceCanvas");
const raceCtx=raceCanvas.getContext("2d");
let raceRunning=false,raceAnimation=null,racePlayerLane=1,raceTraffic=[],raceDistance=0,raceLastTime=0,raceSpawnTimer=0,raceRoadOffset=0,raceVehicle="bike",raceSpeed=.22;

const laneCenters=[180,300,420],roadLeft=110,roadRight=490;

function startRace(){
 if(raceAnimation)cancelAnimationFrame(raceAnimation);
 raceRunning=true;racePlayerLane=1;raceTraffic=[];raceDistance=0;raceSpawnTimer=0;raceRoadOffset=0;
 raceLastTime=performance.now();raceVehicle=document.getElementById("vehicleSelect").value;
 document.getElementById("raceStatus").textContent="🏁 Race started! Avoid the traffic!";
 raceAnimation=requestAnimationFrame(raceLoop);
}
function stopRace(){
 raceRunning=false;
 if(raceAnimation)cancelAnimationFrame(raceAnimation);
 raceAnimation=null;drawRaceScene();
 document.getElementById("raceStatus").textContent="Race stopped. Press START RACE to play again.";
}
function moveRacePlayer(direction){if(raceRunning)racePlayerLane=Math.max(0,Math.min(2,racePlayerLane+direction));}
document.getElementById("leftRace").addEventListener("pointerdown",e=>{e.preventDefault();moveRacePlayer(-1);});
document.getElementById("rightRace").addEventListener("pointerdown",e=>{e.preventDefault();moveRacePlayer(1);});

document.addEventListener("keydown",event=>{
 if(document.activeElement.tagName==="INPUT"||document.activeElement.tagName==="SELECT")return;
 if(event.key==="ArrowLeft"&&raceRunning){event.preventDefault();moveRacePlayer(-1);}
 if(event.key==="ArrowRight"&&raceRunning){event.preventDefault();moveRacePlayer(1);}
});

function drawRoad(){
 const w=raceCanvas.width,h=raceCanvas.height;
 raceCtx.fillStyle="#07110f";raceCtx.fillRect(0,0,w,h);
 raceCtx.fillStyle="#10281c";raceCtx.fillRect(0,0,roadLeft,h);raceCtx.fillRect(roadRight,0,w-roadRight,h);
 raceCtx.fillStyle="#202530";raceCtx.fillRect(roadLeft,0,roadRight-roadLeft,h);
 raceCtx.strokeStyle="#00eaff";raceCtx.lineWidth=4;raceCtx.beginPath();
 raceCtx.moveTo(roadLeft,0);raceCtx.lineTo(roadLeft,h);raceCtx.moveTo(roadRight,0);raceCtx.lineTo(roadRight,h);raceCtx.stroke();
 raceCtx.strokeStyle="#c6d0e2";raceCtx.lineWidth=3;raceCtx.setLineDash([32,28]);raceCtx.lineDashOffset=-raceRoadOffset;
 raceCtx.beginPath();raceCtx.moveTo(240,0);raceCtx.lineTo(240,h);raceCtx.moveTo(360,0);raceCtx.lineTo(360,h);raceCtx.stroke();raceCtx.setLineDash([]);
 raceCtx.fillStyle="#ff416c";
 for(let y=-50;y<h+50;y+=100){const yy=(y+raceRoadOffset)%(h+100);raceCtx.fillRect(roadLeft-10,yy,8,35);raceCtx.fillRect(roadRight+2,yy,8,35);}
}
function drawVehicle(x,y,type,color){
 raceCtx.save();raceCtx.translate(x,y);
 if(type==="bike"){
  raceCtx.fillStyle="#050505";raceCtx.fillRect(-10,-28,20,18);raceCtx.fillRect(-10,12,20,18);
  raceCtx.fillStyle=color;raceCtx.beginPath();raceCtx.moveTo(0,-34);raceCtx.lineTo(12,-8);raceCtx.lineTo(8,24);raceCtx.lineTo(-8,24);raceCtx.lineTo(-12,-8);raceCtx.closePath();raceCtx.fill();
  raceCtx.fillStyle="#e8faff";raceCtx.fillRect(-5,-19,10,8);
 }else{
  raceCtx.fillStyle="#050505";raceCtx.fillRect(-22,-30,44,66);
  raceCtx.fillStyle=color;raceCtx.fillRect(-19,-32,38,64);
  raceCtx.fillStyle="#0b2236";raceCtx.f
