#!/usr/bin/python
# coding=utf-8

"""

"""
import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils
import os
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
        device_params = utils.get_device_data(controller.version())
        logger.write_log("Script UI Calculator---------")

        try:
            calculator = Calculator(a, op, b)
            if calculator.valid:
                logger.write_log("Operation: " + a + op + b)
                action(logger, controller, calculator, device_params)
            else:
                logger.error_log("Validation of Inputs Failed")
        except Exception as ex:
            logger.error_log(ex.message)


def action(logger, controller, calculator, params):
    controller.unlock_phone()
    controller.click_home()
    logger.write_log(calculator.res)
    controller.click_home()
    logger.end_log()


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    run("1", "+", "1")
