import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6750957059:AAGU0IED2KUb4k4m4oTpMR2S0MpIONN6g4o")
    API_ID = int(os.environ.get("API_ID", 23990433))
    API_HASH = os.environ.get("API_HASH", "e6c4b6ee1933711bc4da9d7d17e1eb20")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1001864683653")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
