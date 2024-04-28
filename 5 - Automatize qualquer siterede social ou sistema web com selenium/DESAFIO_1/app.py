from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Opçoes de inicialização do Chrome

'''
Desafio 1
Encontre cada um deste botões usando o que aprendeu e descubra o estado de cada um desses botões
'''


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


def verificar_botao(botao):
    if botao.is_enabled():
        print('Botao esta habilitado')
    else:
        print('Botao esta desabilitado')

    

botao_um = driver.find_element(By.XPATH, '//button[@class="btn btn-info"]')
botao_dois = driver.find_element(By.XPATH, '//button[@class="btn2 btn btn-dark"]')
botao_tres = driver.find_element(By.XPATH, '//button[@class="btn2 btn btn-warning"]')

verificar_botao(botao_um)
verificar_botao(botao_dois)
verificar_botao(botao_tres)


input('Pressione uma tecla para fechar: ')
