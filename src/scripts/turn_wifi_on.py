#!/usr/bin/python
# coding=utf-8

"""

"""

import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger


def run(filename, path):
    logger = Logger(filename, path)

    controller = PhoneControl(3)

    serial = controller.read_serial()
    logger.write_log("1st Device on List = {}".format(serial))

    controller.init_device()

    logger.write_log("Script Turn Wifi On---------")
    try:
        action(logger, controller)
        time.sleep(3)
    except Exception as ex:
        logger.error_log(ex.message)


def action(logger, controller):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button('Settings')
    controller.click_button('Network & internet')
    controller.click_button('Wi‑Fi')
    if controller.button_exists('OFF', 'android.widget.Switch'):
        logger.write_log("Status: Wifi Off")
        controller.switch_button('OFF')
        if controller.button_exists('ON', 'android.widget.Switch'):
            logger.write_log("WIFI TURNED ON")
    else:
        logger.write_log("WIFI ALREADY ON")
    controller.click_home()
    logger.end_log()


if __name__ == "__main__":
    run("log_wifi.txt", "../../qa/reports/")

