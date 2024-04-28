from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Opções de inicialização do Chrome
# Utilizáveis:
# from random import randint # Trabalhar com geração aleatória de dados
# from time import sleep # Trabalhar com tempo (data e horas)
# from selenium.webdriver.support.select import Select # Permite interagir com Dropdown
# from selenium.webdriver.common.keys import Keys # Usar teclas do teclado


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


#  Um código JavaScript. O Python roda o código JS no navegador

def scrollar_final_da_pagina():
    # Scrollar ate o fim da pagina
    scroll = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    return scroll


def scrollar_topo_da_pagina():
    # Scrollar ate o topo da pagina
    scroll = driver.execute_script("window.scrollTo(0, document.body.scrollTop);")

    return scroll


def scrollar_para_descer(pixel):
    # Scrollar X quantidade de pixel(descer)
    scroll = driver.execute_script(f'window.scrollTo(0, {pixel});')

    return scroll


def scrollar_para_subir(pixel):
    # Scrollar X quantidade de pixel(subir)
    scroll = driver.execute_script(f'window.scrollTo(0, -{pixel});')

    return scroll


def clicar_elemento(driver, by, value, tempo_limite_espera=30):
    """
    Função criada para clicar em um elemento somente quanto ele estiver clicavel, em um periodo de 30 segundo.

    clicar_elemento(driver, By.XPATH, 'VALOR')
    """
    try:
        wait = WebDriverWait(driver, tempo_limite_espera)

        # Aguardar até que o elemento seja clicável
        elemento = wait.until(EC.element_to_be_clickable((by, value)))

        # Clicar no elemento
        elemento.click()

        return elemento

    except TimeoutException as te:
        print(f'Tempo limite de espera ({tempo_limite_espera}s) atingido. Elemento não clicável.')

        raise te

    except NoSuchElementException as nse:
        print(f'Elemento não encontrado. Estratégia: {by}, Valor: {value}')

        raise nse
