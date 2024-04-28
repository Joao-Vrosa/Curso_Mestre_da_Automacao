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

sleep(2)

# - Clicar em login
campo_login = driver.find_element(By.XPATH, "//a[text()='Login']")
campo_login.click()
sleep(2)

# - Clicar no campo e-mail
campo_email = driver.find_element(By.ID, 'email')
sleep(2)

# - Digitar e-mail
campo_email.send_keys('teste@gmail.com')
sleep(2)

# - Clicar no campo senha
campo_senha = driver.find_element(By.ID, 'senha')
sleep(2)

# - Digitar a senha
campo_senha.send_keys('senhaTeste')
sleep(2)

# - Clicar em enviar
campo_enviar = driver.find_element(By.XPATH, "//button[text()='Enviar']")
campo_enviar.click()


input('Pressione uma tecla para fechar: ')
