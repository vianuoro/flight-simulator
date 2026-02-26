# SkyRiot 🛩️  
*A ridiculously simple browser flight shooter written in Python*

SkyRiot is a lightweight, arcade-style airplane shooter built with one goal:

> Make it playable fast.  
> Make it run in a browser.  
> Keep it simple.

No over-engineered engines. No aerospace PhD required. Just Python, a sky-colored background, and things that explode when you shoot them.

---

## 🧠 The Easiest Possible Approach

We are not building a full 3D simulator.

We are building:

**A 2D top-down or pseudo-3D shooter using `pygame`, compiled to WebAssembly with `pygbag`.**

That’s it.

### Why?

- `pygame` is simple
- `pygbag` runs pygame in the browser
- No custom WebGL
- No backend server
- No complicated rendering pipeline
- Just Python → browser

---

## 🛠 Tech Stack

- **Python 3.11+**
- **pygame**
- **pygbag** (to run in browser)

---

## 🎮 Game Design (Minimal Version)

### Core Gameplay Loop

- Player airplane moves around screen
- Enemy airplanes spawn
- Player shoots bullets
- Bullets destroy enemies
- Enemies damage player on collision
- Score increases
- Repeat until explosion

Fast. Arcade. Clean.

---

## 🕹 Controls

| Action | Key |
|--------|------|
| Move   | Arrow Keys or WASD |
| Shoot  | Space |
| Quit   | ESC |

No throttle.  
No lift equations.  
No wind resistance debates.

We vibe first. We optimize later.

---

## 📁 Project Structure
