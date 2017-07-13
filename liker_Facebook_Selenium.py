# -*- coding: utf-8 -*-
# Autor: @kr1shn4murt1
# Fecha: Julio 11 2017
# Este script se loguea a facebook y da like a
# todas las fotos del yogui Jani Jaatinen @gokulacandra

########################## Inicia Login  ####################

import time
from selenium import webdriver
# Libreria importada paras simular el enter
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

body= driver.find_element_by_xpath('//body')
body.send_keys(Keys.PAGE_DOWN)

time.sleep(2)

def dar_Like():
	# Se define el link del like
	like= driver.find_element_by_xpath("id('fbPhotoSnowliftFeedback')/div/div[1]/div/div/div/div/div/span[1]/div/a")
	# Se verifica si no se le ha dado like a la foto
	if like.get_attribute('aria-pressed')== "false":
		# Se da click a like
		like.click()

def click_Siguiente():
	siguiente= driver.find_element_by_xpath("id('photos_snowlift')/div[2]/div/div[1]/div[1]/div[1]/a[2]/i")
	siguiente.click()
	time.sleep(2)

driver.get('https://www.facebook.com/photo.php?fbid=10154660342821512&set=pb.689476511.-2207520000.1499811097.&type=3&theater')
time.sleep(2)
like= driver.find_element_by_xpath("id('fbPhotoSnowliftFeedback')/div/div[1]/div/div/div/div/div/span[1]/div/a")

# Like a la primera foto, de aqui en adelante 
#se hace un ciclo
dar_Like()

# se le da click a la siguiente foto hasta pasar por todas
while True:
	click_Siguiente()
	dar_Like()


# mostrar ventana de alert javascript, se ejecuta pero
# genera error en la ejecucion del script
#driver.execute_script("alert('Saludos terricola');")




















