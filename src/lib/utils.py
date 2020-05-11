# coding=utf-8
import phonenumbers
import json
import os


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
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "..", "devices", "", name + ".json")
    with open(path, 'r') as json_file:
        data = json.load(json_file)
    return data


def get_device_data(serialnumber):
    devices = read_json("device_compatibility")
    if serialnumber in devices:
        device_version = devices[serialnumber]
        return read_json(device_version)
    else:
        raise KeyError(
            'Not compatible with your device. (have you added your device serial to src/devices/device_compatibility.json ?)')


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)
