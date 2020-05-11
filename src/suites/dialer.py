import src.scripts.dial_number as DialNumber
import src.scripts.dial_number_ui as DialNumberUI


def run_suite():
    # here all the test cases are specified
    # you can run specific scripts if you want to input manual numbers
    # TC-005
    #DialNumber.run("4493019556")
    # TC-006
    #DialNumber.run("asd6c9asd")
    # TC-007
    #DialNumber.run("+59122794948")
    # TC-008
    #DialNumber.run("911")
    # TC-009
    DialNumberUI.run("4493019556")
    # TC-010
    DialNumberUI.run("4kj234hj1")
    # TC-011
    DialNumberUI.run("+59177236019")
    # TC-012
    DialNumberUI.run("911")


if __name__ == "__main__":
    run_suite()
