# Alertar e pedir algo no pyautogui

import pyautogui as py

py.alert(text='Iniciando sua automacao', title='Automacao Teste', button='Continuar')

email = py.prompt(text='Digite o seu E-mail', title='Dados Obrigadtorios')
print(f'Voce digitou o e-mail: {email}')


resposta = py.confirm(text='Continuar rodando automacao?', title='Confirmacao', buttons=['Sim', 'Nao', 'Cancelar']).upper()

if resposta == 'SIM':
    print('Encerrando automacao')
elif resposta == 'NAO':
    print('Continuando automacao')
else:
    print('Cancelando operacao')


senha = py.password(text='Digite sua senha', title='Login', mask='*')
print(senha)
