# Utilizando o Scroll do mouse

# Página mencionada na aula: https://pt.wikipedia.org/wiki/Brasil

import pyautogui as py
from time import sleep

sleep(2)

py.moveTo(929,591, duration=0.5)
# Scrollar ate secao de historia
py.scroll(-2200)
