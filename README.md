# Repositorio de scripts hechos en selenium webdriver

Scripts written in selenium python  - Scripts de selenium python

Herramientas usadas:
http://www.seleniumhq.org/projects/webdriver/ 

Para localizar los elementos a darle click
https://addons.mozilla.org/en-US/firefox/addon/element-locator-for-webdriv/

Como segunda opcion para cuando falla el addon anterior webdriver locator
https://addons.mozilla.org/en-US/firefox/addon/xpath-checker/


# Listado de scripts:

gmail_Envio_Correo_Selenium.py

liker_Facebook_Selenium.py

visualizador_Todas_Las_Fotos_Facebook_Selenium.py

explotacion_SQLi_DVWA_Selenium.py

xss_Explotacion_DVWA_Selenium.py


# Descripcion de los scripts

Para usar los scripts antes deben editarse para cambiar las variables que aparecen en las primeras lineas como por ejemplo
"email", "password" , "url" , etc


* gmail_Envio_Correo_Selenium.py    -> Este script se loguea a gmail via web y se envia un correo asi mismo

* liker_Facebook_Selenium.py        -> Este script se loguea a facebook y le da like a todas las fotos de un perfil

* visualizador_Todas_Las_Fotos_Facebook_Selenium.py -> Este script se loguea a una cuenta de facebook de la cual deben        
                                                       proporcionarse credenciales y visualiza todas las fotos de un perfil
                                                       
* explotacion_SQLi_DVWA_Selenium.py -> Este script se loguea a dvwa y explota la vulnerabilidad SQL injection paso a paso          
                                       extrayendo todos los datos, luego obtiene el texto plano de los hashes

* xss_Explotacion_DVWA_Selenium.py  -> Este script se loguea a DVWA y explota la vulnerabilidad XSS



# Como ejecutar los scripts

1 - Instalar selenium -> pip install selenium

2 - Descargar geckodriver y copiarlo al path c:\windows\system32 -> https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-win32.zip esta version es si se tiene instalado python 32 bits

3 - Editar el script deseado en bloc de notas y cambiar las variables email, password, url que estásn en las primeras lineas de los scripts

4 - Darle doble click al script.py deseado
