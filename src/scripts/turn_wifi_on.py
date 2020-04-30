#!/usr/bin/python
# coding=utf-8

"""

"""

import time
from src.lib.phone_control import PhoneControl
from src.lib.logger import Logger
import src.lib.utils as utils


def run(device_version, filename="log_wifi.txt", path="../../qa/reports/"):
    # instantiate logger to save a report file
    logger = Logger(filename, path)
    # initiate connection to device(s)
    controller = PhoneControl()
    # use the parameters for specific version
    device_params = utils.read_json(device_version)
    # read the serials
    serials = controller.read_serials()
    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i+1, serials))

        controller.init_device(serials[i])

        logger.write_log("Script Turn Wifi On---------")
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
    if controller.button_exists('OFF', params['switch_className']):
        logger.write_log("Status: Wifi Off")
        controller.click_button('OFF', params['switch_className'])
        if controller.button_exists('ON', params['switch_className']):
            logger.write_log("WIFI TURNED ON")
    else:
        logger.write_log("WIFI ALREADY ON")
    controller.click_home()
    logger.end_log()


if __name__ == "__main__":
    run(device_version="android9")

