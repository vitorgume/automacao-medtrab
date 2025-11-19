import os
from dotenv import load_dotenv

load_dotenv(override=False)

USER_PLUG_CHAT = os.getenv("USER_PLUG_CHAT")
PASSWORD_PLUG_CHAT = os.getenv("PASSWORD_PLUG_CHAT")