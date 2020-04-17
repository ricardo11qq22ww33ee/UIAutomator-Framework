#!/usr/bin/python
# coding=utf-8

"""

"""
from subprocess import check_call, check_output
import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils


def run(filename, path, number=None):

    logger = Logger(filename, path)

    controller = PhoneControl(3)

    serial = controller.read_serial()
    logger.write_log("1st Device on List = {}".format(serial))

    controller.init_device()

    logger.write_log("Script Dial Number UI---------")
    if number is None:
        n = raw_input("Enter the number to dial : ")
    else:
        n = number

    try:
        dialable, parsedNumber, msg = utils.validate_number(n)
        if dialable:
            logger.write_log(msg + " " + str(parsedNumber))
            action(logger, controller, parsedNumber)
        else:
            logger.error_log("Invalid phone number")
    except Exception as ex:
        logger.error_log(ex.message)


def action(logger, controller, n):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button('Phone')
    if controller.detailed_button_exists('android.widget.ImageButton', 'com.google.android.dialer', 'key pad'):
        controller.click_detailed_button('android.widget.ImageButton', 'com.google.android.dialer', 'key pad')
    controller.longclick_detailed_button('android.widget.ImageButton', 'com.google.android.dialer', 'backspace')
    for digit in str(n):
        if digit.isdigit():
            controller.click_button(digit)
        elif digit == "+":
            controller.longclick_button(digit)
        else:
            logger.error_log("Dialing Error")
            return
    controller.click_detailed_button('android.widget.ImageButton', 'com.google.android.dialer', 'dial')
    if controller.detailed_button_exists('android.widget.ImageButton', 'com.google.android.dialer', 'End call'):
        time.sleep(1)
        logger.write_log("SUCCESSFUL CALL")
        controller.click_detailed_button('android.widget.ImageButton', 'com.google.android.dialer', 'End call')

    else:
        logger.write_log("CALL FAILED")
    controller.click_home()
    logger.end_log()


# ---------------------------------------------------------------------------

if __name__ == "__main__":

    run("log_dialer.txt", "../../qa/reports/")
