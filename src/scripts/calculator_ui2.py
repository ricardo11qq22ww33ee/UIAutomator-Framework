#!/usr/bin/python
# coding=utf-8

"""

"""
import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils
import os
import json
from src.lib.calculator import Calculator


def run(a, op, b, filename="log_calculator.txt"):
    # path to save logs
    cwd_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cwd_path, "..", "..", "qa", "reports", "")
    logger = Logger(filename, path)
    controller = PhoneControl()

    serials = controller.read_serials()
    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i + 1, serials))

        controller.init_device(serials[i])
        device_params = utils.get_device_data(serials[i])
        logger.write_log("Script UI Calculator---------")

        try:
            calculator = Calculator(a, op, b)
            if calculator.valid:
                logger.write_log("Operation: " + a + op + b)
                action(logger, controller, calculator, device_params, a, b, op)
            else:
                logger.error_log("Validation of Inputs Failed")
        except Exception as ex:
            logger.error_log(ex.message)


def action(logger, controller, calculator, params, a, b, op):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button(params['calculator']['text'], params['settings']['className'])
    for i in a:
        if i == "-":
            controller.click_detailed_button(params["-"]["className"], params["-"]["packageName"], params["-"]["description"])
        else:
            controller.click_button(i, params['digit_calculator'])
    controller.click_detailed_button(params[op]["className"], params[op]["packageName"], params[op]["description"])
    for i in b:
        if i == "-":
            controller.click_detailed_button(params["-"]["className"], params["-"]["packageName"],
                                             params["-"]["description"])
        else:
            controller.click_button(i, params['digit_calculator'])
    controller.click_detailed_button(params["="]["className"], params["="]["packageName"], params["="]["description"])
    value = controller.info_select(params["textField_className"], params["calculator_packageName"])
    logger.write_log(calculator.res)
    logger.write_log(value)
    if value == calculator.res:
        time.sleep(1)
        logger.write_log("SUCCESSFUL CALCULATION")
    else:
        time.sleep(1)
        logger.write_log("CALCULATION FAIL")
    controller.click_home()
    logger.end_log()


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run("1", "+", "1")
