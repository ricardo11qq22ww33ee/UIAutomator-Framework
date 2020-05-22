import src.scripts.twilio_voicemail as twilio


def run_suite():
    """"
    This method is to run the script with different values
    """

    # test case 54
    twilio.run("+528451020032", "+12074264782")
    # test case 55
    twilio.run("+528451020032", "+12074264782")
    # test case 58
    twilio.run("+528451020031", "+12074264782")
    # test case 59
    twilio.run("+528451020032", "+12074264781")
    # test case 62
    twilio.run("+528451020032", "")
    # test case 63
    twilio.run("", "+12074264782")
    # test case 64
    twilio.run("", "")
    # test case 65
    twilio.run("+528461043690", "+12074264782")
    # test case 68
    twilio.run("+528451020032", "+12074264782")
    # test case 69
    twilio.run("+528451020032", "+12074264782")
    # test case 70
    twilio.run("+528451020032", "+12074264782")
    # test case 75
    twilio.run("+524494934471", "+12074264782")
    # test case 76
    twilio.run("+524494934471", "+12074264782")
    # test case 79
    twilio.run("+524494934473", "+12074264782")
    # test case 80
    twilio.run("+524494934471", "+12074264781")
    # test case 83
    twilio.run("+524494934471", "")
    # test case 84
    twilio.run("", "+12074264782")
    # test case 85
    twilio.run("", "")
    # test case 86
    twilio.run("+528451020323", "+12074264782")
    # test case 89
    twilio.run("+524494934471", "+12074264782")
    # test case 90
    twilio.run("+524494934471", "+12074264782")
    # test case 91
    twilio.run("+524494934471", "+12074264782")


if __name__ == "__main__":
    run_suite()
