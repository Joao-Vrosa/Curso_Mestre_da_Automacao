'''
DESAFIO:

Crie um programa que pede o usuario e senha e, na sequencia, copia e cola o suario e senha dentro do bloco de notas

'''

import pyautogui as py

usuario = py.prompt(text='Digite o seu usuario:', title='Login').upper()
senha = py.password(text='Digite a sua senha', title='Login', mask='*')

caminho_da_pasta = 'C:/Users/João/Documents/Python/Mestre_da_Automacao/4 - Automatize qualquer sistema ou programa com essa tecnologia/11 - Como mostrar alertas e pegar dados do usuário para automatizar algo'
nome_do_arquivo = 'usuarios.txt'
caminho_completo = caminho_da_pasta + '/' + nome_do_arquivo


with open(caminho_completo, 'a') as arquivo:
    arquivo.write(f'Usuario: {usuario} | Senha: {senha}\n')
    arquivo.close()
