# coding=utf-8
from subprocess import check_call, check_output
import time
from uiautomator import Device


class PhoneControl:
    def __init__(self, timeout=3):
        self.device = None
        self.serial = ""
        self.time = timeout

    def read_serials(self):
        output = check_output(['adb', 'devices'])
        lines = output.splitlines()
        serials = []
        for i in range(1, len(lines)-1):
            serials.append(lines[i].split()[0])
        return serials

    def init_device(self, serial):
        self.serial = serial
        d = Device(serial)
        self.device = d

    def unlock_phone(self):
        check_call(['adb', '-s', self.serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])
        time.sleep(self.time)

    def click_home(self):
        check_call(['adb', '-s', self.serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
        time.sleep(self.time)

    def click_button(self, text, classname):
        self.device(text=text, className=classname).click()
        time.sleep(self.time)

    def longclick_button(self, text, classname):
        self.device(text=text, className=classname).long_click()
        time.sleep(self.time)

    def button_exists(self, text, classname):
        if self.device(text=text, className=classname).exists:
            return True
        else:
            return False

    def click_detailed_button(self, classname, packagename, description):
        self.device(packageName=packagename, className=classname, description=description).click()
        time.sleep(self.time)

    def detailed_button_exists(self, classname, packagename, description):
        if self.device(packageName=packagename, className=classname, description=description).exists:
            return True
        else:
            return False

    def longclick_detailed_button(self, classname, packagename, description):
        self.device(packageName=packagename, className=classname, description=description).long_click()

    def set_text_textfield(self,  classname, packagename, content):
        self.device(packageName=packagename, className=classname).set_text(content)

