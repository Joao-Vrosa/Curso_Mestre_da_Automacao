from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Opçoes de inicialização do Chrome
# Utilizaveis:
# from random import randint # Trabalar com geração aleatoria de dados
from time import sleep # Trabalhar com tempo (data e horas)
# from selenium.webdriver.support.select import Select # Permite interagir com Dropdown
# from selenium.webdriver.common.keys import Keys # Usar teclas do teclado


def iniciar_driver():
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
driver.get('https://www.facebook.com')

sleep(1)

# Logar na conta teste
email = 'SEU_EMAIL'
senha = 'SUA_SENHA'

campo_email = driver.find_element(By.XPATH, "//input[@id='email']")
campo_email.send_keys(email)

sleep(1)

campo_senha = driver.find_element(By.XPATH, "//input[@id='pass']")
campo_senha.send_keys(senha)

sleep(2)

# Clicar em entrar
botao_entrar = driver.find_element(By.XPATH, "//button[@data-testid='royal_login_button']")
botao_entrar.click()

sleep(5)

# Clicar no botao HOME
botao_home = driver.find_element(By.XPATH, "//a[@aria-label='Página inicial']")
botao_home.click()

sleep(3)

# Clicar em "No que voce esta pensando"
campo_publicacao = driver.find_element(By.XPATH, "//*[contains(text(), 'No que você está pensando, Julio?')]")
campo_publicacao.click()

sleep(1)

# Escrever postagem
campo_mensagem = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
mensagem = 'Goodnight!! PYTHON bot hehe'
campo_mensagem.send_keys(mensagem)

sleep(1)

# Clicar em "Publicar"
campo_publicar = driver.find_element(By.XPATH, "//*[contains(text(),'Publicar')]")
campo_publicar.click()

sleep(5)


input('Pressione uma tecla para fechar: ')
driver.close()
