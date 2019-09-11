from os import environ
TELEGRAM_URI = environ.get('TELEGRAM_URL', 'https://api.telegram.org')
OUTLINE_URL = environ.get('OUTLINE_URL', 'https://outline.com')
BOT_TOKEN = environ.get('BOT_TOKEN', '<your_token_here>')
BOT_URL = f'{TELEGRAM_URI}/bot{BOT_TOKEN}'
