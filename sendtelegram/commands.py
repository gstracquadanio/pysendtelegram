import os
import sys
import requests
import textwrap


def send_message(msg_max_len: 'Max char per Telegram message' = 4096):
    # stubs for api url
    telegram_api_url = "https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage".format(
        TELEGRAM_API_TOKEN=os.getenv("TELEGRAM_API_TOKEN")
    )
    # stubs for api data
    telegram_api_data = {"chat_id": os.getenv("TELEGRAM_CHAT_ID"), "text": ""}

    # buffer all stdin messages
    payload = "".join([_ for _ in sys.stdin])

    # wrap text at telegram max length but keeping formatting
    fmt_payload = textwrap.wrap(payload, width=256, replace_whitespace=False)

    # send each formatted payload to
    for _ in fmt_payload:
        telegram_api_data['text'] = _
        r = requests.post(
            telegram_api_url, data= telegram_api_data
        )

        if r.status_code != requests.codes.ok:
            return -1

    return 0
