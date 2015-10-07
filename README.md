# Telegram Log Handler

A python log handler that sends log messages via a Telegram bot.

## Deployment Instructions

### Bot setup
* create a bot via the [BotFather](https://telegram.me/botfather)
* take note of the bot's `token` provided by the botfather
* add the bot to your contacts and sent it a message
* Use the `getUpdates` API method to retrive your `chat_id`
  * YOu can do that by point your browser at `https://api.telegram.org/bot{token}/getUpdates` and look for an `id` element inside a `chat` element

### Handler setup

* Install TelegramHandler by issuing `pip install git+https://github.com/simonacca/TelegramLogHandler/`  
* use it as shown in the following example

```
import logging
from TelegramHandler import TelegramHandler

logger = logging.getLogger()

streamHandler = logging.StreamHandler()
tgHandler = TelegramHandler('myToken', ['myId'])
logger.addHandler(streamHandler)
logger.addHandler(tgHandler)

logging.error('TestMessage')
```
