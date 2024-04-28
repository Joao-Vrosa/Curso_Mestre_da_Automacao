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

driver.maximize_window() # Maximizar a janela
driver.refresh() # Recarrega a pagina atual
driver.get(driver.current_url) # Recarrega a pagina atual
driver.back() # Volta a pagina anterior
driver.forward() # Navega uma vez para frente
print(driver.title) # Obtem o titulo da pagina
print(driver.current_url) # Obtem a URL (endereço) da pagina atual
print(driver.page_source) # Obtem o código fonte da pagina atual

# Obtem o texdo dentro de um alemento
print(driver.find_element(By.XPATH, "//a[@class='navbar-brand']").text)
print(driver.find_element(By.XPATH, "//a[@class='navbar-brand']").get_attribute('href'))


driver.close() # Fecha a janela atual
input('Pressione uma tecla para encerrar: ')
