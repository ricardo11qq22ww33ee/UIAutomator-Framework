# coding=utf-8
import phonenumbers
import json


def validate_number(number):
    # check for emergency number
    if number == "911":
        return True, number, "Emergency number"
    # check if is national number (Mexico)
    parsed = phonenumbers.parse(number, "MX")
    if parsed.country_code == 52 and phonenumbers.is_possible_number(parsed) and phonenumbers.is_valid_number(parsed):
        return True, parsed.national_number, "National number"
    # else check if is international number
    try:
        parsed = phonenumbers.parse(number, None)
    except:
        return False, None, None
    if phonenumbers.is_possible_number(parsed) and phonenumbers.is_valid_number(parsed):
        return True, "+" + str(parsed.country_code) + str(parsed.national_number), "International number"

    return False, None, None


def read_json(name):
    with open("src/devices/"+name+".json") as json_file:
        data = json.load(json_file)
    return data
