# Quebrando captcha

import pyautogui as py
from time import sleep

sleep(2)
captcha = py.locateCenterOnScreen('C:/Users/João/Desktop/Mestre_da_Automacao/Automatize qualquer sistema ou programa com essa tecnologia/13 - Como quebrar captcha com reconhecimento de imagem/captcha_img.png')

py.click(captcha[0], captcha[1], duration=2)
