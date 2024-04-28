from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options # Opçoes de inicialização do Chrome

# Opçoes de inicialização do Chrome
chrome_options = Options()
argumentos = ['--leng=pt-BR', '--window-size=500,500', '--incognito']

for argumento in argumentos:
    chrome_options.add_argument(argumento)
    
# Fonte de opções de switches(opções de inicialização) https://peter.sh/experiments/chromium-command-line-switches/

# Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc

# Argumentos mais utilizados
'''
--start-maximized # Inicia maximizado
--lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
--incognito # Usar o modo anônimo
--window-size=800,800 # Define a resolução da janela em largura e altura
--headless # Roda em segundo plano(com a janela fechada) - Pode usar a maquina que nao qubrara a automacao
--disable-notifications # Desabilita notificações
--disable-gpu # Desabilita renderização com GPU
'''

# Uso de configurações experimentais
chrome_options.add_experimental_option('prefs', {
    # Alterar o local padrão de download de arquivos
    'download.default_directory': 'D:\\Storage\\Desktop\\projetos selenium\\downloads',
    # notificar o google chrome sobre essa alteração
    'download.directory_upgrade': True,
    # Desabilitar a confirmação de download
    'download.prompt_for_download': False,
    # Desabilitar notificações
    'profile.default_content_setting_values.notifications': 2,
    # Permitir multiplos downloads
    'profile.default_content_setting_values.automatic_downloads': 1,

})

# Inicializando o webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Navegar até um site
driver.get('https://facebook.com')

input('Pressione uma tecla para fechar: ')
