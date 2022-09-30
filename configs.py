# (c) @RoyalKrrishna

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "12336818"))
    API_HASH = os.environ.get("API_HASH", "de4c34807c8963ba9418e01c7cc15c4c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5462111014:AAGuKNZq6Xc_Xl9oTXLST3k0inOjEo_aNl4")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQAA0zsXR8oiLOX3oseq-EBvLRFU9PaF-LeMzN3gWUvGOs4R_hlxB2p98o6Gkf9rlbtF5OIItP1CnZKA34HiSLDtc5-d-M8p69DvFwz-BdQsVb3g_NteltcOZxAqtyTriTlAfVgNyb66P2sVdLUhu2ow0BfCmNDEcXHcWs2MVvexjY2Emxuvs73ED_QvEAg8Vt1IbGxWM2PIpBTbP2VTELuYoYYdadlfUY4WeOy9cGB4DXAG6TkPdClvRafuOOgmC6rS24iUYct2wDLsqYmOydJhYsX74mVOKW7C2mmpH184iAsbiJWg3YTmnTa-DIqiG0DpElZLLXiiHiKuCzeP91ACAAAAAUQdfasA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001778120240"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdisk_Links_Sender_Bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER","5437750699"))
    FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "-1001557431626")
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/MdiskLinksSearchBot'>Mdisk Search Robo</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

👨‍💻 DEVELOPER: <a href='https://t.me/sigma_male_007'>Lucifer</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/sigma_male_007'>Click Me</a>

If You Want Your Own Bot Like This Then You Can Contact My Father.</b>
"""

    HOME_TEXT = """
<b>Yo! {}😇,

I'm Mdisk Link Search Robo.</a>

I Can Search🔍 Mobiz-Seriez-Shows❗

Just Drop A Name With Correct Spelling And See My Powers ⚡⚡

<a>If You Didn't Found Ur Result, Please Try Requesting Here👉<i>@blackest_harbour</i> </a></b>
"""



    START_MSG = """

<b>Yo! Dear {}😇,

I'm Mdisk Link Search Robo.</a>

I Can Search🔍 Mobiz-Seriez-Showz❗

Just Drop A Name With Correct Spelling And See My Powers ⚡

<a>If You Didn't Found Ur Result Try Requesting Here👉<u> @blackest_harbour <u> </a></b>
"""



