# PYAUTOGUI - Encontrar e interagir com elementos na tela, com base na sua coordenada.

# POSIÇÃO(X, Y)


## Menos eficiente ##
# Para encontrar a posição na tela você deve:
# 1 - Abrir o terminal e digitar: python
# No python você deve:
# 1 - Digitar a linha de codigo: import pyautogui
# 2 - pyautogui.position() - Ira mostrar a posição atual do mouse/cursor na tela
 
## Mais eficiente ##
# 1 - pyautogui.displayMousePosition()
 
## MELHOR FORMA DE FAZER ##
# No python, digite: from mouseinfo import mouseInfo
# mouseInfo() - Ira abrir uma ferramenta

import pyautogui as py
from time import sleep


sleep(2)

py.click(331,14)
sleep(1)
py.click(638,51)
sleep(1)
py.write('https://mail.google.com/mail/u/0/?pli=1#inbox')
py.press('enter')