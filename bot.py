from functools import partial, reduce

import requests
import validators
from flask import Flask, request, abort
from flask_cors import CORS

from config import BOT_URL, OUTLINE_URL

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def outline():
    body = request.get_json()['message']
    url = body['text']
    chat_id = body['chat']['id']
    format_message = partial(_format_response, chat_id)
    send_message = partial(_bot_handler, 'sendMessage')
    bot_response = _compose(send_message, format_message)

    if not validators.url(url):
        error_message = 'invalid url!'
        bot_response(error_message)
        abort(400)

    outlined_url = _get_outline_url(url)
    bot_response(outlined_url)

    return '{}', 200

def _bot_handler(method, data):
    return requests.post(f'{BOT_URL}/{method}', data).json()

def _get_outline_url(url):
    return f'{OUTLINE_URL}/{url}'

def _format_response(chat_id, text):
    return {
        'text': text.encode('utf-8'),
        'chat_id': chat_id
    }

## ref https://stackoverflow.com/a/37557813
_compose = lambda *F: reduce(lambda f, g: lambda x: f(g(x)), F)

