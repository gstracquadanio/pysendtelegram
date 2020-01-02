import os
import sys
import logging
import requests
import textwrap

__SENDTELEGRAM_API_TOKEN__ = "SENDTELEGRAM_API_TOKEN"
__SENDTELEGRAM_CHAT_ID__ = "SENDTELEGRAM_CHAT_ID"


def send_message(max_msg_len: "Max number of characters of a Telegram message" = 4096):
    if (
        os.getenv(__SENDTELEGRAM_API_TOKEN__) is None
        or os.getenv(__SENDTELEGRAM_CHAT_ID__) is None
    ):
        logging.error(
            "{} or {} are not set".format(
                __SENDTELEGRAM_API_TOKEN__, __SENDTELEGRAM_CHAT_ID__
            )
        )
        return -1

    # stubs for api url
    telegram_api_url = "https://api.telegram.org/bot{SENDTELEGRAM_API_TOKEN}/sendMessage".format(
        SENDTELEGRAM_API_TOKEN=os.getenv(__SENDTELEGRAM_API_TOKEN__)
    )

    # stubs for api data
    telegram_api_data = {"chat_id": os.getenv(__SENDTELEGRAM_CHAT_ID__), "text": ""}

    # buffer all stdin messages
    payload = "".join([_ for _ in sys.stdin])

    # wrap text at telegram max length but keeping formatting
    fmt_payload = textwrap.wrap(payload, width=max_msg_len, replace_whitespace=False)

    # send each formatted payload to
    for _ in fmt_payload:
        telegram_api_data["text"] = _
        r = requests.post(telegram_api_url, data=telegram_api_data)

        if r.status_code != requests.codes.ok:
            return -1

    return 0
