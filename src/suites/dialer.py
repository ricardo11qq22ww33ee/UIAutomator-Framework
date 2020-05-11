import src.scripts.dial_number as DialNumber
import src.scripts.dial_number_ui as DialNumberUI


def run_suite():
    # here all the test cases are specified
    # you can run specific scripts if you want to input manual numbers
    # TC-005
    DialNumber.run("4491963704")
    # TC-006
    DialNumber.run("52 55 90458901")
    # TC-007
    DialNumber.run("+525590458901")
    # TC-008
    DialNumber.run("0019567788720")
    # TC-009
    DialNumber.run("*666g")
    # TC-010
    DialNumber.run("449Q120032")
    # TC-011
    DialNumber.run("SDJBFGALSJHKFGB")
    # TC-012
    DialNumber.run("1234567890123456")
    # TC-013
    DialNumber.run("911")
    # TC-014
    DialNumber.run("*666")
    # TC-015
    DialNumber.run("9a1")
    # TC-016
    DialNumber.run("1")
    # TC-017
    DialNumber.run("+")
    # TC-018
    DialNumber.run("")
    # TC-019
    DialNumberUI.run("4491963704")
    # TC-020
    DialNumberUI.run("52 55 90458901")
    # TC-021
    DialNumberUI.run("+525590458901")
    # TC-022
    DialNumberUI.run("0019567788720")
    # TC-023
    DialNumberUI.run("*666g")
    # TC-024
    DialNumberUI.run("449Q120032")
    # TC-025
    DialNumberUI.run("SDJBFGALSJHKFGB")
    # TC-026
    DialNumberUI.run("1234567890123456")
    # TC-027
    DialNumberUI.run("911")
    # TC-028
    DialNumberUI.run("*666")
    # TC-029
    DialNumberUI.run("9a1")
    # TC-030
    DialNumberUI.run("1")
    # TC-031
    DialNumberUI.run("+")
    # TC-032
    DialNumberUI.run("")


if __name__ == "__main__":
    run_suite()
