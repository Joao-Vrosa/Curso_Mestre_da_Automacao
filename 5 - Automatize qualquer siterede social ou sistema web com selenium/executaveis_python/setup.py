import sys
import os
from cx_Freeze import setup, Executable


# Usuário deve baixar e instalçar o Google Chrome
# Passar a pasta que contem o executavel para o usuário
# Ferramenta para gerar o executavel: pip install cx-freeze


# Definir o que deve ser incluído na pasta final (arquivos ou pastas)
arquivos = ['dados.txt', 'musicas/']

# Saida de arquivos
configuracao =  Executable(
    script='app.py', # Código principal
    icon='rede.ico' # Icone do app
)

# Configurar o executavel
setup(
    name='Automatizador de Login', # Nome do app
    version='1.0', # Versão
    description='Este programa automatiza o login deste site', # Descrição do app
    author='Joao Rosa', # Autor
    options={'build_exe':{
        'include_files': arquivos, # Incluindo os arquivos ou pastas (DEPENDENCIAS)
        'include_msvcr': True # Se o executavel rodar em Windows, deve ser inserido este parametro para que o executavel rode sem a instalação do Python
    }},
    executables=[configuracao]
)
