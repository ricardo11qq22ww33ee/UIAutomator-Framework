#!/usr/bin/python
# coding=utf-8

"""

"""
import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils
import os


def run(number=None, filename="log_dialer.txt"):
    # path to save logs
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "..", "..", "qa", "reports", "")
    logger = Logger(filename, path)

    controller = PhoneControl()

    serials = controller.read_serials()

    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i + 1, serials))

        controller.init_device(serials[i])
        device_params = utils.get_device_data(serials[i])

        logger.write_log("Script Dial Number UI---------")
        if number is None:
            n = raw_input("Enter the number to dial : ")
        else:
            n = number
        try:
            dialable, parsedNumber, msg = utils.validate_number(n)
            if dialable:
                logger.write_log(msg + " " + str(parsedNumber))
                action(logger, controller, parsedNumber, device_params)
            else:
                logger.end_log("Invalid phone number")
        except Exception as ex:
            logger.error_log(ex.message)


def action(logger, controller, number, params):
    controller.unlock_phone()
    controller.click_home()
    controller.click_detailed_button(params["phone"]["className"], params["phone"]["packageName"], params["phone"]["description"])
    if controller.detailed_button_exists(params['key-pad']['className'], params['key-pad']['packageName'],
                                         params['key-pad']['description']):
        controller.click_detailed_button(params['key-pad']['className'], params['key-pad']['packageName'],
                                         params['key-pad']['description'])
    controller.longclick_detailed_button(params['backspace']['className'], params['backspace']['packageName'],
                                         params['backspace']['description'])
    for digit in str(number):
        if digit.isdigit():
            controller.click_button(digit, params['digit_className'])
        elif digit == "+":
            controller.longclick_button("0", params['digit_className'])
        else:
            logger.error_log("Dialing Error")
            return
    controller.click_detailed_button(params['dial']['className'], params['dial']['packageName'], params['dial']['description'])
    if controller.detailed_button_exists(params['hang']['className'], params['hang']['packageName'],
                                         params['hang']['description']):
        time.sleep(1)
        logger.write_log("SUCCESSFUL CALL")
        controller.click_detailed_button(params['hang']['className'], params['hang']['packageName'],
                                         params['hang']['description'])
        logger.end_log()
    else:
        logger.error_log("CALL FAILED")
    controller.click_home()



# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run()
