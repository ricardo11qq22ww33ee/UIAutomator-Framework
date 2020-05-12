import src.scripts.turn_wifi as TurnWifi
import os


def run_suite():
    # here all the test cases are specified
    # TC-001
    TurnWifi.run("OFF")
    # TC-002
    TurnWifi.run("OFF")
    # TC-002
    TurnWifi.run("ON")
    # TC-002
    TurnWifi.run("ON")


if __name__ == "__main__":
    run_suite()
