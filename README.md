# 🦊 Fox and Coin Game 🪙

Welcome to the exciting world of the **Fox and Coin Game**! This is a simple yet thrilling game where you control a fox to collect as many coins as possible within a limited time. The game is built using Python and the Pygame Zero library.

## 🎮 How to Play

The game is straightforward. You control a fox that moves around the screen to collect coins. Each time the fox touches a coin, your score increases by 10 points, and a new coin appears at a random location on the screen. But be quick! You only have 7 seconds to collect as many coins as you can.

## 📝 Code Explanation

Here's a brief overview of what each part of the code does:

- `import pgzrun`: This line imports the Pygame Zero run module, which contains the game loop.

- `width=100` and `height=100`: These lines set the width and height of the game window.

- `game_over = False` and `score = 0`: These lines initialize the game state and the player's score.

- `fox = Actor("fox")` and `coin = Actor("coin")`: These lines create the fox and coin actors (game characters).

- `def draw()`: This function is responsible for drawing the game state onto the screen.

- `def place_coin()`: This function will be used to place the coin at a new location each time it is collected by the fox.

- `def time_up()`: This function sets the game state to over after 7 seconds.

- `def update()`: This function updates the game state. It checks for keyboard input to move the fox and checks for collision between the fox and the coin.

- `pgzrun.go()`: This line starts the game loop.

## 🚀 Get Started

Are you ready to dive into the fun? Just run the Python script and start collecting coins with your fox. Enjoy the game and try to beat your high score!

Remember, the faster you are, the higher your score will be. So, get ready, set, and go! 🚀
