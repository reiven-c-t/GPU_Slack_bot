from dotenv import load_dotenv
from config.datapath import ENV_PATH
import os
load_dotenv(ENV_PATH)

MESSAGE_RUN = "RUN"
MESSAGE_STOP = "STOP"
MESSAGE_CHANGE = "CHANGE"
MESSAGE_TEMPLATE = """- RUN: ({run_gpu_ids})
- STOP: {stop_gpu_ids})
- CHANGE
{change_message}
"""
MESSAGE_CHANGE_TEMPLATE = "\t- gpu {gpu_id}: {last_state} -> {current_state}\n"

OAUTH_TOKEN = os.environ["OAUTH_TOKEN"]
BOT_OAUTH_TOKEN = os.environ["BOT_OAUTH_TOKEN"]  # unused yet
CHANNEL_ID = os.environ["CHANNEL_ID"]