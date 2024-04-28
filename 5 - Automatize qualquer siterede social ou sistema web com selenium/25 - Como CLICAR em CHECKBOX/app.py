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
driver.get('https://cursoautomacao.netlify.app/')

checkbox_1 = driver.find_elements(By.ID, "acessoNivel1Checkbox")
checkbox_2 = driver.find_elements(By.ID, "acessoNivel2Checkbox")
checkbox_3 = driver.find_elements(By.ID, "acessoNivel3Checkbox")

driver.execute_script('arguments[0].click()', checkbox_1)
driver.execute_script('arguments[0].click()', checkbox_2)
driver.execute_script('arguments[0].click()', checkbox_3)

# Verificando se o checkbox esta selecionado
if checkbox_1.is_selected() == True:
    print('Checkbox selecionado')

input('Pressione uma tecla para fechar: ')
