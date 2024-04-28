import pyautogui as py
import keyboard as kb
from time import sleep
import win32api
import win32com


coordenada_coluna_um = 0
coordenada_coluna_dois = 0
coordenada_coluna_tres = 0
coordenada_coluna_quatro = 0

cor_botao_piano = (0,0,0)

coordenada_botao_start = 0


py.click(coordenada_botao_start, duration=1)

# Forma mais rapida de utilzar o click na tela
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32com.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32com.MOUSEEVENTF_LEFTUP,0,0)


# Loop - Quando for precionado a tecla '1' do teclado o loop termina
while kb.is_pressed('1') == False:
    if py.pixelMatchesColor(*coordenada_coluna_um, cor_botao_piano, tolerance=10):
        click(*coordenada_coluna_um)
        sleep(0.05)
        
    if py.pixelMatchesColor(*coordenada_coluna_dois, cor_botao_piano, tolerance=10):
        click(*coordenada_coluna_dois)
        sleep(0.05)
        
    if py.pixelMatchesColor(*coordenada_coluna_tres, cor_botao_piano, tolerance=10):
        click(*coordenada_coluna_tres)
        sleep(0.05)
        
    if py.pixelMatchesColor(*coordenada_coluna_quatro, cor_botao_piano, tolerance=10):
        click(*coordenada_coluna_quatro)
        sleep(0.05)
