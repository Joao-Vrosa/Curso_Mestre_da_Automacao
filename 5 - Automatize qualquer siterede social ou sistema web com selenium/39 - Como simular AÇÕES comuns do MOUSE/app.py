from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Opções de inicialização do Chrome
# Utilizáveis:
# from random import randint # Trabalhar com geração aleatória de dados
# from time import sleep # Trabalhar com tempo (data e horas)
# from selenium.webdriver.support.select import Select # Permite interagir com Dropdown
from selenium.webdriver.common.keys import Keys  # Usar teclas do teclado
from funcoes_utilitarios import funcoes_web # Biblioteca particular de funções para automação com Selenium
from selenium.webdriver import ActionChains  # Trabalhar com o mouse


def iniciar_driver():
    # Fonte de opções de switches(opções de inicialização) https://peter.sh/experiments/chromium-command-line-switches/
    # Lista de opções experimentais(nem todas estão documentadas) https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc

    # Argumentos mais utilizados
    """
    --start-maximized # Inicia maximizado
    --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
    --incognito # Usar o modo anônimo
    --window-size=800,800 # Define a resolução da janela em largura e altura
    --headless # Roda em segundo plano(com a janela fechada) - Pode usar a máquina que nao quebrara a automação
    --disable-notifications # Desabilita notificações
    --disable-gpu # Desabilita renderização com GPU
    """
    chrome_options = Options()
    argumentos = ['--leng=pt-BR', '--window-size=1000,800', '--incognito']

    for argumento in argumentos:
        chrome_options.add_argument(argumento)

    # Uso de configurações experimentais
    chrome_options.add_experimental_option('prefs', {
        # Desabilitar a confirmação de download
        'download.prompt_for_download': False,
        # Desabilitar notificações
        'profile.default_content_setting_values.notifications': 2,
        # Permitir multiplos downloads
        'profile.default_content_setting_values.automatic_downloads': 1,

    })

    # Inicializando o webdriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    return driver


# Chamando a funcao para iniciar o driver
driver = iniciar_driver()

# Navegar até um site
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')

botao = funcoes_web.clicar_elemento(driver, By.ID, 'botao-direito')
chain = ActionChains(driver)
chain.context_click(botao).pause(3).send_keys(Keys.DOWN).pause(3).send_keys(Keys.DOWN).pause(3).click().perform()

input('Pressione uma tecla para fechar: ')
driver.close()
