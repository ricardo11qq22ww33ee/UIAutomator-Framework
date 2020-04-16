# Requisitos del Setup

Estos son los prerequisitos para poder ejecutar el proyecto:

  * Python 2.7
  * Pip package installer
  * Android Debug Bridge (ADB)
  * Android SDK Tools

### Preparacion

Para instalar todas las dependencias, abrir una consola o terminal en el ***root***
del proyecto, y insertar este comando:

`pip install -r requirements.txt`


### Last touches

Para comprobar que el ADB esta instalado correctamente, conectar el telefono en modo debug,  abrir una terminal donde
 se desee y ejecutar el comando: `adb devices`.

Si el setup fue correcto, se mostrara una lista con los dispositivos moviles
conectados al equipo.

