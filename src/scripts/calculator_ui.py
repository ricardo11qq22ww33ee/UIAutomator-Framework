#!/usr/bin/python
# coding=utf-8

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
    controller = PhoneControl(1)

    serials = controller.read_serials()
    for i in range(len(serials)):
        logger.write_log(" Device {} = {}".format(i + 1, serials))

        controller.init_device(serials[i])
        device_params = utils.get_device_data(serials[i])
        logger.write_log("Script UI Calculator -----------------")

        try:
            calculator = Calculator(a, op, b)
            if calculator.valid:
                logger.write_log("Operation: " + a + op + b)
                action(logger, controller, calculator, device_params)
            else:
                logger.error_log("Validation of Inputs Failed")
        except SyntaxError as ex:
            logger.end_log(ex.message)
        except ValueError as ex:
            logger.end_log(ex.message)
        except TypeError as ex:
            logger.end_log(ex.message)
        except ZeroDivisionError as ex:
            logger.end_log(ex.message)
        except Exception as ex:
            logger.error_log(ex.message)


def action(logger, controller, calculator, params):
    controller.unlock_phone()
    controller.click_home()
    controller.click_button(params['calculator']['text'], params['calculator']['className'])
    # empty calculator, depending on the state

    # calculator has a previous result saved
    if controller.detailed_button_exists(params['calculator_clear']['className'], params['calculator_clear']['packageName'], params['calculator_clear']['description']):
        controller.longclick_detailed_button(params['calculator_clear']['className'], params['calculator_clear']['packageName'],
                                             params['calculator_clear']['description'])
    # calculator has non processed input
    if controller.detailed_button_exists(params['calculator_delete']['className'], params['calculator_delete']['packageName'], params['calculator_delete']['description']):
        controller.longclick_detailed_button(params['calculator_delete']['className'],
                                             params['calculator_delete']['packageName'], params['calculator_delete']['description'])
        controller.clear_text_textfield(params['calculator_delete']['className'],
                                        params['calculator_delete']['packageName'])
    for i in calculator.number1:
        if i == "-":
            controller.click_detailed_button(params["-"]["className"], params["-"]["packageName"],
                                             params["-"]["description"])
        else:
            controller.click_button(i, params['digit_calculator'])

    controller.click_detailed_button(params[calculator.operator]["className"], params[calculator.operator]["packageName"],
                                     params[calculator.operator]["description"])
    for i in calculator.number2:
        if i == "-":
            controller.click_detailed_button(params["-"]["className"], params["-"]["packageName"],
                                             params["-"]["description"])
        else:
            controller.click_button(i, params['digit_calculator'])
    controller.click_detailed_button(params["="]["className"], params["="]["packageName"], params["="]["description"])
    result = controller.get_text_textfield(params["calculator_textfield"]["className"],
                                           params["calculator_textfield"]["packageName"])

    # validate result
    if calculator.validate_result(result):
        logger.write_log("VALID RESULT: " + str(calculator.res))
        logger.end_log()
    else:
        logger.error_log("Results don't match")

    controller.click_home()


# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # manual input
    run("2", "/", "3616431")