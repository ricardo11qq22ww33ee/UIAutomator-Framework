import src.scripts.turn_wifi_on as WifiOn
import src.scripts.turn_wifi_off as WifiOff


def run_suite(device_version="android9"):
    # here all the test cases are specified
    # TC-003
    WifiOff.run(device_version)
    # TC-004
    WifiOff.run(device_version)
    # TC-001
    WifiOn.run(device_version)
    # TC-002
    WifiOn.run(device_version)


if __name__ == "__main__":
    run_suite()
