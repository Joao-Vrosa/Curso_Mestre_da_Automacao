import pyautogui as py
from time import sleep

# Link para o o jogo: https://www.crazygames.com/game/doge-miner-2

py.moveTo(570,544, duration=3)

sleep(2)

while True:
    py.click(clicks=1000, interval=0.0, button='left', duration=2)
    