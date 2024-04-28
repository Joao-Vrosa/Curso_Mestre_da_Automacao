# Navegar ate um site com PyAutoGUI

import webbrowser
from time import sleep

# Abrir uma aba no navegador ou criar outro
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(5)

# Abrir uma nova aba em um navegador existente ou criar outro
webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
sleep(5)

# Criar e abrir uma nova janela do zero
webbrowser.open_new('https://cursoautomacao.netlify.app/')
