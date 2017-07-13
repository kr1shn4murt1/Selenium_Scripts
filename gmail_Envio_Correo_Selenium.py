# -*- coding: utf-8 -*-
# Autor: @kr1shn4murt1
# Fecha: Julio 11 2017
# Este script se loguea a gmail y envia un correo asi mismo

########################## Inicia Login  ####################

import time
from selenium import webdriver
# Libreria importada paras simular el enter
from selenium.webdriver.common.keys import Keys

url_Correo= 'https://gmail.com'
email= 'pruebas@gmail.com'
password= 'password' 

browser= webdriver.Firefox()
browser.get(url_Correo)


# Condicion que espera que los campos de login sean visibles
time.sleep(2)

# Se declara el punto de entrada de correo, 
campo_Correo= browser.find_element_by_xpath("id('identifierId')")
campo_Correo.send_keys(email)
campo_Correo.send_keys(Keys.RETURN)

time.sleep(2)
# Se declara el punto de entrada de password
campo_Password= browser.find_element_by_xpath("id('password')/div[1]/div/div[1]/input")
campo_Password.send_keys(password)
campo_Password.send_keys(Keys.RETURN)

time.sleep(5)
########################## Termina Login  ####################

# Darle click al boton "compose" para redactar un nuevo correo
# Se declara el boton compose
link= browser.find_element_by_xpath("//div[@gh='cm']")
# Se le da click al boton compose
link.click()

# Darle tiempo de nuevo a la pagina para que cargue el html
time.sleep(2)

# Se declara el campo de correo destinatario
campo_Para= browser.find_element_by_xpath("//textarea[@aria-label='To']")
# Se llena con el correo seguridad@india.com
campo_Para.send_keys(email)

# Se declara el campo asunto
campo_Asunto= browser.find_element_by_xpath("//input[@name='subjectbox']")
# Se llena el campo con el asunto
campo_Asunto.send_keys("correo de prueba selenium")

cuerpo_Mensaje= browser.find_element_by_xpath("//div[@aria-label='Message Body']")
cuerpo_Mensaje.send_keys("Correo de prueba enviado para demostrar la funcionalidad de selenium")

# Dar click a enviar
browser.find_element_by_xpath("//div[@aria-label='Send ‪(Ctrl-Enter)‬']").click()

time.sleep(2)
browser.refresh()

time.sleep(5)
#print browser.page_source
# guardar pantallazo
browser.save_screenshot("mail.png")


admin/login.php

user=admin&pass=Segura_2017&tokenanticrsf&















