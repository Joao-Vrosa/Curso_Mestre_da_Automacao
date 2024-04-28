# Tirando print da tela

import pyautogui as py

# Tirar print da tela inteira
py.screenshot('tela.jpg')

# Tirar print de apenas uma parte da tela
py.screenshot('calculadora.jpg', region=(1354,109, 395, 660))
