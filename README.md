# 🌿 _EXYDE_

<p align="left">
  <img src="https://img.shields.io/badge/-000000?logo=github&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/-000000?logo=itch.io&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/-000000?logo=unity&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/-000000?logo=unrealengine&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/-000000?logo=cplusplus&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/-000000?logo=python&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/-000000?logo=opengl&logoColor=white&style=for-the-badge" />
</p>

___ 

<p align="center">
  <svg width="240" height="220" viewBox="0 0 240 220" xmlns="http://www.w3.org/2000/svg">
    <style>
      .tri {
        fill: #f6d400;
        animation: blink 1s infinite alternate;
        filter: url(#crt-glow);
      }

      @keyframes blink {
        0%, 70% { opacity: 1; transform: translate(0,0) scale(1); }
        80% { opacity: 0.6; transform: translate(1px,-1px) scale(1.02); }
        90% { opacity: 0.3; transform: translate(-1px,1px) scale(0.98); }
        100% { opacity: 1; transform: translate(0,0) scale(1); }
      }

      text {
        fill: #ffee88;
        font-family: 'Courier New', monospace;
        font-size: 18px;
        text-anchor: middle;
        letter-spacing: 6px;
        animation: textGlitch 2s infinite;
      }

      @keyframes textGlitch {
        0%, 100% { opacity: 1; transform: translate(0,0); }
        20% { opacity: 0.9; transform: translate(1px, -1px); }
        40% { opacity: 0.8; transform: translate(-1px, 1px); }
        60% { opacity: 1; transform: translate(1px, 0); }
        80% { opacity: 0.9; transform: translate(0, -1px); }
      }

      .scanline {
        stroke: rgba(255,255,255,0.05);
        stroke-width: 1;
      }

      .crt {
        animation: flicker 0.2s infinite alternate;
      }

      @keyframes flicker {
        from { opacity: 0.95; }
        to { opacity: 1; }
      }
    </style>

    <defs>
      <filter id="crt-glow">
        <feGaussianBlur stdDeviation="1.2" result="blur"/>
        <feMerge>
          <feMergeNode in="blur"/>
          <feMergeNode in="SourceGraphic"/>
        </feMerge>
      </filter>
    </defs>

    <!-- CRT scanlines -->
    <g>
      <rect width="240" height="220" fill="black"/>
      <g class="crt">
        <!-- Triforce -->
        <polygon class="tri" points="120,30 80,90 160,90"/>
        <polygon class="tri" points="80,130 40,190 120,190"/>
        <polygon class="tri" points="160,130 120,190 200,190"/>
        <!-- Text -->
        <text x="120" y="210">E X Y D E</text>
      </g>

      <!-- horizontal scanlines -->
      <g>
        <!-- 220 / 4px spacing ≈ 55 lines -->
        <g>
          <line class="scanline" x1="0" y1="4" x2="240" y2="4" />
          <line class="scanline" x1="0" y1="8" x2="240" y2="8" />
          <line class="scanline" x1="0" y1="12" x2="240" y2="12" />
          <line class="scanline" x1="0" y1="16" x2="240" y2="16" />
          <!-- You can copy-paste more if you want denser lines -->
        </g>
      </g>
    </g>
  </svg>
</p>

<svg width="240" height="220" viewBox="0 0 240 220" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Glow simple -->
    <filter id="glow">
      <feGaussianBlur stdDeviation="2" />
    </filter>
  </defs>

  <!-- Fond noir -->
  <rect width="240" height="220" fill="black"/>

  <!-- Triforce avec glow -->
  <polygon fill="#f6d400" points="120,30 80,90 160,90" filter="url(#glow)"/>
  <polygon fill="#f6d400" points="80,130 40,190 120,190" filter="url(#glow)"/>
  <polygon fill="#f6d400" points="160,130 120,190 200,190" filter="url(#glow)"/>

  <!-- Texte -->
  <text x="120" y="210" fill="#ffee88" font-family="Courier New" font-size="18" text-anchor="middle">
    E X Y D E
  </text>
</svg>


<svg width="240" height="220" viewBox="0 0 240 220" xmlns="http://www.w3.org/2000/svg">
  <polygon fill="#f6d400" points="120,30 80,90 160,90"/>
  <polygon fill="#f6d400" points="80,130 40,190 120,190"/>
  <polygon fill="#f6d400" points="160,130 120,190 200,190"/>
  <text x="120" y="210" fill="#ffee88" font-family="Courier New" font-size="18" text-anchor="middle">E X Y D E</text>
</svg>

___

<p align="center">
  <svg width="200" height="180" viewBox="0 0 200 180" xmlns="http://www.w3.org/2000/svg">
    <style>
      .tri { fill:#f0d000; animation: blink 1.2s infinite alternate; }
      .glitch { fill:#f0d000; filter:url(#glitch); }
      @keyframes blink {
        0%, 80% { opacity:1; }
        90%, 100% { opacity:0.2; }
      }
      text {
        fill:#e0e0a0;
        font-family:'Courier New', monospace;
        font-size:16px;
        text-anchor:middle;
        animation: glitchText 2s infinite;
      }
      @keyframes glitchText {
        0% { transform: translate(0,0); opacity:1; }
        20% { transform: translate(1px,-1px); opacity:0.9; }
        40% { transform: translate(-1px,1px); opacity:1; }
        60% { transform: translate(1px,0); opacity:0.8; }
        80% { transform: translate(0,-1px); opacity:1; }
        100% { transform: translate(0,0); opacity:1; }
      }
    </style>
    <defs>
      <filter id="glitch">
        <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" result="turb"/>
        <feDisplacementMap in2="turb" in="SourceGraphic" scale="3"/>
      </filter>
    </defs>
    <!-- Triforce -->
    <polygon class="tri" points="100,10 60,70 140,70"/>
    <polygon class="tri" points="60,110 20,170 100,170"/>
    <polygon class="tri" points="140,110 100,170 180,170"/>
    <!-- Pseudo -->
    <text x="100" y="175">E X Y D E</text>
  </svg>
</p>



---

## 🌱 Hey ! I'm Younes "_Exyde_" Balandjian

🔭 _French video game & interactive experience developer._

I love crafting interactive works — blending **art, tech, and meaning** — with an indie spirit.

Check my [WIP Engine/Renderer project](https://exyde.github.io/OpenGLRenderer/)

---

## 🧠 Core Skills

| Domain | Tools / Languages / Frameworks |
| ------- | ------------------------------ |
| 🎮 **Game Creation** | Game Design, Tech Art, Shaders, 3D, VFX, Production |
| 💻 **Programming** | C++, C#, Python, GLSL, HLSL, Haxe |
| 🔥 **Real-Time VFX** | ShaderGraph, VFX Graph, Niagara, Blender, Photoshop, Krita |
| ⚙️ **Game Engines** | Unity, Godot, Unreal, Custom Tools & Pipelines |
| 🧩 **Engine & Renderer Dev** | OpenGL, C++, Graphics Architecture |
| 🛠️ **IRL Creation** | Woodworking, Arduino, 3D Printing, DIY Prototyping |

---

## 🔗 Links

| Links | Topic |
| ------ | ------ |
| [**Itch**] | Video Games & Interactive Experiences |
| [**Instagram**] | VFX, Political art, sharing & experiments |
| [**Bluesky**] | Random thoughts, OpenGL renderer logs |
| [**Github**] | Various projects & open-source utilities |
| [**Soundcloud**] | Old musical memories |
| [**Youtube**] | Literally anything! |
| [**exyde.com**] | 🌱 Work in progress |

[**Itch**]: https://exyde.itch.io/
[**Instagram**]: https://www.instagram.com/exyde_/
[**Bluesky**]: https://bsky.app/profile/exyde.bsky.social
[**Github**]: https://github.com/Exyde
[**Soundcloud**]: https://soundcloud.com/mystprod
[**Youtube**]: https://www.youtube.com/@exyde_sly
[**exyde.com**]: https://github.com/Exyde

---

## 🧩 Works — Incoming!

| Project | Description | Role |
| -------- | ------------ | ---- |
| [**World Of Aria**] | Ludogram stuff... | Gameplay Programmer, Technical Artst |
| [**Road96**] | Digix Art stuff... | QA Tester 
| [**Tool & Resources Database**] | Incoming... |
| [**Kingdom Heroes**] | Work Description... | Tech Art, Programmation, Optimization, VFX
| [**Etude n°4**] | ... | Project Management & Full Prototyping - VR Version to come
| [**What Remains of Ourselves**] | ... | Engine Programming, Design, Code, Everyrthing :)
| [**Master Thesis + Game**] | ... |
| [**Outtraghe**] | ... | Game Design, Programming, Artistic Direction
| [**Game Engine**] | ... | Actually, building the engine in c++ !

[**World Of Aria**]: #
[**Road96**]: #
[**Tool & Resources Database**]: #
[**Kingdom Heroes**]: https://github.com/Exyde
[**Etude n°4**]: https://github.com/Exyde
[**What Remains of Ourselves**]: https://github.com/Exyde
[**Master Thesis + Game**]: https://github.com/Exyde
[**Outtraghe**]: https://github.com/Exyde
[**Game Engine**]: https://github.com/Exyde

---

## 📰 Featured

| Reference | Description |
| ---------- | ------------ |
| [**Arles Jam Article**] | ? |

[**Arles Jam Article**]: #
