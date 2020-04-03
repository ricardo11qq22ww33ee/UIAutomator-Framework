#!/usr/bin/python
# coding=utf-8

"""

"""
from subprocess import check_call, check_output
import time
import datetime
import argparse
from uiautomator import Device
import pytz

#---------------------------------------------------------

def readserial():

    output = check_output(['adb', 'devices'])

    lines = output.splitlines()
    firstDev = lines[1].split()[0]
    print ("1st Device on List = {}".format(firstDev))

    return firstDev

def settings_wifi(device,serial):
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])

    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)

    # Settings
    d(text='Settings', packageName='com.motorola.launcher3').click()
    time.sleep(3)

    # Network
    d(text='Network & internet', className='android.widget.TextView').click()
    time.sleep(3)

    # Wifi
    d(text='Wi‑Fi', className='android.widget.TextView').click()
    time.sleep(3)

    if d(text='OFF', className='android.widget.Switch').exists:
        time.sleep(1)
        print("Status: Wifi Off")
        d(text='OFF',className='android.widget.Switch').click()
        time.sleep(5)
        if d(text='ON',className='android.widget.Switch').exists:
            print("Wi-Fi ON --- Turned On")
    else:
        print("Wi-Fi already ON - No need Turn on")
    time.sleep(5)

    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)

    return


#---------------------------------------------------------------------------

if __name__ == "__main__":

    firstserial = readserial()

    start_ts = datetime.datetime.now()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    print('test start:  %s '%start_ts_pst)
    print('serial: %s' % firstserial)

    serial=firstserial #args.serial

    try:
        d = Device(serial)

        print("Script Wifi On---------")
        settings_wifi(d,serial)
        time.sleep(5)



    except Exception as ex:
        print(ex)
    finally:

        #stf_dev.release_device()
        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("-------------RESULTS  -------------------------------------------")
        print('test start:  %s' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)