import os
import re

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
  <title>DailyDoseofBCA</title>

  <!-- FAVICON -->
  <link rel="icon" href="mylogo.png" type="image/png">
  <link rel="apple-touch-icon" href="mylogo.png">

  <!-- Global UI Redesign -->
  <link rel="stylesheet" href="assets/css/global.css">
</head>
<body>

  <!-- Interactive Background -->
  <canvas id="interactive-canvas"></canvas>

  <header>
    <div class="brand" onclick="window.location.href='index.html'">DailyDoseofBCA</div>
    <div class="page-subtitle">{subtitle}</div>
    <p class="subtitle-desc">Get all your notes, assignments here which are handwritten</p>
  </header>

  <!-- Main Content Slider -->
  <div class="slider-viewport" id="viewport">
    <div class="slider-track" id="track">
{slides}
    </div>
  </div>

  <!-- BOTTOM FLOATING NAV -->
  <div class="nav-wrapper">
    <div class="nav-center-wrap">
      <div class="nav-container" id="nav-container">
        <div class="nav-knob" id="nav-knob"></div>
        <div class="nav-item active" data-index="0">Notes</div>
        <div class="nav-item" data-index="1">Assign</div>
        <div class="nav-item" data-index="2">Lab</div>
      </div>
      
      <!-- Mini Menu Box for Semesters -->
      <div class="sem-menu" id="sem-menu">
        <a href="bca-sem1.html" class="sem-menu-btn">Sem 1</a>
        <a href="bca-sem2.html" class="sem-menu-btn">Sem 2</a>
        <a href="bca-sem3.html" class="sem-menu-btn">Sem 3</a>
        <a href="bca-sem4.html" class="sem-menu-btn">Sem 4</a>
        <a href="bca-sem5.html" class="sem-menu-btn">Sem 5</a>
        <a href="bca-sem6.html" class="sem-menu-btn">Sem 6</a>
      </div>
    </div>
    
    <div class="sem-button" id="sem-btn">Sem</div>
  </div>

  <!-- Interactions Script -->
  <script src="assets/js/interactions.js"></script>
</body>
</html>"""

def refactor_sem(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Subtitle
    subtitle_match = re.search(r'<div class="sem-subtitle">(.*?)</div>', content)
    subtitle = subtitle_match.group(1) if subtitle_match else "Semester"

    # Extract Slides
    # Find start of <div class="slider-track" id="track">
    track_start_idx = content.find('<div class="slider-track" id="track">')
    if track_start_idx == -1:
        print(f"Skipping {file_path}, no slider track found.")
        return
        
    track_start_idx += len('<div class="slider-track" id="track">')
    
    # Simple extraction by looking for the end of the track.
    # The track is closed before </div>\n  </div>\n\n  <!-- BOTTOM FLOATING NAV -->
    end_marker = '<!-- BOTTOM FLOATING NAV -->'
    track_end_idx = content.find(end_marker, track_start_idx)
    
    slides_raw = content[track_start_idx:track_end_idx]
    # Remove trailing </div> that closes track and viewport
    slides_raw = slides_raw.rsplit('</div>', 2)[0]
    
    new_content = template.replace('{subtitle}', subtitle).replace('{slides}', slides_raw)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Refactored {file_path}")

for i in range(1, 7):
    file_path = f"bca-sem{i}.html"
    if os.path.exists(file_path):
        refactor_sem(file_path)
