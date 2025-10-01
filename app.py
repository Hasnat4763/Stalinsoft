from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
from dotenv import load_dotenv
from slack_sdk import WebClient
load_dotenv(".env")
from get_response import get_response


app_token = os.environ.get("APP_TOKEN")
bot_token = os.environ.get("BOT_TOKEN")

app = App(token=bot_token)
client = WebClient(token=bot_token)


@app.event("app_mention")
def handle_mention_event(body, say, logger):
    logger.info(body)
    event = body.get("event", {})
    prompt = event.get("text", "")
    response = get_response(prompt)
    say(blocks = response, text = "GULAG!!!")

if __name__ == "__main__":
    handler = SocketModeHandler(app, app_token)
    handler.start()
