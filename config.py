auto_forwarder.sample_config import Config
from auto_forwarder.sample_config import Config


class Development(Config):
    API_KEY = "8220844170:AAEmGmcf_-aDHlM-ibTjwpPcXstZGajPRoM"  # My bot API key
    OWNER_ID = 6436766847  # My user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-https://t.me/latestupsc1/3]  # List of chat id's to forward messages from.
    TO_CHATS = [-@Mishra0078, 1234567890]  # List of chat id's to forward messages to.
    
    WORKERS = 4
