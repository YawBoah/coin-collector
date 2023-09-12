import pgzrun

width=100
height=100


game_over = False  # Boolean variable for game state
score = 0  # Initialize the score

# Create Actors and set their positions
fox = Actor("fox")
fox.pos = (200, 200)

coin = Actor("coin")
coin.pos = (200, 200)

def draw():
    screen.clear()
    
    if not game_over:
        fox.draw()
        coin.draw()
    
    # Display the score
    screen.draw.text("Score: " + str(score), topleft=(10, 10), fontsize=36, color="white")

def place_coin():
    pass  # You'll add logic to place the coin here

def time_up():
    global game_over
    game_over = True

# Set a timer to call time_up() after 7 seconds
clock.schedule(time_up, 7.0)

def update():
    global score, game_over

    if not game_over:
        # Check keyboard input for movement
        if keyboard.left:
            fox.x -= 2
        elif keyboard.right:
            fox.x += 2
        elif keyboard.up:
            fox.y -= 2
        elif keyboard.down:
            fox.y += 2

        # Check for collision between the fox and the coin
        if fox.colliderect(coin):
            score += 10  # Increase the score when the fox touches the coin
            place_coin()  # Place a new coin

        # You can add more game logic here


# Run the game using pgzrun
pgzrun.go()
