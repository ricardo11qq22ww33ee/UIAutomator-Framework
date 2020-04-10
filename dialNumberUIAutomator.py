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
import phonenumbers

# ---------------------------------------------------------


def readserial():

    output = check_output(['adb', 'devices'])

    lines = output.splitlines()
    firstDev = lines[1].split()[0]
    print ("1st Device on List = {}".format(firstDev))

    return firstDev


def is_valid_number(number):
    # check for emergency number
    if number == "*666":
        print "Emergency number"
        return True, number
    # check if is national number (Mexico)
    parsed = phonenumbers.parse(number, "MX")
    if parsed.country_code == 52 and phonenumbers.is_possible_number(parsed) and phonenumbers.is_valid_number(parsed):
        print "National number"
        return True, parsed.national_number
    # else check if is international number
    try:
        parsed = phonenumbers.parse(number, None)
    except:
        return False, None
    if phonenumbers.is_possible_number(parsed) and phonenumbers.is_valid_number(parsed):
        print "International number"
        return True, "+" + str(parsed.country_code) + str(parsed.national_number)

    return False, None


def quick_dial(device, serial, number):
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_WAKEUP'])

    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)

    # Phone
    d(text='Phone', packageName='com.motorola.launcher3').click()
    time.sleep(3)

    # Open dialer if its not open
    if d(packageName='com.google.android.dialer', className='android.widget.ImageButton', description='key pad').exists:
        d(packageName='com.google.android.dialer', className='android.widget.ImageButton', description='key pad').click()

    # Clear textbox
    d(packageName='com.google.android.dialer', className='android.widget.ImageButton', description='backspace').long_click()

    # Enter numbers one by one
    for digit in str(number):
        if digit.isdigit():
            d(text=digit, className='android.widget.TextView', packageName='com.google.android.dialer').click()
            time.sleep(1)
        elif digit == "+":
            d(text=digit, className='android.widget.TextView', packageName='com.google.android.dialer').long_click()
            time.sleep(1)
        else:
            print "Call failed: invalid number"
            check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
            return

    # Call
    d(packageName='com.google.android.dialer', className='android.widget.ImageButton', description='dial').click()
    time.sleep(3)

    if d(packageName='com.google.android.dialer', className='android.widget.ImageButton', description='End call').exists:
        time.sleep(1)
        print("Successful call")
        d(packageName='com.google.android.dialer', className='android.widget.ImageButton', description='End call').click()
        time.sleep(3)
    else:
        print "Call failed"

    # home
    check_call(['adb', '-s', serial, 'shell', 'input keyevent', 'KEYCODE_HOME'])
    time.sleep(3)

    return


# ---------------------------------------------------------------------------

if __name__ == "__main__":

    firstserial = readserial()

    start_ts = datetime.datetime.now()
    start_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

    print('test start:  %s '%start_ts_pst)
    print('serial: %s' % firstserial)

    serial = firstserial #args.serial

    try:
        d = Device(serial)
        print("Script Dial Number with UI Automator---------")
        n = raw_input("Enter the number to dial : ")

        dialable, parsedNumber = is_valid_number(n)
        if dialable:
            quick_dial(d, serial, parsedNumber)
        else:
            print "Invalid phone number"
        time.sleep(5)

    except Exception as ex:
        print(ex)
    finally:

        stop_ts = datetime.datetime.now()
        stop_ts_pst = str(datetime.datetime.now(pytz.timezone('US/Pacific')).strftime('"%m-%d-%y %H:%M:%S.%f"'))

        print("-------------RESULTS  -------------------------------------------")
        print('test start:  %s' % start_ts_pst)
        print('test end  :  %s' % stop_ts_pst)