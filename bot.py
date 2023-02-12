import requests

BOT_API_KEY = '6295550677:AAHHdrSxpATGlxkKsVCuiETb_qN_Tpb3SEI'
MY_CHANNEL_NAME = '@mazutuzu'
MY_MESSAGE_TEXT = 'Hello world!'

response = requests.get(f'https://api.telegram.org/bot{BOT_API_KEY}/sendMessage', {
    'chat_id': MY_CHANNEL_NAME,
    'text': MY_MESSAGE_TEXT
})

if response.status_code == 200:
    print('ok')
else:
    print(response.text)  # Do what you want with response