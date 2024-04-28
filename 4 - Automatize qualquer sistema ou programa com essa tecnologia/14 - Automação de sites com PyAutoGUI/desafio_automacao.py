'''
1) Navegue até o site https://cursoautomacao.netlify.app/
2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
3) Clique em alerta, para gerar a alerta
4) Feche a alerta
5) Suba a página totalmente para cima
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os 
arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
'''

import webbrowser as web
import pyautogui as py
from time import sleep
    

# 1) Navegue até o site https://cursoautomacao.netlify.app/
web.open_new('https://cursoautomacao.netlify.app/')
sleep(2)

# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
py.moveTo(1265,294, duration=0.5)
py.scroll(-500)

sleep(0.5)

campo_nome = py.locateCenterOnScreen('C:/Users/João/Desktop/Mestre_da_Automacao/Automatize qualquer sistema ou programa com essa tecnologia/14 - Automação de sites com PyAutoGUI/CAMPO_NOME.png')
py.click(campo_nome[0], campo_nome[1], duration=0.5)
py.typewrite('Joao')

# 3) Clique em alerta, para gerar a alerta
campo_botao_alerta = py.locateCenterOnScreen('C:/Users/João/Desktop/Mestre_da_Automacao/Automatize qualquer sistema ou programa com essa tecnologia/14 - Automação de sites com PyAutoGUI/CAMPO_BOTAO_ALERTA.png')
py.click(campo_botao_alerta[0], campo_botao_alerta[1], duration=0.5)

# 4) Feche a alerta
py.click(1178,203, duration=1) # O reconhecimento da imagem do botao nao funcionou
# botao_fechar_alerta = py.locateCenterOnScreen('C:/Users/João/Desktop/Mestre_da_Automacao/Automatize qualquer sistema ou programa com essa tecnologia/14 - Automação de sites com PyAutoGUI/BOTAO_FECHAR_ALERTA.png')
# py.click(botao_fechar_alerta[0], botao_fechar_alerta[1], duration=0.5)

# 5) Suba a página totalmente para cima
py.scroll(2000)
sleep(0.5)

# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os 
# arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
py.scroll(-1700)

# Fazer download Excel
py.click(346,816, duration=1)
sleep(1)
# Clicar em salvar
py.click(745,573, duration=1)

sleep(1)

# Fazer download PDF
py.click(554,812, duration=1)
sleep(1)
# Clicar em salvar
py.click(745,573, duration=1)


# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
py.alert(text='VOCÊ TERMINOU!', title='Automacao de Site', button='Continuar')
