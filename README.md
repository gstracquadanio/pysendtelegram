# sendtelegram

Current version: 0.2.0

A Telegram replacement for sendmail.

`sendtelegram` uses a Telegram bot to send messages to a specific user. It reads from `stdin`, splits the input text into messages of at most MAX_MSG_LEN
characters (default: 4096) and send them
using the Telegram API.

`sendtelegram` adheres to the 12 factor principles to manage settings.

It requires two environment variables:
* SENDTELEGRAM_API_TOKEN: the Telegram API token.
* SENDTELEGRAM_CHAT_ID: id of the chat between the bot and the target user.


## Usage

```
usage: sendtelegram [-h] [-m MAX_MSG_LEN]

optional arguments:
  -h, --help            show this help message and exit
  -m MAX_MSG_LEN, --max-msg-len MAX_MSG_LEN
                        Max number of characters of a Telegram message (default: 4096)
```

## Examples

Sending a text file as a telegram message:
```
cat README.md | sendtelegram
```

## Author

* Giovanni Stracquadanio, giovanni.stracquadanio@ed.ac.uk
