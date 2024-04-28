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
driver.get('https://cursoautomacao.netlify.app/')

# Salvar nossa janela atual
janela_inicial = driver.current_window_handle

# Abrir nova janela
driver.execute_script('window,scrollTo(0,500);')
sleep(3)

botao_abrir_aba = driver.find_element(By.XPATH, '//button[contains(text(),"Abrir aba")]')
driver.execute_script('arguments[0].click()', botao_abrir_aba)
sleep(1)

# Verificar quais janelas então abertas
janelas = driver.window_handles
for janela in janelas:
    print(janela)
    
    if janela not in janela_inicial:
        driver.switch_to.window(janela)
        campo_pesquisa = driver.find_element(By.XPATH, "//input[@id='senha']")
        sleep(1)
        
        campo_pesquisa.send_keys('12345')
        sleep(1)
        
        driver.close()
        

driver.switch_to.window(janela_inicial)
        

input('Pressione uma tecla para fechar: ')
driver.close()
