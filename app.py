from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>itslakshman2018 | Digital World</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{
 background:#03060b;color:#e8faff;
 font-family:Arial,sans-serif;overflow-x:hidden
}
canvas{
 position:fixed;inset:0;width:100%;height:100%;
 z-index:-1;opacity:.35
}
header{
 position:sticky;top:0;z-index:5;
 display:flex;justify-content:space-between;align-items:center;
 padding:20px 8%;background:#03060be8;
 border-bottom:1px solid #00d9ff55
}
.logo{font-size:19px;font-weight:bold;color:#00d9ff}
nav a{color:#d8faff;text-decoration:none;margin-left:18px;font-size:13px}
nav a:hover{color:#00d9ff}
.hero{
 min-height:85vh;display:flex;flex-direction:column;
 justify-content:center;align-items:center;text-align:center;padding:50px 20px
}
.tag{
 border:1px solid #00d9ff;color:#00d9ff;padding:9px 16px;
 border-radius:30px;font-size:11px;letter-spacing:3px
}
h1{font-size:clamp(36px,8vw,72px);margin:25px 0}
.glow{color:#00d9ff;text-shadow:0 0 12px #00d9ff,0 0 35px #007bff}
.hero p{max-width:580px;line-height:1.8;color:#a8c2d2}
.btn{
 display:inline-block;margin:25px 7px;padding:13px 22px;
 color:#001018;background:#00d9ff;text-decoration:none;
 border-radius:5px;font-weight:bold;box-shadow:0 0 20px #00d9ff55
}
.btn:hover{transform:translateY(-3px)}
.btn.alt{background:transparent;color:#00d9ff;border:1px solid #00d9ff}
section{padding:70px 8%;scroll-margin-top:70px}
.title{font-size:27px;color:#00d9ff;margin-bottom:25px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:18px}
.card{
 padding:25px;background:#08111cdd;border:1px solid #123d50;
 border-radius:10px;transition:.25s
}
.card:hover{border-color:#00d9ff;box-shadow:0 0 22px #00d9ff22;transform:translateY(-4px)}
.card h3{color:#00d9ff;margin-bottom:12px}
.card p{color:#a8c2d2;line-height:1.7}
.social{
 display:inline-block;margin-top:18px;padding:13px 20px;
 color:#00d9ff;border:1px solid #00d9ff;border-radius:6px;
 text-decoration:none
}
.social:hover{background:#00d9ff;color:#001018}
footer{text-align:center;padding:28px;color:#829aaa;border-top:1px solid #123d50}
@media(max-width:600px){
 header{padding:16px 5%;flex-direction:column;gap:13px}
 nav a{margin:0 7px;font-size:12px}
 section{padding:55px 6%}
}
</style>
</head>
<body>
<canvas id="matrix"></canvas>

<header>
 <div class="logo">LAKSHMAN.DEV</div>
 <nav>
  <a href="#home">HOME</a>
  <a href="#about">ABOUT</a>
  <a href="#projects">PROJECTS</a>
  <a href="#contact">CONTACT</a>
 </nav>
</header>

<main>
<section class="hero" id="home">
 <div class="tag">WELCOME TO MY DIGITAL WORLD</div>
 <h1>I'm <span class="glow">Lakshman</span></h1>
 <p>Creator • Gamer • Digital Explorer<br>
 Welcome to my personal website. Explore my world, projects and creative journey.</p>
 <div>
  <a class="btn" href="#about">EXPLORE MORE</a>
  <a class="btn alt" href="#contact">INSTAGRAM ↗</a>
 </div>
</section>

<section id="about">
 <h2 class="title">// ABOUT ME</h2>
 <div class="card">
  <h3>itslakshman2018</h3>
  <p>I'm Lakshman. I enjoy gaming, creativity, technology and exploring new digital ideas. This is my personal space on the internet.</p>
 </div>
</section>

<section id="projects">
 <h2 class="title">// MY PROJECTS</h2>
 <div class="grid">
  <div class="card"><h3>01 / WEB DESIGN</h3><p>Building modern websites with creative designs and interactive effects.</p></div>
  <div class="card"><h3>02 / GAMING</h3><p>Gaming interests, highlights and my digital gaming world.</p></div>
  <div class="card"><h3>03 / CREATIVE LAB</h3><p>Exploring fresh ideas and learning new technology skills.</p></div>
 </div>
</section>

<section id="contact">
 <h2 class="title">// CONNECT WITH ME</h2>
 <div class="card">
  <h3>Let's Connect</h3>
  <p>Follow me on Instagram to see my profile and updates.</p>
  <a class="social" href="https://www.instagram.com/itslakshman2018?igsh=MjM3a3VmbW0xeG1z" target="_blank" rel="noopener noreferrer">@itslakshman2018 — Instagram ↗</a>
 </div>
</section>
</main>

<footer>© 2026 itslakshman2018 | Built with creativity & code.</footer>

<script>
const canvas=document.getElementById("matrix");
const ctx=canvas.getContext("2d");
let drops=[];
function resize(){
 canvas.width=innerWidth;
 canvas.height=innerHeight;
 drops=Array(Math.ceil(canvas.width/18)).fill(1);
}
function draw(){
 ctx.fillStyle="rgba(3,6,11,0.12)";
 ctx.fillRect(0,0,canvas.width,canvas.height);
 ctx.fillStyle="#00d9ff";
 ctx.font="14px monospace";
 drops.forEach((y,i)=>{
  const char=String.fromCharCode(33+Math.random()*90);
  ctx.fillText(char,i*18,y*18);
  if(y*18>canvas.height&&Math.random()>.975)drops[i]=0;
  drops[i]++;
 });
}
addEventListener("resize",resize);
resize();
setInterval(draw,55);
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)
