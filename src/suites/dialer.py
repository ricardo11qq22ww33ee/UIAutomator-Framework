import src.scripts.dial_number as DialNumber
import src.scripts.dial_number_ui as DialNumberUI


def run_suite(device_version="android9"):
    # here all the test cases are specified
    # you can run specific scripts if ypu want to input manual numbers
    # TC-005
    DialNumber.run(device_version, "4493019556")
    # TC-006
    DialNumber.run(device_version, "asd6c9asd")
    # TC-007
    DialNumber.run(device_version, "+59122794948")
    # TC-008
    DialNumber.run(device_version, "911")
    # TC-009
    DialNumberUI.run(device_version, "4493019556")
    # TC-010
    DialNumberUI.run(device_version, "4kj234hj1")
    # TC-011
    DialNumberUI.run(device_version, "+59177236019")
    # TC-012
    DialNumberUI.run(device_version, "911")


if __name__ == "__main__":
    run_suite()
