# Snake Water Gun Game (Python)

## Project Overview

This project is a **simple command-line game built using Python** where the user plays **Snake-Water-Gun** against the computer.
The computer randomly selects a choice, and the program decides the winner based on the game rules.

This project demonstrates fundamental Python concepts such as:

* Functions
* Conditional statements
* Lists
* User input handling
* Random module usage

## Game Rules

The rules of the game are similar to **Rock-Paper-Scissors**:

* 🐍 **Snake drinks Water → Snake wins**
* 💧 **Water damages Gun → Water wins**
* 🔫 **Gun kills Snake → Gun wins**

If both the user and computer choose the same option, the result is a **Draw**.

## How the Game Works

1. The user enters one of the following choices:
   * `snake`
   * `water`
   * `gun`

2. The computer randomly selects one of these options.

3. The program compares both choices and prints the result:

   * **You win**
   * **Computer win**
   * **Draw**

---

## Technologies Used

* Python
* Random Module

## Example Output

Enter snake, water or gun to play the game: snake

Computer Choice: water

You win!


## Project Structure

snake-water-gun-game-python
│
├── snake_water_gun_game.py
└── README.md

