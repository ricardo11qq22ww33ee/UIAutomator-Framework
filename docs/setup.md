# Setup requirements

These are the requirements for running this project.

  * Python 2.7
  * Pip package installer
  * Android Debug Bridge (ADB)
  * Android SDK Tools

### Preparation

Before running the project, be sure to open a terminal in the root of the project and 
run 

`pip install -r requirements.txt`

to install the required python modules.


### Last touches

To ensure that the Android Tools are working, plugin the phone, enable
USB debugging and in a terminal run `adb devices`.

If the setup is correct, it will show the connected phone with it's serial.

Finally, make sure that the phone does not have any Lock-screens enabled.

