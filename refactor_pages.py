import os
import re

about_template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
  <title>About Me</title>

  <!-- FAVICON -->
  <link rel="icon" href="mylogo.png" type="image/png">
  <link rel="apple-touch-icon" href="mylogo.png">

  <!-- Global UI Redesign -->
  <link rel="stylesheet" href="assets/css/global.css">
  <style>
    .profile-card {
        text-align: center;
        padding: 40px 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .profile-pic {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        border: 4px solid var(--accent-cyan);
        box-shadow: 0 0 20px rgba(0, 240, 255, 0.4);
        margin-bottom: 20px;
    }
    .about-text {
        font-size: 1.1rem;
        line-height: 1.8;
        color: var(--text-secondary);
        max-width: 600px;
        margin: 20px auto;
    }
    .video-section {
        margin-top: 40px;
        width: 100%;
        max-width: 600px;
    }
    .video-section video {
        width: 100%;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border: 1px solid var(--glass-border);
    }
  </style>
</head>
<body>

  <!-- Interactive Background -->
  <canvas id="interactive-canvas"></canvas>

  <div class="back-btn-container">
    <a href="javascript:history.back()" class="back-btn">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
    </a>
  </div>

  <header>
    <div class="brand" onclick="window.location.href='index.html'">DailyDoseofBCA</div>
    <div class="page-subtitle">About Me</div>
  </header>

  <div class="grid-container" style="display:flex; justify-content:center;">
    <div class="glass-card profile-card">
      <img class="profile-pic" src="batman1.jpg" alt="Your Picture">
      <h2 style="font-size: 2rem; color: #fff;">Waheed</h2>
      
      <p class="about-text">
        Hello! I'm Batman, a passionate individual with expertise in Joking. 
        I love working on challenging projects and constantly learning new things to improve myself and contribute effectively. 
        When I'm not working, you can find me exploring technology, reading jokes, or spending quality time with loved ones and cracking hard jokes on them.
      </p>

      <div class="video-section">
          <h3 style="margin-bottom: 15px; color: var(--accent-cyan);">Introduction Video</h3>
          <video controls autoplay muted loop>
              <source src="daredevil.mp4" type="video/mp4">
              Your browser does not support the video tag.
          </video>
      </div>
    </div>
  </div>

  <!-- Interactions Script -->
  <script src="assets/js/interactions.js"></script>
</body>
</html>"""

def refactor_about():
    with open('about.html', 'w', encoding='utf-8') as f:
        f.write(about_template)
    print("Refactored about.html")

def update_colors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply midnight glass theme colors to contact and admin
    content = content.replace('--bg: #0d0f14;', '--bg: #050505;')
    content = content.replace('--bg: #10131a;', '--bg: #050505;')
    content = content.replace('--accent: #2dd4bf;', '--accent: #00f0ff;')
    content = content.replace('--accent: #38bdf8;', '--accent: #00f0ff;')
    content = content.replace('--accent-2: #60a5fa;', '--accent-2: #8a2be2;')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated colors for {file_path}")

refactor_about()
if os.path.exists('contact.html'):
    update_colors('contact.html')
if os.path.exists('admin.html'):
    update_colors('admin.html')
