
from twilio.rest import Client
from src.lib.logger import Logger
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure


def run(number_to=None, number_from=None, filename="log_twilio.txt"):
    # path to save logs
    path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path, "..", "..", "qa", "reports", "")
    # instantiate logger to save a report file
    logger = Logger(filename, path)
    logger.write_log("Script Twilio Voice Mail  ---------")
    try:
        action(logger, number_to, number_from)
    except Exception as ex:
        logger.end_log(ex.message)


def action(logger, number_to, number_from):
    account_sid = 'ACc86884f6d8841e6497873914ab28de99'
    auth_token = '950cc4c17493774642b1c4ef7243c9c2'
    client = Client(account_sid, auth_token)
    try:
        call = client.calls.create(
                                machine_detection='Enable',
                                method='GET',
                                status_callback='http://123f25d0.ngrok.io/response',
                                status_callback_event=['initiated', 'answered', 'completed', 'no-answer', 'queued', 'completed',
                                                       'ringing', 'failed', 'busy'],
                                status_callback_method='POST',
                                url='http://123f25d0.ngrok.io/answer',
                                to=number_to,
                                from_=number_from
            )
    except Exception as ex:
        logger.end_log(ex.message)


    past = call.status
    while ValueError:
        try:
            call = client.calls(call.sid) \
                .update(
                      )
            if past != call.status:
                past = call.status
                if call.status == 'completed':
                    print(call.answered_by)
                    if call.answered_by == "human":
                        logger.end_log("The person you want to contacted answered the call")
                        break
                    elif call.answered_by == "unknown":
                        logger.end_log("The someone you want to contacted answered the message")
                        break
                    else:
                        logger.end_log("The person you want to contacted received the message")
                        break

                elif call.status == 'in-progress':
                    print(call.answered_by)
                    logger.write_log("The call has been answered")

                elif call.status == 'failed':
                    logger.end_log("The call has failed")
                    break

                elif call.status == 'ringing':
                    logger.write_log("The cellphone you want to call is ringing")

                elif call.status == 'queued':
                    logger.write_log("The call has been set")

        except ValueError:
            logger.error_log(ValueError.message)
            print(ValueError)


if __name__ == "__main__":
    run()

