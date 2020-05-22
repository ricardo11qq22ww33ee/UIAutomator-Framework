import src.suites.dialer as DialerSuite
import src.suites.wifi as WifiSuite
import src.suites.calculatorapp as CalculatorSuite
from src.lib.logger import Logger
import src.suites.twilio as twilio
import os.path


def run_framework():
    cwd_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cwd_path, "qa", "reports", "")
    logger = Logger("logger_suite.txt", path)
    # here all the suites specified will be ran, to execute all test cases
    # Wifi Suite
    WifiSuite.run_suite()
    # Dialer Suite
    DialerSuite.run_suite()
    # Calculator Suite
    CalculatorSuite.run_suite()
    # Twilio Suite
    twilio.run_suite()
    logger.end_suit()


if __name__ == "__main__":
    run_framework()
