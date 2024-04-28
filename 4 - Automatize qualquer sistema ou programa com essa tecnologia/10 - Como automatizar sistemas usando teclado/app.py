# Como usar botoes e atalhos do teclado

import pyautogui as py
from time import sleep

# Clicar no campo e-mail
py.click(1411, 265, duration=2)
sleep(1)
# Digitar email
py.typewrite('teste@gmail.com')
# Apertar tab
py.press('tab')
# Digitar senha
py.typewrite('123456')
# Apertar tab
py.press('tab')
# Apertar space
py.press('space')
