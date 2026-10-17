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
.game3d{width:100%;height:260px;border:1px solid #00eaff88;border-radius:12px;overflow:hidden;background:radial-gradient(ellipse at 50% 0%,#172b52 0%,#02060c 72%);margin:12px 0;box-shadow:0 0 18px #00eaff18,inset 0 0 22px #00eaff12}
.game3d canvas{filter:saturate(1.18) contrast(1.04)}
.card{backdrop-filter:blur(8px)}
.game3d canvas{width:100%;height:100%;margin:0;border:0;display:block}
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
<a href="#home">HOME</a><a href="#about">ABOUT</a>
<a href="#projects">PROJECTS</a><a href="#games">GAMING</a>
<a href="#race">RACING</a><a href="#3dgames">3D GAMES</a>
<a href="#terminal">TERMINAL</a><a href="#contact">CONTACT</a>
</nav>
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
<canvas id="snake" width="300" height="300"></canvas>
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
<canvas id="road" width="300" height="440"></canvas>
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
<button class="btn" onclick="driveStart()">START / RESTART</button>
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

<section id="contact">
<h2 class="heading">CONTACT ME</h2><div class="card" style="text-align:center">
<h3>Let's Connect</h3><p>Follow my social media for updates.</p>
<a class="btn" href="https://www.instagram.com/" target="_blank" rel="noopener noreferrer">INSTAGRAM</a>
</div></section>

<footer>© <span id="year"></span> ItsLakshman2018 | Digital World ⚡</footer>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
const $=id=>document.getElementById(id);
$("year").textContent=new Date().getFullYear();

// Matrix background
const bg=document.createElement("canvas");
bg.style.cssText="position:fixed;inset:0;width:100%;height:100%;z-index:-1;opacity:.12;pointer-events:none";
document.body.prepend(bg);
const bx=bg.getContext("2d");let drops=[];
function resizeBg(){bg.width=innerWidth;bg.height=innerHeight;drops=Array(Math.ceil(bg.width/15)).fill(0)}
window.addEventListener("resize",resizeBg);resizeBg();
setInterval(()=>{
 bx.fillStyle="rgba(5,8,22,.18)";bx.fillRect(0,0,bg.width,bg.height);
 bx.fillStyle="#00eaff";bx.font="15px monospace";
 drops.forEach((y,i)=>{bx.fillText("01LAKSHMAN"[Math.random()*10|0],i*15,y*15);drops[i]=y*15>bg.height&&Math.random()>.97?0:y+1});
},60);

// Number Guess
let secret=Math.floor(Math.random()*100)+1,attempts=0;
function guessGame(){
 const v=Number($("guess").value);
 if(!$("guess").value||v<1||v>100){$("guessOut").textContent="Enter a number from 1 to 100.";return}
 attempts++;
 $("guessOut").textContent=v===secret?"🎉 Correct! Attempts: "+attempts:v<secret?"Too low! Try higher.":"Too high! Try lower.";
}
function resetGuess(){secret=Math.floor(Math.random()*100)+1;attempts=0;$("guess").value="";$("guessOut").textContent="New number generated!"}

// Rock Paper Scissors
function rps(p){
 const a=["Rock","Paper","Scissors"],c=a[Math.floor(Math.random()*3)];
 const win=(p==="Rock"&&c==="Scissors")||(p==="Paper"&&c==="Rock")||(p==="Scissors"&&c==="Paper");
 $("rpsOut").textContent="You: "+p+" | Computer: "+c+" | "+(p===c?"Draw!":win?"You win!":"Computer wins!");
}

// Reflex Test
let state=0,reflexTimer=null,reflexTime=0;
function reflexGame(){
 if(state===0){
  state=1;$("reflex").textContent="WAIT...";$("reflex").style.background="#d62828";$("reflexOut").textContent="Wait for green!";
  reflexTimer=setTimeout(()=>{state=2;reflexTime=performance.now();$("reflex").textContent="CLICK NOW!";$("reflex").style.background="#00d26a"},1500+Math.random()*2500);
 }else if(state===1){
  clearTimeout(reflexTimer);state=0;$("reflexOut").textContent="Too early! Try again.";$("reflex").textContent="START TEST";$("reflex").style.background="";
 }else{
  $("reflexOut").textContent="Reaction time: "+Math.round(performance.now()-reflexTime)+" ms";
  state=0;$("reflex").textContent="START TEST";$("reflex").style.background="";
 }
}

// Memory Matrix
let memorySequence=[],memoryPick=[],memoryActive=false;
function memoryStart(){
 const box=$("memory");box.innerHTML="";memorySequence=[];memoryPick=[];memoryActive=false;
 for(let i=0;i<16;i++){const b=document.createElement("button");b.className="tile";b.onclick=()=>memoryChoose(i,b);box.appendChild(b)}
 while(memorySequence.length<4){const n=Math.floor(Math.random()*16);if(!memorySequence.includes(n))memorySequence.push(n)}
 memorySequence.forEach(n=>box.children[n].style.background="#00eaff");
 $("memoryOut").textContent="Remember the highlighted tiles!";
 setTimeout(()=>{memorySequence.forEach(n=>box.children[n].style.background="#101a35");memoryActive=true;$("memoryOut").textContent="Tap the four tiles."},1100);
}
function memoryChoose(n,b){
 if(!memoryActive||memoryPick.includes(n))return;
 memoryPick.push(n);
 if(memorySequence.includes(n)){b.style.background="#00a86b";b.textContent="✓"}else{b.style.background="#b51e35";b.textContent="×"}
 if(memoryPick.length===4){memoryActive=false;const score=memoryPick.filter(n=>memorySequence.includes(n)).length;$("memoryOut").textContent=score===4?"🎉 Perfect memory!":"Score: "+score+"/4. Try again!"}
}

// Snake Game
const snakeCanvas=$("snake"),sx=snakeCanvas.getContext("2d"),cell=15,board=20;
let snake=[],food={x:10,y:10},dir={x:1,y:0},snakeTimer=null,snakeScore=0,snakeAlive=false;
function snakeStart(){
 clearInterval(snakeTimer);snake=[{x:5,y:10},{x:4,y:10},{x:3,y:10}];dir={x:1,y:0};food={x:12,y:10};snakeScore=0;snakeAlive=true;$("snakeOut").textContent="Score: 0";drawSnake();snakeTimer=setInterval(snakeTick,130);
}
function snakeDir(x,y){if(x===-dir.x&&y===-dir.y)return;dir={x,y}}
function snakeTick(){
 if(!snakeAlive)return;
 const head={x:snake[0].x+dir.x,y:snake[0].y+dir.y};
 if(head.x<0||head.y<0||head.x>=board||head.y>=board||snake.some(s=>s.x===head.x&&s.y===head.y)){
  snakeAlive=false;clearInterval(snakeTimer);$("snakeOut").textContent="Game over! Score: "+snakeScore+". Press RESTART.";return;
 }
 snake.unshift(head);
 if(head.x===food.x&&head.y===food.y){snakeScore++;food={x:Math.floor(Math.random()*board),y:Math.floor(Math.random()*board)};$("snakeOut").textContent="Score: "+snakeScore}else snake.pop();
 drawSnake();
}
function drawSnake(){
 sx.fillStyle="#02060c";sx.fillRect(0,0,300,300);sx.fillStyle="#ff477e";sx.fillRect(food.x*cell,food.y*cell,cell-1,cell-1);sx.fillStyle="#00eaff";snake.forEach(s=>sx.fillRect(s.x*cell,s.y*cell,cell-1,cell-1));
}

// Racing Game
const road=$("road"),rx=road.getContext("2d");
let playerLane=1,obstacles=[],raceRunning=false,raceTimer=null,raceScore=0;
function raceStart(){raceStop();playerLane=1;obstacles=[];raceScore=0;raceRunning=true;$("raceOut").textContent="Race started! Avoid traffic.";raceTimer=setInterval(raceTick,100)}
function raceStop(){raceRunning=false;clearInterval(raceTimer);raceTimer=null;drawRoad()}
function raceMove(d){playerLane=Math.max(0,Math.min(2,playerLane+d));drawRoad()}
function raceTick(){
 if(!raceRunning)return;
 if(Math.random()<.035)obstacles.push({lane:Math.floor(Math.random()*3),y:-45});
 obstacles.forEach(o=>o.y+=5);obstacles=obstacles.filter(o=>o.y<450);
 const py=365;
 if(obstacles.some(o=>o.lane===playerLane&&o.y>py-35&&o.y<py+35)){raceRunning=false;clearInterval(raceTimer);$("raceOut").textContent="Crash! Score: "+raceScore+". Restart to try again."}
 if(raceRunning){raceScore++;$("raceOut").textContent="Distance: "+raceScore}
 drawRoad();
}
function drawRoad(){
 rx.fillStyle="#111820";rx.fillRect(0,0,300,440);rx.fillStyle="#273340";rx.fillRect(25,0,250,440);
 rx.strokeStyle="#f7f7f7";rx.setLineDash([22,18]);rx.lineWidth=3;rx.beginPath();rx.moveTo(108,0);rx.lineTo(108,440);rx.moveTo(192,0);rx.lineTo(192,440);rx.stroke();rx.setLineDash([]);
 const px=66+playerLane*84;rx.fillStyle=$("vehicle").value==="bike"?"#00eaff":"#ffb703";rx.fillRect(px-13,365,26,42);
 rx.fillStyle="#ff304f";obstacles.forEach(o=>rx.fillRect(66+o.lane*84-15,o.y,30,40));
}
drawRoad();

// Keyboard controls
document.addEventListener("keydown",e=>{
 if(e.key==="ArrowLeft"){if(raceRunning)raceMove(-1);else snakeDir(-1,0)}
 if(e.key==="ArrowRight"){if(raceRunning)raceMove(1);else snakeDir(1,0)}
 if(e.key==="ArrowUp")snakeDir(0,-1);
 if(e.key==="ArrowDown")snakeDir(0,1);
 if(e.key==="Enter"&&document.activeElement===$("cmd"))command();
});

// 3D game setup
const scenes3d={};
function makeWorld(id,bgColor=0x020817){
 const host=$(id);
 if(!host||!window.THREE){if(host)host.textContent="3D library failed to load. Check internet.";return null}
 const scene=new THREE.Scene();scene.background=new THREE.Color(bgColor);
 const camera=new THREE.PerspectiveCamera(65,(host.clientWidth||300)/(host.clientHeight||210),.1,100);
 camera.position.set(0,4,8);camera.lookAt(0,0,0);
 const renderer=new THREE.WebGLRenderer({antialias:true});
 renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
 renderer.setSize(host.clientWidth||300,host.clientHeight||210);
 host.replaceChildren(renderer.domElement);
 scene.add(new THREE.HemisphereLight(0x9beeff,0x202040,2));
 const light=new THREE.DirectionalLight(0xffffff,2);light.position.set(3,8,5);scene.add(light);
 const world={host,scene,camera,renderer};scenes3d[id]=world;
 const resize=()=>{const w=host.clientWidth||300,h=host.clientHeight||210;camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h,false)};
 if(window.ResizeObserver)new ResizeObserver(resize).observe(host);
 window.addEventListener("resize",resize);
 return world;
}
function cube(scene,color,x,y,z,sx=1,sy=1,sz=1){
 const m=new THREE.Mesh(new THREE.BoxGeometry(sx,sy,sz),new THREE.MeshStandardMaterial({color,roughness:.35,metalness:.3}));
 m.position.set(x,y,z);scene.add(m);return m;
}

function sphere(scene,color,x,y,z,r=0.3,detail=16){
 const m=new THREE.Mesh(new THREE.SphereGeometry(r,detail,detail),new THREE.MeshStandardMaterial({color,roughness:.32,metalness:.18}));
 m.position.set(x,y,z);scene.add(m);return m;
}
function addRunnerHero(scene){
 const g=new THREE.Group();
 const mat=(color,roughness=.35)=>new THREE.MeshStandardMaterial({color,roughness,metalness:.15});
 const torso=new THREE.Mesh(new THREE.CapsuleGeometry(.22,.38,4,8),mat(0x00d9ff));torso.position.y=.75;g.add(torso);
 const head=new THREE.Mesh(new THREE.SphereGeometry(.19,16,12),mat(0xffc9a0));head.position.y=1.18;g.add(head);
 const visor=new THREE.Mesh(new THREE.BoxGeometry(.27,.07,.06),mat(0x10233f));visor.position.set(0,1.2,.16);g.add(visor);
 for(const x of [-.13,.13]){const leg=new THREE.Mesh(new THREE.BoxGeometry(.13,.38,.15),mat(0x304a7b));leg.position.set(x,.25,0);g.add(leg);
 const arm=new THREE.Mesh(new THREE.BoxGeometry(.11,.34,.12),mat(0x00a9cc));arm.position.set(x*2,.77,0);arm.rotation.z=x<0?-.25:.25;g.add(arm);}
 g.position.set(0,0,2);scene.add(g);return g;
}
function addSportsCar(scene,color,x,y,z){
 const g=new THREE.Group(), paint=new THREE.MeshStandardMaterial({color,metalness:.65,roughness:.23});
 function part(geo,mat,px,py,pz){const m=new THREE.Mesh(geo,mat);m.position.set(px,py,pz);g.add(m);return m;}
 part(new THREE.BoxGeometry(.95,.25,1.55),paint,0,.32,0);
 part(new THREE.BoxGeometry(.68,.27,.72),new THREE.MeshStandardMaterial({color:0x14283c,metalness:.4,roughness:.18}),0,.55,-.12);
 part(new THREE.BoxGeometry(.7,.05,.13),new THREE.MeshStandardMaterial({color:0xffffff,emissive:0x88ddff,emissiveIntensity:1.5}),0,.36,.79);
 for(const x of [-.49,.49])for(const z of [-.48,.48]){
  const wheel=part(new THREE.CylinderGeometry(.17,.17,.12,16),new THREE.MeshStandardMaterial({color:0x10131b,roughness:.8}),x,.18,z);wheel.rotation.z=Math.PI/2;
  part(new THREE.CylinderGeometry(.08,.08,.125,12),new THREE.MeshStandardMaterial({color:0x9cb5ca,metalness:.8}),x,.18,z).rotation.z=Math.PI/2;
 }
 g.position.set(x,y,z);scene.add(g);return g;
}
function addZombieModel(scene,x,z){
 const g=new THREE.Group(),skin=new THREE.MeshStandardMaterial({color:0x67b56b,roughness:.8}),cloth=new THREE.MeshStandardMaterial({color:0x394c42,roughness:1});
 function part(geo,mat,px,py,pz){const m=new THREE.Mesh(geo,mat);m.position.set(px,py,pz);g.add(m);return m;}
 part(new THREE.BoxGeometry(.48,.62,.3),cloth,0,.62,0);
 part(new THREE.SphereGeometry(.24,14,12),skin,0,1.12,0);
  for(const ex of [-.09,.09]){
  part(new THREE.SphereGeometry(.045,8,8),
   new THREE.MeshStandardMaterial({color:0xff3030}),
   ex,1.16,.2);
 }

 for(const x of [-.34,.34]){
  const arm=part(
   new THREE.BoxGeometry(.13,.45,.13),
   cloth,x,.7,0
  );
  arm.rotation.z=x<0?-.3:.3;

  for(const z of [-.13,.13]){
   part(new THREE.BoxGeometry(.14,.4,.15),
    cloth,x*.45,.23,z);
  }
 }

 g.position.set(x,0,z);
 scene.add(g);
 return g;
}

// Neon Runner 3D
const runnerWorld=makeWorld("runner3d",0x050b20);
let runnerHero=null,runnerBlocks=[],runnerLane=0,runnerLive=false,runnerScore=0;

if(runnerWorld){
 const s=runnerWorld.scene;
 const floor=cube(s,0x101a35,0,-.15,0,5,.2,18);
 runnerHero=addRunnerHero(s);
 runnerWorld.camera.position.set(0,3.5,7);
 runnerWorld.camera.lookAt(0,0,0);

 for(let i=0;i<18;i++){
  cube(s,i%2?0x00eaff:0x174c78,-2.2,-.02,-i,0.04,.03,.6);
  cube(s,i%2?0x00eaff:0x174c78,2.2,-.02,-i,0.04,.03,.6);
 }
}

function runnerStart(){
 if(!runnerWorld)return;
 runnerBlocks.forEach(b=>runnerWorld.scene.remove(b));
 runnerBlocks=[];
 runnerLane=0;
 runnerScore=0;
 runnerLive=true;
 runnerHero.position.x=0;
 $("runnerOut").textContent="Run! Avoid the blocks.";
 for(let i=0;i<5;i++){
  const b=cube(runnerWorld.scene,0xff3155,
   [-1.5,0,1.5][Math.floor(Math.random()*3)],
   .45,-8-i*5,.7,.9,.7);
  runnerBlocks.push(b);
 }
}

function runnerMove(d){
 if(!runnerLive)return;
 runnerLane=Math.max(-1,Math.min(1,runnerLane+d));
 runnerHero.position.x=runnerLane*1.5;
}

function runnerTick(){
 if(!runnerWorld)return;
 if(runnerLive){
  runnerScore++;
  runnerBlocks.forEach(b=>{
   b.position.z+=.12;
   if(b.position.z>2){
    b.position.z=-25-Math.random()*10;
    b.position.x=[-1.5,0,1.5][Math.floor(Math.random()*3)];
   }
   if(Math.abs(b.position.z-2)<.6&&
      Math.abs(b.position.x-runnerHero.position.x)<.65){
    runnerLive=false;
    $("runnerOut").textContent="Crash! Score: "+runnerScore;
   }
  });
 }
}

// Zombie Survival 3D
const zombieWorld=makeWorld("zombie3d",0x101408);
let zombies=[],zombieScore=0,zombiePlayer={x:0,z:2};

if(zombieWorld){
 const s=zombieWorld.scene;
 cube(s,0x253522,0,-.15,0,10,.2,10);
 zombieWorld.camera.position.set(0,5,8);
 zombieWorld.camera.lookAt(0,0,0);

 for(let i=0;i<6;i++){
  zombies.push(addZombieModel(s,
   (Math.random()-.5)*5,
   (Math.random()-.5)*4-1));
 }
 zombieWorld.renderer.domElement.addEventListener("click",e=>{
  const rect=e.target.getBoundingClientRect();
  const mouse=new THREE.Vector2(
   (e.clientX-rect.left)/rect.width*2-1,
   -(e.clientY-rect.top)/rect.height*2+1
  );
  const ray=new THREE.Raycaster();
  ray.setFromCamera(mouse,zombieWorld.camera);
  const hits=ray.intersectObjects(zombieWorld.scene.children,true);
  if(hits.length){
   let obj=hits[0].object;
   while(obj.parent&&!zombies.includes(obj))obj=obj.parent;
   if(zombies.includes(obj)){
    zombieWorld.scene.remove(obj);
    zombies=zombies.filter(z=>z!==obj);
    zombieScore++;
    $("zombieOut").textContent="Zombies tagged: "+zombieScore;
    const z=addZombieModel(zombieWorld.scene,
     (Math.random()-.5)*5,
     (Math.random()-.5)*4-1);
    zombies.push(z);
   }
  }
 });
}

function zombieMove(dx,dz){
 if(!zombieWorld)return;
 zombiePlayer.x=Math.max(-3,Math.min(3,zombiePlayer.x+dx));
 zombiePlayer.z=Math.max(-3,Math.min(3,zombiePlayer.z+dz));
 zombieWorld.camera.position.x=zombiePlayer.x;
 zombieWorld.camera.position.z=8+zombiePlayer.z;
 zombieWorld.camera.lookAt(zombiePlayer.x,0,0);
}

// 3D Drift Drive
const driveWorld=makeWorld("drive3d",0x07101d);
let driveCar=null,driveBlocks=[],driveRunning=false,driveDistance=0,driveLane=0;

if(driveWorld){
 const s=driveWorld.scene;
 cube(s,0x26313d,0,-.15,0,5,.2,18);
 driveCar=addSportsCar(s,0x00c8ff,0,0,2);
 driveWorld.camera.position.set(0,3.4,7);
 driveWorld.camera.lookAt(0,.3,0);

 for(let i=0;i<12;i++){
  cube(s,0xffffff,-2,-.02,-i, .06,.03,.5);
  cube(s,0xffffff,2,-.02,-i, .06,.03,.5);
 }
}

function driveStart(){
 if(!driveWorld)return;
 driveBlocks.forEach(b=>driveWorld.scene.remove(b));
 driveBlocks=[];
 driveDistance=0;
 driveLane=0;
 driveRunning=true;
 driveCar.position.x=0;
 $("driveOut").textContent="Drive started!";
 for(let i=0;i<5;i++){
  driveBlocks.push(cube(driveWorld.scene,0xff3355,
   [-1.3,0,1.3][Math.floor(Math.random()*3)],
   .4,-8-i*5,.8,.8,.8));
 }
}

function driveMove(d){
 if(!driveRunning)return;
 driveLane=Math.max(-1,Math.min(1,driveLane+d));
 driveCar.position.x=driveLane*1.3;
}

function driveTick(){
 if(!driveWorld||!driveRunning)return;
 driveDistance++;
 driveBlocks.forEach(b=>{
  b.position.z+=.13;
  if(b.position.z>2){
   b.position.z=-25-Math.random()*10;
   b.position.x=[-1.3,0,1.3][Math.floor(Math.random()*3)];
  }
  if(Math.abs(b.position.z-driveCar.position.z)<.8&&
     Math.abs(b.position.x-driveCar.position.x)<.8){
   driveRunning=false;
   $("driveOut").textContent="Crash! Distance: "+driveDistance+
    ". Press START / RESTART.";
  }
 });
 if(driveRunning)$("driveOut").textContent="Distance: "+driveDistance;
}

// Space Blaster 3D
const spaceWorld=makeWorld("space3d",0x020414);
let spaceShip=null,spaceTargets=[],spaceShots=[],spaceScore=0,spaceLane=0;

if(spaceWorld){
 const s=spaceWorld.scene;
 spaceWorld.camera.position.set(0,4,8);
 spaceWorld.camera.lookAt(0,0,0);

 spaceShip=new THREE.Group();
 const body=new THREE.Mesh(
  new THREE.ConeGeometry(.35,.9,5),
  new THREE.MeshStandardMaterial({
   color:0x00eaff,metalness:.6,roughness:.2,
   emissive:0x003344
  })
 );
 body.rotation.x=-Math.PI/2;
 spaceShip.add(body);
 spaceShip.position.set(0,0,2);
 s.add(spaceShip);

 for(let i=0;i<20;i++){
  sphere(s,0xffffff,(Math.random()-.5)*9,
   Math.random()*5-1,-Math.random()*20,.035,6);
 }
 for(let i=0;i<5;i++){
  spaceTargets.push(sphere(s,0xff3155,
   (Math.random()-.5)*5,0,-4-i*4,.35,12));
 }
}

function spaceMove(d){
 if(!spaceShip)return;
 spaceLane=Math.max(-2,Math.min(2,spaceLane+d));
 spaceShip.position.x=spaceLane;
}

function spaceShoot(){
 if(!spaceWorld||!spaceShip)return;
 const shot=cube(spaceWorld.scene,0x00eaff,
  spaceShip.position.x,0,1.4,.12,.12,.5);
 spaceShots.push(shot);
}

function spaceTick(){
 if(!spaceWorld)return;
 spaceShots.forEach(shot=>{
  shot.position.z-=.25;
  if(shot.position.z< -25){
   spaceWorld.scene.remove(shot);
  }
 });
 spaceShots=spaceShots.filter(s=>s.position.z>=-25);

 spaceTargets.forEach(target=>{
  target.position.z+=.035;
  if(target.position.z>4){
   target.position.z=-20-Math.random()*10;
   target.position.x=(Math.random()-.5)*4;
  }

  spaceShots.forEach(shot=>{
   if(shot.position.distanceTo(target.position)<.65){
    target.position.z=-20-Math.random()*10;
    spaceScore++;
    $("spaceOut").textContent="Targets hit: "+spaceScore;
    shot.position.z=-30;
   }
  });
 });
}

// Animation loop
function animate3D(){
 requestAnimationFrame(animate3D);
 const t=performance.now()*.001;

 if(runnerHero&&runnerLive){
  runnerHero.position.y=Math.abs(Math.sin(t*9))*.08;
 }
 if(runnerWorld){
  runnerBlocks.forEach(b=>{b.rotation.y+=.01});
  runnerWorld.renderer.render(runnerWorld.scene,runnerWorld.camera);
 }
 if(zombieWorld){
  zombies.forEach((z,i)=>{z.rotation.y=Math.sin(t+i)*.15});
  zombieWorld.renderer.render(zombieWorld.scene,zombieWorld.camera);
 }
 if(driveWorld){
  driveBlocks.forEach(b=>{b.rotation.y+=.01});
  driveWorld.renderer.render(driveWorld.scene,driveWorld.camera);
 }
 if(spaceWorld){
  spaceTargets.forEach((z,i)=>{z.rotation.y+=.02;z.rotation.x+=.01});
  spaceWorld.renderer.render(spaceWorld.scene,spaceWorld.camera);
 }
}
setInterval(runnerTick,50);
setInterval(driveTick,50);
setInterval(spaceTick,50);
animate3D();

// Terminal demo
function command(){
 const input=$("cmd"),out=$("out");
 const c=input.value.trim().toLowerCase();
 if(!c)return;
 const cmds={
  help:"Commands: help, about, games, racing, date, browser, device, network, clear",
  about:"ItsLakshman2018 — futuristic digital world.",
  games:"Available: Number Guess, RPS, Reflex, Memory, Snake.",
  racing:"Neon Racing Arena is ready.",
  date:new Date().toLocaleString(),
  browser:navigator.userAgent,
  device:"Screen: "+innerWidth+" x "+innerHeight,
  network:navigator.onLine?"Browser reports online.":"Browser reports offline."
 };
 if(c==="clear")out.textContent="";
 else out.textContent+="\n> "+c+"\n"+(cmds[c]||"Unknown command. Type help.");
 input.value="";
 out.scrollTop=out.scrollHeight;
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
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
