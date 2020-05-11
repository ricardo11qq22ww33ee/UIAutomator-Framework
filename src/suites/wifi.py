import src.scripts.turn_wifi as TurnWifi
import os


def run_suite():
    # here all the test cases are specified
    # TC-003
    TurnWifi.run("ON")
    # TC-004
    TurnWifi.run("OFF")
    TurnWifi.run("ON")


if __name__ == "__main__":
    run_suite()
