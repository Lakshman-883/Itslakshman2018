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
.game3d{width:100%;height:210px;border:1px solid #00eaff66;border-radius:8px;overflow:hidden;background:#02060c;margin:12px 0}
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

// 1. Neon Runner 3D
let runnerLane=0,runnerLive=false,runnerScore=0,runnerObs=[];
(function(){
 const w=makeWorld("runner3d");if(!w)return;
 w.camera.position.set(0,4,7);w.camera.lookAt(0,0,-3);
 cube(w.scene,0x15223d,0,-.25,-4,5,.3,18);
 for(let x=-1;x<=1;x++)cube(w.scene,0x00eaff,x*1.3,.01,-4,.035,.02,18);
 const player=cube(w.scene,0x00eaff,0,.45,2,.6,.8,.6);
 w.tick=()=>{
  player.position.x=runnerLane*1.3;
  runnerObs.forEach(o=>o.position.z+=.12);
  runnerObs=runnerObs.filter(o=>{
   if(o.position.z>4){w.scene.remove(o);return false}
   if(runnerLive&&Math.abs(o.position.z-2)<.55&&Math.abs(o.position.x-player.position.x)<.65){
    runnerLive=false;$("runnerOut").textContent="Crash! Score: "+runnerScore+". Restart to play.";
   }
   return true;
  });
  if(runnerLive){
   runnerScore++;$("runnerOut").textContent="Distance: "+runnerScore;
   if(Math.random()<.025)runnerObs.push(cube(w.scene,0xff3864,([-1,0,1][Math.random()*3|0])*1.3,.45,-10,.7,.8,.7));
  }
 };
})();
function runnerStart(){
 runnerLane=0;runnerLive=true;runnerScore=0;
 if(scenes3d.runner3d)runnerObs.forEach(o=>scenes3d.runner3d.scene.remove(o));
 runnerObs=[];$("runnerOut").textContent="Run! Dodge the blocks.";
}
function runnerMove(d){runnerLane=Math.max(-1,Math.min(1,runnerLane+d))}

// 2. Zombie Survival 3D
let zombieScore=0,zombies=[];
(function(){
 const w=makeWorld("zombie3d");if(!w)return;
 w.camera.position.set(0,5,8);w.camera.lookAt(0,0,0);
 cube(w.scene,0x18251f,0,-.3,0,10,.3,10);
 function addZombie(){
  const g=new THREE.Group();
  cube(g,0x4ba66b,0,.45,0,.5,.8,.35);
  cube(g,0x9ad46b,0,1.05,0,.42,.42,.42);
  g.position.set((Math.random()-.5)*5,0,(Math.random()-.5)*3);
  w.scene.add(g);zombies.push(g);
 }
 for(let i=0;i<5;i++)addZombie();
 w.renderer.domElement.addEventListener("click",e=>{
  const r=w.renderer.domElement.getBoundingClientRect();
  const mouse=new THREE.Vector2((e.clientX-r.left)/r.width*2-1,-(e.clientY-r.top)/r.height*2+1);
  const ray=new THREE.Raycaster();ray.setFromCamera(mouse,w.camera);
  const hits=ray.intersectObjects(zombies,true);
  if(!hits.length)return;
  let g=hits[0].object;
  while(g.parent&&g.parent!==w.scene)g=g.parent;
  w.scene.remove(g);zombies=zombies.filter(z=>z!==g);
  zombieScore++;$("zombieOut").textContent="Zombies tagged: "+zombieScore;
  while(zombies.length<5)addZombie();
 });
})();
function zombieMove(dx,dz){
 const w=scenes3d.zombie3d;if(!w)return;
 w.camera.position.x=Math.max(-3,Math.min(3,w.camera.position.x+dx*.4));
 w.camera.position.z=Math.max(5,Math.min(10,w.camera.position.z+dz*.4));
}

// 3. 3D Drift Drive
let driveLane=0,driveDistance=0,driveObs=[];
(function(){
 const w=makeWorld("drive3d");if(!w)return;
 w.camera.position.set(0,4,8);w.camera.lookAt(0,0,-2);
 cube(w.scene,0x242b3a,0,-.3,-4,5,.3,20);
 for(const x of [-1.3,1.3])cube(w.scene,0x00eaff,x,-.12,-4,.04,.04,20);
 w.  const car=cube(w.scene,0xffb703,driveLane*1.3,.35,2,.8,.5,1.2);

  w.tick=()=>{
    car.position.x=driveLane*1.3;
    driveObs.forEach(o=>o.position.z+=.15);

    driveObs=driveObs.filter(o=>{
      if(o.position.z>5){
        w.scene.remove(o);
        return false;
      }

      if(
        Math.abs(o.position.z-2)<.7 &&
        Math.abs(o.position.x-car.position.x)<.8
      ){
        $("driveOut").textContent=
          "Crash! Distance: "+driveDistance+" — refresh to retry.";
      }

      return true;
    });

    driveDistance++;
    $("driveOut").textContent="Distance: "+driveDistance;

    if(Math.random()<.025){
      const lane=([-1,0,1][Math.random()*3|0]);
      driveObs.push(
        cube(w.scene,0xff3864,lane*1.3,.35,-12,.8,.6,1)
      );
    }
  };
})();

function driveMove(d){
  driveLane=Math.max(-1,Math.min(1,driveLane+d));
}

// 4. Space Blaster 3D
let spaceLane=0,spaceScore=0,spaceShots=[],spaceTargets=[];

(function(){
  const w=makeWorld("space3d",0x030014);
  if(!w)return;

  w.camera.position.set(0,4,8);
  w.camera.lookAt(0,0,-3);

  cube(w.scene,0x171737,0,-.4,-4,8,.3,20);

  const ship=cube(
    w.scene,0x00eaff,0,.35,2,.6,.35,.9
  );

  for(let i=0;i<35;i++){
    const star=cube(
      w.scene,0xffffff,
      (Math.random()-.5)*8,
      Math.random()*4,
      -Math.random()*20,
      .035,.035,.035
    );
  }

  function addTarget(){
    const target=cube(
      w.scene,0xff3864,
      ([-1,0,1][Math.random()*3|0])*1.3,
      .4,
      -12,
      .6,.6,.6
    );
    spaceTargets.push(target);
  }

  for(let i=0;i<4;i++)addTarget();

  w.tick=()=>{
    ship.position.x=spaceLane*1.3;

    spaceTargets.forEach(t=>t.position.z+=.09);
    spaceShots.forEach(s=>s.position.z-=.25);

    spaceShots=spaceShots.filter(s=>{
      if(s.position.z < -18){
        w.scene.remove(s);
        return false;
      }
      return true;
    });

    spaceTargets=spaceTargets.filter(t=>{
      const hit=spaceShots.some(s=>
        Math.abs(s.position.x-t.position.x)<.5 &&
        Math.abs(s.position.z-t.position.z)<.6
      );

      if(hit){
        w.scene.remove(t);
        spaceScore++;
        $("spaceOut").textContent="Targets hit: "+spaceScore;
        return false;
      }

      if(t.position.z>5){
        t.position.z=-12;
        t.position.x=([-1,0,1][Math.random()*3|0])*1.3;
      }

      return true;
    });

    while(spaceTargets.length<4)addTarget();
  };
})();

function spaceMove(d){
  spaceLane=Math.max(-1,Math.min(1,spaceLane+d));
}

function spaceShoot(){
  const w=scenes3d.space3d;
  if(!w)return;

  const shot=cube(
    w.scene,0x00eaff,spaceLane*1.3,.4,1,.12,.12,.5
  );

  spaceShots.push(shot);
}

// Three.js animation loop
function animate3D(){
  requestAnimationFrame(animate3D);

  Object.values(scenes3d).forEach(w=>{
    if(!w)return;

    if(typeof w.tick==="function")w.tick();

    w.renderer.render(w.scene,w.camera);
  });
}

if(window.THREE){
  animate3D();
}

// Terminal commands
function command(){
  const input=$("cmd");
  const out=$("out");
  const cmd=input.value.trim().toLowerCase();

  if(!cmd)return;

  const commands={
    help:
      "Available commands:\n"+
      "help, about, games, racing, date,\n"+
      "browser, device, network, clear",

    about:
      "ItsLakshman2018 — Creator | Gamer | Digital Explorer",

    games:
      "Available games:\n"+
      "Number Guess, Rock Paper Scissors,\n"+
      "Reflex Test, Memory Matrix, Snake,\n"+
      "Neon Runner 3D, Zombie Survival 3D,\n"+
      "3D Drift Drive, Space Blaster 3D",

    racing:
      "Neon Racing Arena is ready.\n"+
      "Choose a vehicle and press START RACE.",

    date:
      new Date().toLocaleString(),

    browser:
      "Browser: "+navigator.userAgent,

    device:
      "Screen: "+screen.width+" x "+screen.height,

    network:
      navigator.onLine
        ? "Browser reports that you are online."
        : "Browser reports that you are offline.",

    clear:""
  };

  if(cmd==="clear"){
    out.textContent="Terminal cleared.";
  }else{
    out.textContent+="\n\n> "+input.value+"\n"+
      (commands[cmd]||"Unknown command. Type help.");
  }

  out.scrollTop=out.scrollHeight;
  input.value="";
}

// Keyboard support for 3D games
document.addEventListener("keydown",e=>{
  if(["INPUT","TEXTAREA"].includes(
    document.activeElement.tagName
  ))return;

  if(e.key==="ArrowLeft"){
    runnerMove(-1);
    driveMove(-1);
    spaceMove(-1);
  }

  if(e.key==="ArrowRight"){
    runnerMove(1);
    driveMove(1);
    spaceMove(1);
  }

  if(e.code==="Space"){
    e.preventDefault();
    spaceShoot();
  }
});

// Keep the road drawing updated
$("vehicle").addEventListener("change",drawRoad);

// Flask routes are defined below in Python.
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
    app.run(host="0.0.0.0", port=port, debug=False)
