import src.scripts.dial_number as DialNumber
import src.scripts.dial_number_ui as DialNumberUI


def run_suite(filename, path):
    # here all the test cases are specified
    # you can run specific scripts if ypu want to input manual numbers
    # TC-005
    DialNumber.run(filename, path, "4493019556")
    # TC-006
    DialNumber.run(filename, path, "asd6c9asd")
    # TC-007
    DialNumber.run(filename, path, "+59122794948")
    # TC-008
    DialNumber.run(filename, path, "911")
    # TC-009
    DialNumberUI.run(filename, path, "4493019556")
    # TC-010
    DialNumberUI.run(filename, path, "4kj234hj1")
    # TC-011
    DialNumberUI.run(filename, path, "+59177236019")
    # TC-012
    DialNumberUI.run(filename, path, "911")


if __name__ == "__main__":
    run_suite("log_dialer.txt", "../../qa/reports/")
