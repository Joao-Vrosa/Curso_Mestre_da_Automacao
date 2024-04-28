from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Opçoes de inicialização do Chrome


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

logo = driver.find_element(By.CLASS_NAME, 'navbar-brand')
links_menu = driver.find_elements(By.CLASS_NAME, 'nav-link')

if logo is not None:
    print('Logo encontrado')
    
if links_menu is not None:
    print('Links Encontrados')
    print(len(links_menu))

input('Pressione uma tecla para fechar: ')
driver.close()
