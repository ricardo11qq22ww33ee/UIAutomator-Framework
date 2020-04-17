import src.suites.dialer as DialerSuite
import src.suites.wifi as WifiSuite
import os.path


def run_framework():
    my_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(my_path, "qa", "reports", '')

    # here all the suites specified will be ran, to execute all test cases
    # Wifi Suite
    WifiSuite.run_suite("log_wifi.txt", path)
    # Dialer Suite
    DialerSuite.run_suite("log_dialer.txt", path)


if __name__ == "__main__":
    run_framework()
