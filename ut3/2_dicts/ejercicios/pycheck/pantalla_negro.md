# Cómo poner la pantalla en negro con atajos de teclado

Para poder poner la pantalla en negro con atajos de teclado, como si simularamos el apagado manual de la pantall debemos crear un script de bash en cualquier carpeta del usuario con el siguiente contenido:

'''
rem #!/bin/bash

xset s blank ; sleep 1 ; xset s activate
'''

Ejecutamos el siguiente comando para otorgar permisos de ejecución al script:

'''

chmod +x "ruta del archivo"

'''

Luego de esto deberemos de acceder a la apliación del sistema ***Teclado -> Atajos de las aplicaciones -> Añadir*** y buscaremos este fichero y crearemos un atajo de teclado con el que nos sintamos cómodos.