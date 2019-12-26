import slack
from config.const import OAUTH_TOKEN, BOT_OAUTH_TOKEN, CHANNEL_ID

client = slack.WebClient(token=OAUTH_TOKEN)


def send_message(message):
    client.chat_postMessage(
        channel=CHANNEL_ID,
        text=message
    )
