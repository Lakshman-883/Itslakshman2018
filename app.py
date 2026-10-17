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
canvas{display:block;max-width:100%;height:auto;margin:15px auto;border:1px solid var(--blue);background:#02060c}
#memory{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;max-width:320px;margin:15px auto}
.tile{height:48px;background:#101a35;color:var(--blue);border:1px solid var(--blue);border-radius:6px;font-size:20px}
.terminal{background:#02050b;border:1px solid #00eaff66;padding:15px;border-radius:10px;font-family:monospace}
#out{height:180px;overflow:auto;white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.6}
.row{display:flex;gap:8px;align-items:center}
.row input{flex:1;min-width:0}
footer{text-align:center;padding:25px;border-top:1px solid #00eaff33;color:#9eacc7}
@media(max-width:600px){header{justify-content:center}nav{justify-content:center}section{padding:35px 5%}}
</style>
</head>
<body>

<header>
<a class="logo" href="#home">LAKSHMAN_2018</a>
<nav>
<a href="#home">HOME</a>
<a href="#about">ABOUT</a>
<a href="#projects">PROJECTS</a>
<a href="#games">GAMING</a>
<a href="#race">RACING</a>
<a href="#terminal">TERMINAL</a>
<a href="#contact">CONTACT</a>
</nav>
</header>

<section id="home" class="hero">
<div>
<p>WELCOME TO MY DIGITAL WORLD</p>
<h1>ITS LAKSHMAN</h1>
<p>Creator | Gamer | Digital Explorer<br>Welcome to my futuristic neon universe.</p>
<a class="btn" href="#projects">EXPLORE PROJECTS</a>
<a class="btn alt" href="#games">PLAY GAMES</a>
</div>
</section>

<section id="about">
<h2 class="heading">ABOUT ME</h2>
<div class="card">
<h3>Who Am I?</h3>
<p>Welcome to ItsLakshman2018 — a digital space for creativity, gaming and web projects.</p>
</div>
</section>

<section id="projects">
<h2 class="heading">MY PROJECTS</h2>
<div class="grid">
<div class="card"><h3>🌐 Portfolio</h3><p>Futuristic personal website.</p></div>
<div class="card"><h3>🎮 Gaming Zone</h3><p>Five browser mini-games.</p></div>
<div class="card"><h3>🏎️ Racing Arena</h3><p>Choose a vehicle and avoid traffic.</p></div>
<div class="card"><h3>💻 Digital Terminal</h3><p>Try the available demo commands.</p></div>
</div>
</section>

<section id="games">
<h2 class="heading">🎮 GAMING ZONE</h2>
<div class="grid">

<div class="card">
<h3>🔢 Number Guess</h3>
<p>Guess the number from 1 to 100.</p>
<input id="guess" type="number" min="1" max="100" placeholder="Enter number">
<button class="btn" onclick="guessGame()">GUESS</button>
<button class="btn alt" onclick="resetGuess()">RESET</button>
<div id="guessOut" class="result"></div>
</div>

<div class="card">
<h3>✊ Rock Paper Scissors</h3>
<button class="btn" onclick="rps('Rock')">✊ Rock</button>
<button class="btn" onclick="rps('Paper')">✋ Paper</button>
<button class="btn" onclick="rps('Scissors')">✌️ Scissors</button>
<div id="rpsOut" class="result"></div>
</div>

<div class="card">
<h3>⚡ Reflex Test</h3>
<p>Click after the button turns green.</p>
<button id="reflex" class="btn" onclick="reflexGame()">START TEST</button>
<div id="reflexOut" class="result"></div>
</div>

<div class="card">
<h3>🧠 Memory Matrix</h3>
<p>Remember the highlighted tiles.</p>
<button class="btn" onclick="memoryStart()">START</button>
<div id="memory"></div>
<div id="memoryOut" class="result"></div>
</div>

<div class="card">
<h3>🐍 Snake Game</h3>
<p>Use arrow keys or touch controls.</p>
<canvas id="snake" width="300" height="300"></canvas>
<div style="text-align:center">
<button class="btn" onclick="snakeDir(0,-1)">⬆️</button><br>
<button class="btn" onclick="snakeDir(-1,0)">⬅️</button>
<button class="btn" onclick="snakeDir(0,1)">⬇️</button>
<button class="btn" onclick="snakeDir(1,0)">➡️</button><br>
<button class="btn alt" onclick="snakeStart()">RESTART</button>
</div>
<div id="snakeOut" class="result">Score: 0</div>
</div>

</div>
</section>

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
<canvas id="road" width="300" height="440"></canvas>
<div style="text-align:center">
<button class="btn" onclick="raceMove(-1)">⬅️ LEFT</button>
<button class="btn" onclick="raceMove(1)">RIGHT ➡️</button>
</div>
<div id="raceOut" class="result">Choose a vehicle and start.</div>
<p>Desktop: use arrow keys. Mobile: use the buttons.</p>
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
<p style="color:#9eacc7">This is a demo terminal. It cannot execute real operating-system commands or access private device information.</p>
</section>

<section id="contact">
<h2 class="heading">CONTACT ME</h2>
<div class="card" style="text-align:center">
<h3>Let's Connect</h3>
<p>Follow my social media for updates and new projects.</p>
<a class="btn" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">INSTAGRAM</a>
</div>
</section>

<footer>© <span id="year"></span> ItsLakshman2018 | Digital World ⚡</footer>

<script>
const $=id=>document.getElementById(id);
$("year").textContent=new Date().getFullYear();

// Matrix background
const bg=document.createElement("canvas");
bg.style.cssText="position:fixed;inset:0;width:100%;height:100%;z-index:-1;opacity:.12;pointer-events:none";
document.body.prepend(bg);
const bx=bg.getContext("2d");
let drops=[];

function resizeBg(){
 bg.width=innerWidth;
 bg.height=innerHeight;
 drops=Array(Math.ceil(bg.width/15)).fill(0);
}
window.addEventListener("resize",resizeBg);
resizeBg();

setInterval(()=>{
 bx.fillStyle="rgba(5,8,22,.18)";
 bx.fillRect(0,0,bg.width,bg.height);
 bx.fillStyle="#00eaff";
 bx.font="15px monospace";
 drops.forEach((y,i)=>{
  bx.fillText("01LAKSHMAN"[Math.random()*10|0],i*15,y*15);
  drops[i]=y*15>bg.height&&Math.random()>.97?0:y+1;
 });
},60);

// Number Guess
let secret=Math.floor(Math.random()*100)+1;
let attempts=0;

function guessGame(){
 const v=Number($("guess").value);
 if(!$("guess").value||v<1||v>100){
  $("guessOut").textContent="Enter a number from 1 to 100.";
  return;
 }
 attempts++;
 $("guessOut").textContent=v===secret
  ?"🎉 Correct! Attempts: "+attempts
  :v<secret?"Too low! Try higher.":"Too high! Try lower.";
}

function resetGuess(){
 secret=Math.floor(Math.random()*100)+1;
 attempts=0;
 $("guess").value="";
 $("guessOut").textContent="New number generated!";
}

// Rock Paper Scissors
function rps(p){
 const a=["Rock","Paper","Scissors"];
 const c=a[Math.floor(Math.random()*3)];
 const win=(p==="Rock"&&c==="Scissors")||
 (p==="Paper"&&c==="Rock")||
 (p==="Scissors"&&c==="Paper");
 const result=p===c?"Draw!":win?"You win!":"Computer wins!";
 $("rpsOut").textContent="You: "+p+" | Computer: "+c+" | "+result;
}

// Reflex test
let state=0,reflexTimer=null,reflexTime=0;

function reflexGame(){
 if(state===0){
  state=1;
  $("reflex").textContent="WAIT...";
  $("reflex").style.background="#d62828";
  $("reflexOut").textContent="Wait for green!";

  reflexTimer=setTimeout(()=>{
   state=2;
   reflexTime=performance.now();
   $("reflex").textContent="CLICK NOW!";
   $("reflex").style.background="#00d26a";
  },1500+Math.random()*2500);

 }else if(state===1){
  clearTimeout(reflexTimer);
  state=0;
  $("reflexOut").textContent="Too early! Try again.";
  $("reflex").textContent="START TEST";
  $("reflex").style.background="";

 }else{
  const ms=Math.round(performance.now()-reflexTime);
  state=0;
  $("reflexOut").textContent="Reaction time: "+ms+" ms";
  $("reflex").textContent="START TEST";
  $("reflex").style.background="";
 }
}

// Memory Matrix
let memorySequence=[],memoryPick=[],memoryActive=false;

function memoryStart(){
 const box=$("memory");
 box.innerHTML="";
 memorySequence=[];
 memoryPick=[];
 memoryActive=false;

 for(let i=0;i<16;i++){
  const b=document.createElement("button");
  b.className="tile";
  b.textContent="";
  b.onclick=()=>memoryChoose(i,b);
  box.appendChild(b);
 }

 while(memorySequence.length<4){
  const n=Math.floor(Math.random()*16);
  if(!memorySequence.includes(n))memorySequence.push(n);
 }

 memorySequence.forEach(n=>{
  box.children[n].style.background="#00eaff";
 });

 $("memoryOut").textContent="Remember the highlighted tiles!";

 setTimeout(()=>{
  memorySequence.forEach(n=>{
   box.children[n].style.background="#101a35";
  });
  memoryActive=true;
  $("memoryOut").textContent="Tap the four tiles.";
 },1100);
}

function memoryChoose(n,b){
 if(!memoryActive||memoryPick.includes(n))return;

 memoryPick.push(n);

 if(memorySequence.includes(n)){
  b.style.background="#00a86b";
  b.textContent="✓";
 }else{
  b.style.background="#b51e35";
  b.textContent="×";
 }

 if(memoryPick.length===4){
  memoryActive=false;
  const score=memoryPick.filter(n=>memorySequence.includes(n)).length;
  $("memoryOut").textContent=score===4
   ?"🎉 Perfect memory!"
   :"Score: "+score+"/4. Try again!";
 }
}

// Snake game
const snakeCanvas=$("snake");
const sx=snakeCanvas.getContext("2d");
const cell=15,board=20;

let snake=[],food={x:10,y:10},dir={x:1,y:0};
let snakeTimer=null,snakeScore=0,snakeAlive=false;

function snakeStart(){
 clearInterval(snakeTimer);
 snake=[{x:5,y:10},{x:4,y:10},{x:3,y:10}];
 dir={x:1,y:0};
 food={x:12,y:10};
 snakeScore=0;
 snakeAlive=true;
 $("snakeOut").textContent="Score: 0";
 drawSnake();
 snakeTimer=setInterval(snakeTick,130);
}

function snakeDir(x,y){
 if(x===-dir.x&&y===-dir.y)return;
 dir={x,y};
}

function snakeTick(){
 if(!snakeAlive)return;

 const head={x:snake[0].x+dir.x,y:snake[0].y+dir.y};

 if(head.x<0||head.y<0||head.x>=board||head.y>=board||
 snake.some(s=>s.x===head.x&&s.y===head.y)){
  snakeAlive=false;
  clearInterval(snakeTimer);
  $("snakeOut").textContent="Game over! Score: "+snakeScore+". Press RESTART.";
  return;
 }

 snake.unshift(head);

 if(head.x===food.x&&head.y===food.y){
  snakeScore++;
  food={x:Math.floor(Math.random()*board),y:Math.floor(Math.random()*board)};
  $("snakeOut").textContent="Score: "+snakeScore;
 }else{
  snake.pop();
 }

 drawSnake();
}

function drawSnake(){
 sx.fillStyle="#02060c";
 sx.fillRect(0,0,300,300);
 sx.fillStyle="#ff477e";
 sx.fillRect(food.x*cell,food.y*cell,cell-1,cell-1);
 sx.fillStyle="#00eaff";
 snake.forEach(s=>sx.fillRect(s.x*cell,s.y*cell,cell-1,cell-1));
}

// Racing game
const road=$("road");
const rx=road.getContext("2d");

let playerLane=1,obstacles=[],raceRunning=false;
let raceTimer=null,raceScore=0;

function raceStart(){
 raceStop();
 playerLane=1;
 obstacles=[];
 raceScore=0;
 raceRunning=true;
 $("raceOut").textContent="Race started! Avoid traffic.";
 raceTimer=setInterval(raceTick,100);
}

function raceStop(){
 raceRunning=false;
 clearInterval(raceTimer);
 raceTimer=null;
 drawRoad();
}

function raceMove(d){
 playerLane=Math.max(0,Math.min(2,playerLane+d));
 drawRoad();
}

function raceTick(){
 if(!raceRunning)return;

 if(Math.random()<0.035){
  obstacles.push({lane:Math.floor(Math.random()*3),y:-45});
 }

 obstacles.forEach(o=>o.y+=5);
 obstacles=obstacles.filter(o=>o.y<450);

 const py=365;

 if(obstacles.some(o=>o.lane===playerLane&&o.y>py-35&&o.y<py+35)){
  raceRunning=false;
  clearInterval(raceTimer);
  $("raceOut").textContent="Crash! Score: "+raceScore+". Restart to try again.";
 }

 raceScore++;

 if(raceRunning){
  $("raceOut").textContent="Distance: "+raceScore;
 }

 drawRoad();
}

function drawRoad(){
 rx.fillStyle="#111820";
 rx.fillRect(0,0,300,440);
 rx.fillStyle="#273340";
 rx.fillRect(25,0,250,440);

 rx.strokeStyle="#f7f7f7";
 rx.setLineDash([22,18]);
 rx.lineWidth=3;
 rx.beginPath();
 rx.moveTo(108,0);
 rx.lineTo(108,440);
 rx.moveTo(192,0);
 rx.lineTo(192,440);
 rx.stroke();
 rx.setLineDash([]);

 const px=66+playerLane*84;

 rx.fillStyle=$("vehicle").value==="bike"?"#00eaff":"#ffb703";
 rx.fillRect(px-13,365,26,42);

 rx.fillStyle="#ff304f";
 obstacles.forEach(o=>{
  rx.fillRect(66+o.lane*84-15,o.y,30,40);
 });
}

drawRoad();

// Keyboard controls
document.addEventListener("keydown",e=>{
 if(e.key==="ArrowLeft"){
  if(raceRunning)raceMove(-1);
  else snakeDir(-1,0);
 }
 if(e.key==="ArrowRight"){
  if(raceRunning)raceMove(1);
  else snakeDir(1,0);
 }
 if(e.key==="ArrowUp")snakeDir(0,-1);
 if(e.key==="ArrowDown")snakeDir(0,1);
 if(e.key==="Enter"&&document.activeElement===$("cmd"))command();
});

// Demo terminal
function command(){
 const input=$("cmd");
 const c=input.value.trim().toLowerCase();
 const out=$("out");

 if(!c)return;

 if(c==="clear"){
  out.textContent="";
  input.value="";
  return;
 }

 const responses={
  help:"Available commands: help, about, games, racing, date, browser, device, network, clear",
  about:"ItsLakshman2018 - Creator | Gamer | Digital Explorer",
  games:"Number Guess, Rock Paper Scissors, Reflex Test, Memory Matrix, Snake",
  racing:"Choose a vehicle and start the Neon Racing Arena.",
  date:new Date().toString(),
  browser:"Browser: "+navigator.userAgent,
  device:"Screen: "+screen.width+" x "+screen.height,
  network:"Online status: "+(navigator.onLine?"Online":"Offline")
 };

 out.textContent+="\n> "+c+"\n"+(responses[c]||"Unknown command. Type help.");
 out.scrollTop=out.scrollHeight;
 input.value="";
}
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
