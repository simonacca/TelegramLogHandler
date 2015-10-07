import logging

class TelegramHandler(logging.Handler):
    """
    A handler class which sends a Telegram message for each logging event.
    """
    def __init__(self, token, ids):
        """
        Initialize the handler.

        Initialize the instance with the bot's token and a list of chat_id(s)
        of the conversations that should be notified by the handler.
        """
        logging.Handler.__init__(self)
        self.token = token
        self.ids = ids

    def emit(self, record):
        """
        Emit a record.

        Format the record and send it to the specified chats.
        """
        try:
            import requests
            requests_handler = logging.getLogger("requests")

            url = 'https://api.telegram.org/bot{}/sendMessage'.format(self.token)

            requests_handler.propagate = False
            for chat_id in self.ids:
                payload = {
                    'chat_id':chat_id,
                    'text': self.format(record)
                }

                requests.post(url, data=payload)
            requests_handler.propagate = True
        except:
            self.handleError(record)
