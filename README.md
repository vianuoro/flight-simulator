# SkyRiot 🛩️

**A lightweight browser flight shooter written in Python.**

SkyRiot is an arcade‑style aircraft shooter with a single, unapologetic goal:

> Get it into your browser quickly, keep it small, and keep the fun immediate.

No physics degrees. No heavy engines. Just Python, a sky‑blue backdrop, and a lot of explosions.

---

## 💡 Philosophy

This is not a flight simulator. There are no realistic aerodynamics, no 3D modeling, no server infrastructure.

What SkyRiot *is*:

* A 2D top‑down (or pseudo‑3D) shooter built with [`pygame`](https://www.pygame.org/)
* Compiled to WebAssembly with [`pygbag`](https://pygbag.readthedocs.io/) so it runs directly in your browser
* A minimal codebase that you can fork, modify, and understand in minutes

Why this approach?

1. **Simplicity** – fewer moving parts means fewer headaches.
2. **Portability** – Python code, no JavaScript required.
3. **Speed** – start playing in seconds with `pygbag`.

---

## 🛠️ Tech Stack

| Component | Purpose |
|-----------|---------|
| Python 3.11+ | Core language |
| pygame | Game library for input, graphics, sound |
| pygbag | WebAssembly exporter to run pygame in the browser |

---

## 🎮 Gameplay Overview

The game loop is intentionally basic:

1. Player aircraft moves around the screen.
2. Enemies spawn and move toward the player.
3. Player fires bullets to destroy enemies.
4. Collisions damage the player or destroy enemies.
5. Score increases with each kill.
6. Repeat until the player explodes.

Fast. Addictive. Pure arcade.

---

## 🕹 Controls

| Action | Key |
|--------|-----|
| Move   | Arrow keys or **WASD** |
| Shoot  | **Space** |
| Quit   | **Esc** |

There’s no throttle, lift, or drag — just point, shoot, and survive.

---

## 📂 Project Layout

```
skyriot/             # root package
├── main.py          # entry point
├── player.py        # player logic
├── enemy.py         # enemy behavior
├── bullet.py        # bullet handling
├── settings.py      # configurable constants
├── requirements.txt # Python dependencies
└── README.md        # you are here 📝
```

The directory is deliberately flat to keep navigation trivial.

---

## 🚀 Getting Started

### Running Locally

```bash
pip install -r requirements.txt
python main.py
```

### Playing in a Browser

```bash
pip install pygbag
pygbag .        # builds and serves the game
```

Open [http://localhost:8000](http://localhost:8000) in your browser and watch Python fly.

---

## 🧩 Contributing

Feel free to fork the repo, add new features, or refactor for fun. Pull requests are welcome!

---

## 📄 License

This project is provided under the MIT License — do whatever you like with it.

