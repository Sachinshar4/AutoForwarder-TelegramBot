auto_forwarder.sample_config import Config
from auto_forwarder.sample_config import Config


class Development(Config):
    API_KEY = "8220844170:AAEmGmcf_-aDHlM-ibTjwpPcXstZGajPRoM"  # My bot API key
    OWNER_ID = 6436766847  # My user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-https://t.me/latestupsc1/3]  # List of chat id's to forward messages from.
    TO_CHATS = [-@Mishra0078, 1234567890]  # List of chat id's to forward messages to.
    
    WORKERS = 4
if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "8220844170:AAEmGmcf_-aDHlM-ibTjwpPcXstZGajPRoM-M"  # API key obtained from BotFather
    OWNER_ID = "6436766847"  # If you dont know, run the bot and do /id in your private chat with the bot

    # FOR AUTOMATICALLY FORWARDING MESSAGES
    FROM_CHATS = [-https://t.me/latestupsc1/3 ]  # List of chat id's to forward messages from
    TO_CHATS = [-@Mishra0078]  # List of chat id's to forward messages to

    # FOR WEBHOOKS
    WEBHOOK = False
    IP_ADDRESS = "152.58.75.188"  # Use "0.0.0.0" if using Heroku
    URL = http://t.me/Autoforwordgroupbot # The URL that the bot should listen to for updates
    PORT = 8080  # Port to listen on for webhooks
    CERT_PATH = None  # Path to certificate file

    WORKERS = 4  # Depends on usage, 4 by default


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
