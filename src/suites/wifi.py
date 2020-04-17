import src.scripts.turn_wifi_on as WifiOn
import src.scripts.turn_wifi_off as WifiOff


def run_suite(filename, path):
    # here all the test cases are specified
    # TC-003
    WifiOff.run(filename, path)
    # TC-004
    WifiOff.run(filename, path)
    # TC-001
    WifiOn.run(filename, path)
    # TC-002
    WifiOn.run(filename, path)


if __name__ == "__main__":
    run_suite("log_wifi.txt", "../../qa/reports/")
