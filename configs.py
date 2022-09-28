# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -100)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/MdiskLinksSearchBot'>Mdisk Search Robo</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 DEVELOPER: <a href='https://t.me/sigma_male_007'>Aayush</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/sigma_male_007'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact My Father.</b>
"""

    HOME_TEXT = """
<b>Yo! {}😇,

I'm Mdisk Link Search Robo.</a>

I Can Search 🔍 Mobiz-Seriez-Showz❗

Just Drop A Name With Correct Spelling And My Powers ⚡

<a>If You Didn't Found Ur Result Try Requesting Here @blackest_harbour</a></b>
"""



    START_MSG = """

<b>Yo! {}😇,

I'm Mdisk Link Search Robo.</a>

I Can Search 🔍 Mobiz-Seriez-Showz❗

Just Drop A Name With Correct Spelling And My Powers ⚡

<a>If You Didn't Found Ur Result Try Requesting Here @blackest_harbour </a></b>
"""



