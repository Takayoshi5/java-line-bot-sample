from flask import Flask, request, abort
from linebot import (
 LineBotApi, WebhookHandler
)
from linebot.exceptions import (
 InvalidSignatureError
)
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage
)

from jinja2 import Markup


app = Flask(__name__)

#環境変数取得
ACCESS_TOKEN = "UZ+z5conaeMKob3IEvw8X65e0GxjwGQBWFXnIjtaBewypYBe2smn+LO3ybUEl73Zk2Vz87O7ALVr71ozL27hZRuy6xa3UDqrd3EQ9fX+1hU8of3+nZKj4rEJmgoD4H5Mrpwrt9qYDEEdGWLmIUK6sgdB04t89/1O/w1cDnyilFU="
SECRET = "0bc2c65b05e01105c74761927968c1cb"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    word = event.message.text # 受け取ったメッセージ
    
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=word))

if __name__ == "__main__":
 app.run()