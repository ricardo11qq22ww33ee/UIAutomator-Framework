import src.suites.dialer as DialerSuite
import src.suites.wifi as WifiSuite
import os.path


def run_framework():
    # here all the suites specified will be ran, to execute all test cases
    # Wifi Suite
    WifiSuite.run_suite()
    # Dialer Suite
    DialerSuite.run_suite()


if __name__ == "__main__":
    run_framework()
