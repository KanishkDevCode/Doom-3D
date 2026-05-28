# Doom 3D - Python Raycasting Engine

A 2.5D First-Person Shooter (FPS) game heavily inspired by the classic **Doom**. Built entirely in Python using the `pygame` library. 

Unlike modern games that use 3D APIs (like OpenGL or Vulkan), this project uses a custom-built **Raycasting Engine** from scratch to render a 3D perspective from a 2D grid map—mirroring the exact technical constraints and brilliance of early 90s games.

## 🚀 Features

* **Custom Raycasting Engine**: A fully functional DDA (Digital Differential Analyzer) raycaster built from the ground up.
* **Animated Sprites**: Supports 2D sprites in 3D space, scaling correctly based on depth and distance.
* **Enemy AI & Pathfinding**: Enemies navigate the map using **Breadth-First Search (BFS)** algorithms to find the shortest path to the player.
* **Combat System**: Includes a functional shotgun weapon, player health, taking damage, and enemy line-of-sight detection.
* **Immersive Audio**: Integrated sound effects for shooting, enemy noises, and a background theme.
* **Highly Modular Architecture**: Clean, object-oriented codebase separating logic for the player, rendering, map, pathfinding, and UI.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KanishkDevCode/Doom-3D.git
   cd Doom-3D
   ```

2. **Install requirements:**
   The only external dependency required is `pygame`. You can install it using pip:
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   Navigate into the game folder and run `main.py`:
   ```bash
   cd RaycastingGame
   python main.py
   ```

## 🎮 Controls

* **W, A, S, D**: Move forward, left, backward, right
* **Mouse Movement**: Look around (left/right)
* **Left Mouse Button**: Fire shotgun
* **ESC**: Quit the game

## 📁 Project Structure

* `main.py`: The entry point and main game loop.
* `raycasting.py`: The core math for distance calculation, texture mapping, and projection.
* `map.py`: Contains the 2D grid matrix of the level map.
* `player.py`: Handles player movement, mouse view, collision, and health.
* `object_renderer.py`: Handles rendering the UI elements, sky, floor, and scaling walls/sprites.
* `npc.py` & `object_handler.py`: Manages enemy behavior, stats, logic, and spawning.
* `pathfinding.py`: Uses a BFS algorithm for the enemies to track the player.

## 📜 License
This project is open-source and available under the MIT License. Feel free to fork, modify, and improve!
