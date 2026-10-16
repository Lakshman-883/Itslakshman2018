from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>itslakshman2018 | Official Website</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:#05080f;color:#eaf7ff;font-family:Arial,sans-serif}
header{padding:22px 8%;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:15px;border-bottom:1px solid #12344a}
.logo{color:#00d9ff;font-size:22px;font-weight:bold}
nav a{color:#d9f5ff;text-decoration:none;margin:0 8px;font-size:14px}
nav a:hover{color:#00d9ff}
.hero{min-height:75vh;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:50px 20px;background:radial-gradient(ellipse at center,#102b40 0%,#05080f 70%)}
.badge{color:#00d9ff;border:1px solid #00d9ff;padding:8px 16px;border-radius:30px;font-size:12px;letter-spacing:2px}
h1{font-size:clamp(36px,8vw,68px);margin:22px 0}
h1 span{color:#00d9ff;text-shadow:0 0 25px #007aab}
.hero p{color:#a8bdcc;max-width:600px;line-height:1.8}
.button{display:inline-block;margin:25px 8px 0;padding:12px 22px;color:#001018;background:#00d9ff;border:1px solid #00d9ff;border-radius:6px;text-decoration:none;font-weight:bold}
.button.outline{background:transparent;color:#00d9ff}
section{padding:65px 8%}
.section-title{color:#00d9ff;font-size:28px;margin-bottom:25px}
.card-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
.card{background:#0a121e;border:1px solid #15374b;padding:25px;border-radius:12px;transition:.2s}
.card:hover{border-color:#00d9ff;transform:translateY(-4px)}
.card h3{color:#00d9ff;margin-bottom:12px}
.card p{color:#a8bdcc;line-height:1.7}
.socials{display:flex;flex-wrap:wrap;gap:12px}
.socials a{color:#00d9ff;border:1px solid #15516b;border-radius:6px;padding:12px 18px;text-decoration:none}
footer{text-align:center;padding:25px;color:#8096a7;border-top:1px solid #12344a;font-size:13px}
@media(max-width:600px){header{justify-content:center}nav{text-align:center;line-height:2.4}}
</style>
</head>
<body>
<header>
<div class="logo">LAKSHMAN.DEV</div>
<nav>
<a href="#home">Home</a><a href="#about">About</a>
<a href="#projects">Projects</a><a href="#gallery">Gallery</a>
<a href="#contact">Contact</a>
</nav>
</header>
<main>
<section class="hero" id="home">
<div class="badge">WELCOME TO MY DIGITAL WORLD</div>
<h1>I'm <span>Lakshman</span></h1>
<p>Welcome to my official website. Explore my profile, creative projects, interests and digital journey — all in one place.</p>
<div><a class="button" href="#about">Explore More</a><a class="button outline" href="#contact">Connect With Me</a></div>
</section>
<section id="about">
<h2 class="section-title">// About Me</h2>
<div class="card"><h3>itslakshman2018</h3><p>I'm Lakshman. This is my personal corner on the internet. I enjoy exploring technology, creativity and new digital ideas. More about me will be added soon.</p></div>
</section>
<section id="projects">
<h2 class="section-title">// My Projects</h2>
<div class="card-grid">
<div class="card"><h3>01. Web Design</h3><p>Creative website designs with modern visual styles.</p></div>
<div class="card"><h3>02. Digital Content</h3><p>Creative ideas and content for digital platforms.</p></div>
<div class="card"><h3>03. Learning Lab</h3><p>Learning technology and building new skills.</p></div>
</div>
</section>
<section id="gallery">
<h2 class="section-title">// Gallery</h2>
<div class="card"><h3>My Gallery</h3><p>Your photos can be added here later. No photos have been uploaded yet.</p></div>
</section>
<section id="contact">
<h2 class="section-title">// Connect With Me</h2>
<div class="card"><h3>Let's Connect</h3><p>Find me on social media and follow my latest updates.</p>
<div class="socials" style="margin-top:20px">
<a href="https://www.instagram.com/itslakshman2018/" target="_blank" rel="noopener noreferrer">Instagram ↗</a>
<a href="https://www.youtube.com/" target="_blank" rel="noopener noreferrer">YouTube ↗</a>
</div></div>
</section>
</main>
<footer>© 2026 itslakshman2018 | Made with creativity and code.</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)
