import settings
from winLoseOrDraw import endGame, finish
from game import game

settings.init()

while not settings.stop:
    game()

    endGame()

finish()








