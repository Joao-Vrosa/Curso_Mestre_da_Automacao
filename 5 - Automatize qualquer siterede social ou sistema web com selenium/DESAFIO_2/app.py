from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Opçoes de inicialização do Chrome
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    argumentos = ['--leng=pt-BR', '--window-size=800,600', '--incognito']

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
driver.get('https://cursoautomacao.netlify.app/desafios')

# Encontrar o campo nome
campo_nome = driver.find_element(By.ID, 'dadosusuario')

sleep(1)

# Digitar o nome
campo_nome.send_keys('Nome Teste da Silva')

sleep(1)

# Clicar no botao enviar
botao_enviar = driver.find_element(By.ID, 'desafio2')
driver.execute_script('arguments[0].click()', botao_enviar)

sleep(1)

# Digitar nome
campo_nome_escondido = driver.find_element(By.ID, 'escondido')
campo_nome_escondido.send_keys('Nome Teste Escondido da Silva')

sleep(1)

# Clicar em validar
botao_validar = driver.find_element(By.ID, 'validarDesafio2')
driver.execute_script('arguments[0].click()', botao_validar)


input('Pressione uma tecla para fechar: ')
