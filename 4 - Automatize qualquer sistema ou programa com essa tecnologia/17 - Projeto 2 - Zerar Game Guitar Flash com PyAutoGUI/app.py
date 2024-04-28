
import pyautogui as py
import keyboard
from time import sleep

# Site: https://guitarflash.com/?lg=pt
# Musica indicada: Somewhere I Belong por Linkin Park - Modo facil

# Verificar se há um botão com a cor correspondente dentro do criculo daquela cor

coordenada_botao_verde = 724,866
coordenada_botao_vermelho = 830,872
coordenada_botao_amarelo = 947,870

sleep(7)

while not keyboard.is_pressed('1'):
    if py.pixelMatchesColor(*coordenada_botao_verde, (0, 150, 0), tolerance=10):
        py.press('a')
        sleep(0.05)

    if py.pixelMatchesColor(*coordenada_botao_vermelho, (248, 0, 0), tolerance=10):
        py.press('s')
        sleep(0.05)

    if py.pixelMatchesColor(*coordenada_botao_amarelo, (244, 244, 2), tolerance=10):
        py.press('j')
        sleep(0.05)
