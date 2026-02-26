# flight-simulator
AI-written-flight-simulator

# SkyRiot 🛩️🔥  
*A browser-based Python flight combat simulator*

SkyRiot is an arcade-style 3D flight simulator where you pilot a fighter jet, weave through the sky, and engage enemy aircraft in fast-paced aerial combat.

Built in **Python**, designed to run in the **browser**, and structured for fun-first experimentation.

---

## 🎯 Vision

Create a lightweight, multiplayer-ready (eventually), browser-playable dogfighting simulator that balances:

- ✈️ Responsive flight physics  
- 🎮 Arcade-style combat  
- 🌐 Web deployment  
- 🧠 Clean, modular Python architecture  

This is not a hyper-realistic aerospace engineering project.  
This is speed, sky, and smoke trails.

---

## 🛠 Tech Stack

### Core Language
- **Python 3.11+**

### Rendering (Browser-Compatible Options)
One of the following approaches will be used:

- **Pyodide** (Python running in WebAssembly)
- **Brython**
- **Pygbag** (Pygame → WebAssembly)
- Or a Python backend + WebGL frontend

### Graphics / Engine Options
- `pygame` (arcade prototype)
- `moderngl`
- `ursina`
- Or custom WebGL bridge

Final stack will evolve as the project matures.

---

## 🕹 Gameplay Features (Planned)

### Phase 1 — Prototype
- Player-controlled aircraft
- Basic 3D or pseudo-3D skybox
- Throttle control
- Pitch / yaw / roll
- Shooting projectiles
- Enemy AI aircraft
- Collision detection
- Health system

### Phase 2 — Combat Polish
- Lock-on targeting
- Missile system
- Bullet spread + recoil
- Particle trails
- Explosions
- Sound effects

### Phase 3 — Advanced Systems
- Multiplayer dogfights
- Leaderboards
- Procedural sky environments
- Damage modeling
- HUD with radar + velocity vector

---

## 🎮 Controls (Planned)

| Action        | Key |
|--------------|-----|
| Pitch        | W / S |
| Roll         | A / D |
| Yaw          | Q / E |
| Throttle     | Shift / Ctrl |
| Fire Gun     | Space |
| Fire Missile | F |

Controls are configurable.

---

## 🧠 Architecture Overview
