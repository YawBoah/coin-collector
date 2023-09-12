import pgzrun

width=400
height=400

score=0

game_over = False

fox = Actor("fox")
fox.pos = (200, 200)

coin = Actor("coin")
coin.pos = (200, 200)

def update():
    pass

def draw():
    screen.clear()
    fox.draw()
    coin.draw()

pgzrun.go()