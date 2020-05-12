# Environment

Los detalles del environment se encuentran en el documento del Test Plan

## Prerrequisitos

-Debe haber un acceso directo en el home del telefono, donde se pueda abrir las siguientes aplicaciones:

- Phone
- Calculator
- Settings

-Se debe agregar el serial del telefono al documento src/devices/device_compatibility.json, especificando que version de Android
utilizar. 


-Las versiones de Android son representadas el los .json de src/devices. Estos contienen los detalles de los objetos, dependiendo
de la version. Si se desea agregar compatibilidad para una nueva version, se debe implementar ese json correspondiente, con
los nombres de uiautomator necesarios.