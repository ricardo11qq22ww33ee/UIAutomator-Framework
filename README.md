# Ejecucion de los scripts

Este documento indica como se deben ejecutar los scripts.

Antes de comenzar, se requiere que todos los pasos del documento de docs/SETUP.MD hayan sido cumplidos.

Tambien es necesario abrir una consola o terminal en el ***root*** del proyecto.

### Seleccionar las test suites a ejecutar

Para seleccionar que test suites ejecutar, se debe modificar el archivo **main.py**.

```import src.suites.dialer as DialerSuite
import src.suites.wifi as WifiSuite


def run_framework():
    # here all the suites specified will be ran, to execute all test cases
    # Wifi Suite
    WifiSuite.run_suite("log_wifi.txt", "../../qa/reports/")
    # Dialer Suite
    DialerSuite.run_suite("log_dialer.txt", "../../qa/reports/")


if __name__ == "__main__":
    run_framework()
```


### Ejecutar los scripts de la framework

Desde la ***root*** del proyecto ejecutar el comando;

`python main.py`

Esto ejecutara todas las suites que se hayan declarado previamente.


### Ejecutar scripts particulares manualmente

Si se desea, se pueden ejecutar scripts manualmente. Desde la root, ejecutar:

`cd src/scripts`

Una vez en el directorio de los scripts, si por ejemplo quiero ejecutar dial_number con mis propios inputs:

`python dial_number.py`

En este caso, se le solicitara por consola el input del numero con el que se desea realizar la marcacion.

