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


### Ultimos detalles

Para comprobar que el ADB esta instalado correctamente, conectar el telefono en modo debug,  abrir una terminal donde
 se desee y ejecutar el comando: `adb devices`.

Si el setup fue correcto, se mostrara una lista con los dispositivos moviles
conectados al equipo.


### Compatibilidad del dispositivo

Para que el framework funcione con su dispositivo, debe asegurarse que su version este implementada.

Para verificar esto:
 
 1. Ejecutar en una terminal ``adb devices``
 2. Copiar el serial perteneciente a su dispositivo.
 3. Ir a la carpeta src/devices. En el archivo device_compatibility.json, agregar su serial especificando el nombre de
    la version a la que pertenece su telefono. Si no existe ninguna, la framework no es compatible.
 
 Versiones compatibles actualmente: android9, huaweiY9



# Ejecucion de los scripts

Despues de habeer cumplido todos los requisitos del setup, abrir una consola o terminal en el ***root*** del proyecto:

### Seleccionar las test suites a ejecutar

Para seleccionar que test suites ejecutar, se debe modificar el archivo **main.py**, para definir las test suites que se desean ejecutar.

```
def run_framework():
    # here all the suites specified will be ran, to execute all test cases
    # Wifi Suite
    WifiSuite.run_suite()
    # Dialer Suite
    DialerSuite.run_suite()
    # Calculator Suite
    CalculatorSuite.run_suite()


if __name__ == "__main__":
    run_framework()

```


### Ejecutar los scripts de la framework

Desde la ***root*** del proyecto ejecutar el comando;

`python main.py`

Esto ejecutara todas las suites que se hayan declarado previamente.


### Ejecutar test suites particulares manualmente

Si se desea, se pueden ejecutar test suites manualmente. Desde la root, ejecutar:

`cd src/suites`

Una vez en el directorio de las suites, se definen los scripts a correr y se definen los inputs. Por ejemplo, para correr la suite de Calculadora:

`python calculatorapp.py`

En este caso, se deben definir los inputs de la calculadora en el archivo *inputs/calculatorapp.txt*
