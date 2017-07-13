# -*- coding: utf-8 -*-
# Autor: @kr1shn4murt1
# Fecha: Julio 11 2017
# Este script se loguea a facebook y visualiza
# todas las Fotos del yogui Jani Jaatinen @gokulacandra

########################## Inicia Login  ####################

import time
from selenium import webdriver
# Libreria importada para simular el enter
from selenium.webdriver.common.keys import Keys

url_Objetivo= 'https://www.facebook.com'
email= 'pruebas@gmail.com'
password= 'password' 

driver= webdriver.Firefox()
driver.get(url_Objetivo)


# Condicion que espera que los campos de login sean visibles
time.sleep(2)

# Se declara el punto de entrada de correo, 
campo_Correo= driver.find_element_by_xpath("//input[@id='email']")

# Se declara el punto de entrada de password
campo_Password= driver.find_element_by_xpath("//input[@id='pass']")

campo_Correo.send_keys(email)
campo_Password.send_keys(password)
campo_Password.send_keys(Keys.RETURN)

time.sleep(5)
########################## Termina Login  ####################

campo_Busqueda= driver.find_element_by_xpath("//input[@aria-label='Search']")
campo_Busqueda.send_keys("jani jaatinen")
campo_Busqueda.send_keys(Keys.ENTER)

time.sleep(2)
driver.get("https://www.facebook.com/jani.jaatinen")

time.sleep(2)
driver.get("https://www.facebook.com/jani.jaatinen/photos?pnref=lhc")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

