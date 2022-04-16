from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import urllib
import os

locale = os. getcwd()
path_midia = 'logo.png'
midia_send = f'{locale}/userdate/midia/{path_midia}'

contatos = open('userdate\\config\\Numeros.txt','r')
lst = []
linhas = contatos.readlines()
for linha in linhas:
        lst.append(linha)

path = 'userdate\\drivers'
opts = Options()
opts.add_argument('--disable-blink-features=AutomationControlled')
opts.add_argument(f"--user-data-dir={locale}\\userdate\\navegador")
manager = ChromeDriverManager(path=path)
driver = webdriver.Chrome(service=Service(manager.install()),chrome_options=opts)
driver.get('https://web.whatsapp.com/')
print('ESCANEIE O QR CODE!')

while len(driver.find_elements_by_id('side')) < 1:
    time.sleep(4)

def nave_():
    global mensagem
    global driver
    for x in range(len(lst)):
        texto = urllib.parse.quote("Oi LINDO") #AQUI É ADICIONADO O TEXTO PARA SER ENVIADO.
        driver.get(f'https://web.whatsapp.com/send?phone={lst[x]}&text={texto}')
        while len(driver.find_elements_by_id('side')) < 1:
            time.sleep(3)
        try:
            time.sleep(4)
            driver.find_element_by_xpath('//button[contains(.,"OK")]')
            print('Número invalido')
        except:
            midia_()
            send_()
        
def midia_():
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia_send)
    time.sleep(3)

def send_():
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(Keys.ENTER)
    time.sleep(3)
    
#INICIAR PROJETO!
nave_()
driver.quit()