import os
import re
import glob

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

  <div class="back-btn-container">
    <a href="javascript:history.back()" class="back-btn">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
    </a>
  </div>

  <header>
    <div class="brand" onclick="window.location.href='index.html'">DailyDoseofBCA</div>
    <div class="page-subtitle">{title}</div>
  </header>

  <!-- Grid Content -->
  <div class="grid-container">
{cards}
  </div>

  <!-- Interactions Script -->
  <script src="assets/js/interactions.js"></script>
</body>
</html>"""

def refactor_assi(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract Title (try h1, h2)
    title_match = re.search(r'<h1>(.*?)</h1>', content)
    if not title_match:
        title_match = re.search(r'<h2>(.*?)</h2>', content)
        
    title = title_match.group(1).strip() if title_match else "Assignments / Notes"
    # Remove any inner HTML tags from title
    title = re.sub(r'<[^>]+>', '', title)

    cards_html = ""
    
    # Method 1: .cont
    conts = re.findall(r'<div class="cont.*?">(.*?)</div>', content, re.DOTALL)
    if conts:
        for cont in conts:
            ip_match = re.search(r'<p class="ip">(.*?)</p>', cont, re.DOTALL)
            a_match = re.search(r'<a.*?href="(.*?)".*?>(.*?)</a>', cont, re.DOTALL)
            card_title = ip_match.group(1).strip() if ip_match else "Document"
            card_link = a_match.group(1).strip() if a_match else "#"
            card_btn = "Open"
            cards_html += f"""
    <div class="glass-card">
      <div class="card-header"><span class="subject">{card_title}</span></div>
      <p class="description">Access the document.</p>
      <a href="{card_link}" class="action-btn assign" target="_blank">{card_btn}</a>
    </div>"""

    # Method 2: .assign-card
    elif '<div class="assign-card' in content:
        conts = re.findall(r'<div class="assign-card.*?">(.*?)</div>\s*</div>', content, re.DOTALL)
        if not conts: # Fallback strict match
            conts = re.split(r'<div class="assign-card', content)[1:]
        for cont in conts:
            h3_match = re.search(r'<h3.*?>(.*?)</h3>', cont, re.DOTALL)
            p_match = re.search(r'<p>(.*?)</p>', cont, re.DOTALL)
            a_match = re.search(r'<a.*?href="(.*?)".*?>', cont, re.DOTALL)
            
            card_title = h3_match.group(1).strip() if h3_match else "Document"
            desc = p_match.group(1).strip() if p_match else "Access the document."
            card_link = a_match.group(1).strip() if a_match else "#"
            
            cards_html += f"""
    <div class="glass-card">
      <div class="card-header"><span class="subject">{card_title}</span></div>
      <p class="description">{desc}</p>
      <a href="{card_link}" class="action-btn assign" target="_blank">Open</a>
    </div>"""

    # Method 3: .note-item
    elif '<div class="note-item">' in content:
        conts = re.findall(r'<div class="note-item">(.*?)</div>', content, re.DOTALL)
        for cont in conts:
            p_match = re.search(r'<p class="note-title.*?">(.*?)</p>', cont, re.DOTALL)
            a_match = re.search(r'<a.*?href="(.*?)".*?>', cont, re.DOTALL)
            
            card_title = p_match.group(1).strip() if p_match else "Document"
            card_link = a_match.group(1).strip() if a_match else "#"
            
            cards_html += f"""
    <div class="glass-card">
      <div class="card-header"><span class="subject">{card_title}</span></div>
      <p class="description">Access the document.</p>
      <a href="{card_link}" class="action-btn assign" target="_blank">Open</a>
    </div>"""
    else:
        print(f"Skipping {file_path}, unsupported layout.")
        return

    if cards_html:
        new_content = template.replace('{title}', title).replace('{cards}', cards_html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Refactored {file_path}")
    else:
        print(f"Failed to extract cards for {file_path}")

files = glob.glob("*assi.html") + glob.glob("*-assignment.html") + glob.glob("*-notes.html") + glob.glob("*-labmanual.html") + glob.glob("*assign.html")
for f in files:
    refactor_assi(f)
