# 🎮 Pokemon Summary – Flask Web App

A **Flask web application** that recreates the classic **Game Boy Pokémon summary screen**.

The app displays a team of six Pokémon with their **sprite, cry, trainer memo, ability, stats, and move details**, styled to resemble the original retro interface from the Pokémon games.

---

## 👨‍💻 Author

**Aditya Bhardwaj**
B.Tech – Computer Science Engineering
Section: D2
Roll No: 07

This project was created as part of personal practice to explore **Flask backend development, frontend UI rendering, and game-style interface design using web technologies.**

---

# ✨ Features

* Retro **Game Boy–style summary interface**
* Board overlays for:

  * Info
  * Skills
  * Moves
* **Keyboard-only navigation** for switching Pokémon and cards
* Backend **Flask API** serving Pokémon summary data
* **Audio effects**

  * UI click sound
  * Individual Pokémon cry

---

# 🧰 Tech Stack

| Technology | Usage                                |
| ---------- | ------------------------------------ |
| Python 3   | Backend logic                        |
| Flask      | Web server and API                   |
| HTML       | UI structure                         |
| CSS        | Retro pixel UI styling               |
| JavaScript | Client-side rendering and navigation |

---

# 📁 Project Structure

```
Pokemon-Summary/
│
├── app.py
│   Flask application with routes and Pokémon API
│
├── templates/
│   └── index.html
│      Main UI layout
│
├── static/
│   ├── frontend/
│   │   ├── script.js
│   │   │   Client-side rendering, state handling,
│   │   │   keyboard controls, and audio playback
│   │   └── style.css
│   │       Retro pixel-style UI and animations
│   │
│   ├── Images/
│   │   Pokémon sprites and board overlays
│   │
│   ├── sound/
│   │   Pokémon cries and click sound effects
│   │
│   └── types_logo/
│       Pokémon type icons
│
└── data/
    ├── pokemon_constants.py
    │   Pokémon names, abilities, and trainer memo text
│
    ├── pokemon_moves_fire_red.py
    │   Move definitions and team move lists
│
    └── reference.py
        Sprite and cry file mappings
```

---

# 🐾 Pokémon Included

The application displays the following Pokémon:

* Charizard
* Blastoise
* Nidoking
* Venusaur
* Alakazam
* Pikachu

---

# 🎮 Controls

Keyboard navigation is used to interact with the interface.

| Key                                    | Action                                |
| -------------------------------------- | ------------------------------------- |
| `ArrowUp`                              | Next Pokémon                          |
| `ArrowDown`                            | Previous Pokémon                      |
| `ArrowLeft`                            | Previous card (Info / Skills / Moves) |
| `ArrowRight`                           | Next card (Info / Skills / Moves)     |
| `ArrowUp` / `ArrowDown` (Moves screen) | Change selected move                  |
| `Enter` or `Z`                         | Replay Pokémon cry                    |

---

# 🔌 API

## GET `/api/pokemon`

Returns a list of **six Pokémon objects**.

Each object contains:

### Basic Information

* `name`
* `dex`
* `nickname`
* `level`
* `item`

### Trainer Information

* `trainer`
* `id_number`
* `trainer_memo`

### Pokémon Details

* `type1`
* `type2`
* `ability`
* `ability_desc`

### Assets

* `image`
* `cry`

### Battle Stats

* `hp`
* `attack`
* `defence`
* `sp_atk`
* `speed`

### Moves

Each move includes:

* `name`
* `power`
* `accuracy`
* `pp`
* `description`
* `effect`

---

# ⚙️ Setup

### 1️⃣ Create a virtual environment

```powershell
python -m venv .venv
```

### 2️⃣ Activate the environment

```powershell
.\\.venv\\Scripts\\Activate.ps1
```

### 3️⃣ Install dependencies

```powershell
pip install flask
```

### 4️⃣ Run the application

```powershell
python app.py
```

Open the application in your browser:

```
http://127.0.0.1:5000/
```

---

# 🖼 Static Assets

The UI depends on these folders:

* `static/Images/boards/` → board overlays
* `static/Images/` → Pokémon sprite images
* `static/sound/` → Pokémon cries and click sound effects
* `static/types_logo/` → Pokémon type icons

If removing assets for GitHub size optimization, ensure all files referenced in:

* `data/reference.py`
* `static/frontend/script.js`

are still available.

---

# 📌 Notes

* Pokémon team data is currently **static and hardcoded** in Python files.
* The `models/` directory contains extra modules that are **not required by the current Flask route flow**.
* This project focuses mainly on **UI recreation and API integration rather than game mechanics.**

---

# ⭐ Future Improvements

Possible enhancements:

* Add **dynamic team builder**
* Integrate **PokéAPI for live data**
* Support **mobile controls**
* Add **battle simulation**
* Improve **pixel-perfect UI accuracy**

---

If you like the project, consider ⭐ starring the repository!
