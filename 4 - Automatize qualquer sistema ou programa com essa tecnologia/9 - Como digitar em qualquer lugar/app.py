# Escerver no bloco de notas

import pyautogui as py
from time import sleep
import pyperclip # Consegue escrever as mensagens com acentos

def escrever_mensagem(msg):
    pyperclip.copy(msg)
    mensagem = py.hotkey('ctrl', 'v')


# Abrir bloco de notas
py.press('winleft')
sleep(0.5)
py.write('Bloco de Notas')
sleep(0.5)
py.press('enter')

sleep(1.5)

# Acrever no bloco de notas
escrever_mensagem('Automação de escrita e teclado com o Pyautogui')
