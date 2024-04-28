# "Arrastar" algo para outro lugar

import pyautogui as py
from time import sleep


sleep(2)

for i in range(8):
    # Mover ate uma coordenada
    py.moveTo(1308,237, duration=2)
    # Clicar, arrastar e soltar em uma coordenada
    py.dragTo(905,284, button='left', duration=1.5)
