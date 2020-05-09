#!/usr/bin/python
# coding=utf-8

"""

"""

import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils


def run(device_version, filename="log_wifi.txt", path="qa/reports/"):

    logger = Logger(filename, path)

    controller = PhoneControl()

    device_params = utils.read_json(device_version)

    serials = controller.read_serials()
    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i + 1, serials))

        controller.init_device(serials[i])

        logger.write_log("Script Turn Wifi Off---------")
        try:
            action(logger, controller, device_params)
            time.sleep(3)
        except Exception as ex:
            logger.error_log(ex.message)


def action(logger, controller, params):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button(params['settings']['text'], params['settings']['className'])
    controller.click_button(params['network']['text'], params['network']['className'])
    controller.click_button(params['wi-fi']['text'], params['wi-fi']['className'])
    if controller.button_exists('ON', params['switch_className']):
        logger.write_log("Status: Wifi On")
        controller.click_button('ON', params['switch_className'])
        if controller.button_exists('ON', params['switch_className']):
            logger.write_log("WIFI TURNED ON")
    else:
        logger.write_log("WIFI ALREADY ON")
    controller.click_home()
    logger.end_log()


if __name__ == "__main__":
    run(device_version="android9")

