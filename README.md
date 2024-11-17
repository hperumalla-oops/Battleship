# Battleship README


## Introduction
Welcome to **Battleship**, a python project replicating the classic children's board game of the same name. The project is set to a single-player mode where you compete against the computer.
Battleship is set is in a sea, a 16x8 grid, where half of the sea
**(8x8)** has your ships strategically located and the other half has your opponents.


Each player has 3 ships-Battleship (4 dot), a submarine (3 dot) and a Cruiser (2 dot), which he needs to place in his sea.
The game aims to make guesses at the position of each other's ships alternatingly. If you guess the coordinates of you opponent's ship correctly, you get a hit, or a single point, or else you miss and it is your opponent's turn.



## Prerequisites


- **Python 3.x**
-  Python Libraries:
  - tkinter
  - Numpy


Install these dependencies with the following code:


```sh
pip install numpy
pip install tk
```


## How to Run the Code


1. **Clone the Repository:**
   ```sh
   git clone https://github.com/me50/hperumalla-oops/project.git
   cd project.py
   ```


2. **Run the Code:**
   Execute the following incantation in your terminal:
   ```sh
   python Batteship.py
   ```


3. **The Game Begins:**
   The game comprises two steps:
   
   - **Step 1:** Setting up your sea, or placing the ships in the most strategic location, making it hard for your opponent to guess its coordinates. Remember, you can only set your ship horizontally or vertically and not on any diagonals.
   
   - **Step 2:** Once you are done with setting your sea, the real game begins, the computer takes a guess at you grid, if it hits your ship a red 'X' appears, else a white 'O' appears on your sea, then you have a go at the computer's sea.


   - **Hint:**  Since the ships are placed horizontally or vertically, once you hit a dot of the ship, the rest of the ship is in the vicinity of the dot!


## Application Workflow


### Step 1: Initialization.
Global Variables:
main_list: Player's ship positions.
ship_sizes: Sizes of the ships (2-dot, 3-dot, 4-dot).
your_sea_buttons and comp_sea_buttons: Grids for the player and computer.
ug: Temporarily stores selected positions during ship placement.
your_score and comp_score: Track scores.
cg: Computer's ship positions.

 ### Step 2: Main Function
GUI Setup: Creates an 8x8 grid for both player and computer.
Instructions: Displays a welcome message with game rules.
Computer Ship Placement: Randomly generates non-overlapping ships.

### Step 3: Ship Placement
Player's Ship Placement:
Player selects positions via clicks.
Validates ships are in a row or column.
Prompts next ship size after a valid placement; errors reset selections.
Computer's Ship Placement:
Automatically generates valid positions for its ships.

### Step 4: Starting the Game
Game Start: Player completes ship placement; computer begins its turn.
Turn Switching: Computer and player take turns attacking grids.

### Step 5: Gameplay
Computer's Turn:
Randomly attacks positions.
Updates score on hits; marks misses.
Enables player's turn afterward.
Player's Turn:
Player clicks to attack computer’s grid.
Updates score on hits; marks misses.
Switches turn to the computer.

### Step 6: End of Game
Win/Loss Check: First to score 9 wins.
Game Over: Displays result and closes the application.
