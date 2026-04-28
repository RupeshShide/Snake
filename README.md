# 🐍 Snake CLI Game

A classic Snake game built in Python for terminal (CLI) with number-based controls.

---

## 📖 Description

This is a terminal-based Snake game developed in Python using the built-in curses library.
The game runs entirely in CLI and provides smooth gameplay, real-time movement, and score tracking.

This version uses number-based navigation instead of arrow keys, making it more compatible with Termux and Linux environments.

---

## 🎮 Controls

2 → Move Up  
8 → Move Down  
4 → Move Left  
6 → Move Right  
0 → Exit Game  

---

## ⚡ Features

- Smooth snake movement  
- Random food generation  
- Live score tracking  
- Game over detection (wall + self collision)  
- Number key controls (Termux friendly)  
- Works on Linux & Termux  

---

## 🧩 Dependencies

This game uses only Python built-in modules:

- curses  
- random  

Note:
- curses is pre-installed on most Linux systems  
- Works in Termux with default Python  

---

## 📦 Installation

### 1. Install Python

Termux:
pkg update && pkg upgrade  
pkg install python  

Linux (Ubuntu/Kali/Debian):
sudo apt update  
sudo apt install python3  

---

### 2. Clone Repository

git clone https://github.com/RupeshShide/snake.git  
cd snake  
chmod +x *
---

### 3. Run Game

python3 snake.py  

---

## ⚠️ Notes

- Run in full-screen terminal for best experience  
- If controls lag, reduce timeout in code  
- Designed for CLI environments  

---

## 👨‍💻 Developer

Rupesh Shide  

---

## 🚀 Future Updates

- Color UI  
- Speed levels  
- Obstacles  
- High score system  

---
