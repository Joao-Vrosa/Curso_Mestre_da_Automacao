
import webbrowser as web
import pyautogui as py
from time import sleep


telefones = []

with open('C:/caminho/fones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    

for telefone in telefones:
    web.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(10)
    py.click(1090,275, duration=1)
    sleep(30)
    
    py.click(801,988, duration=1)
    
    py.typewrite('Oi')
    sleep(5)
    py.press('enter')
