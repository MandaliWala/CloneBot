# Copyright (C) 2024 @jithumon
#
# This file is part of clonebot.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

START_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🆘 Help", callback_data="help_cb"),
            InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/Spider_Man_02"),
        ],
        [
            InlineKeyboardButton("⚠️ Disclaimer", callback_data="disc_str"),
            InlineKeyboardButton("📢 Update Channel", url="https://t.me/DigitalGalaxyHQ"),
        ],
        [
            InlineKeyboardButton(
                "📢 Source Code", url="https://t.me/DigitalGalaxyHQ"
            )
        ],
    ]
)

HELP_KB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🫂 About", callback_data="about"),
            InlineKeyboardButton("⚠️ Disclaimer", callback_data="disc_hel"),
        ],
        [InlineKeyboardButton("🔙 Back", callback_data="start_cb")],
    ]
)

STRT_RET_KB = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Back", callback_data="start_cb")]]
)

HELP_RET_KB = InlineKeyboardMarkup(
    [[InlineKeyboardButton("🔙 Back", callback_data="help_cb")]]
)

STARTMSG = "Hi **[{}](tg://user?id={})**, I am an advanced auto forwarder/clone bot, powered by @DigitalGalaxyHQ.\n\nCheck help for commands.\n\n**To avoid any future complications, please read the disclaimer carefully.**"

DISCL_TXT = """
**Disclaimer:**

__Use of this bot is strictly at your own risk. We are not responsible for any consequences, including but not limited to bans, restrictions, or account termination, that may arise from its usage.
To minimize the risk of account suspension or ban, we strongly advise using this bot on a secondary account. Additionally, we recommend avoid using user sessions.
Please ensure compliance with all applicable terms of service and guidelines of Telegram.
By following these guidelines, you can mitigate potential risks and enjoy the benefits of the bot responsibly.
Happy cloning!
@DigitalGalaxyHQ__
"""

HELPMSG = """
If you can make bot admin in source chats, there is no need to use sessions.

✪ **Clone Commands:**
◆ /index - Index a source chat for cloning. (This helps to omit duplicate files)
__Always try to use bot only to avoid bans.__
◆ /clone - Clone all indexed files to a destination chat.
◆ /total - Get the total count of indexed files.
◆ /cleardb - Delete the entire indexed files in database.
◆ /status - To find if any cloning job is ongoing.

✪ **Forwarder Commands:**
◆ /addchat - Add chat to source and destination - `/addchat SOURCE_CHAT_ID DEST_CHAT_ID`
__eg: `/addchat -10012345111 -100123456112`__
◆ /delchat - Remove chat from source and destination - `/delchat SOURCE_CHAT_ID DEST_CHAT_ID`
__eg: `/delchat -10012345111 -100123456112`__
◆ /listchats - List all active chats.
    
✪ **Regular Commands:**
◆ /restart - Restart the bot.
◆ /logs - Get bot logs.
◆ /server - Get sever & bot stats.
"""


ABT_MSG = """
**About This Bot** 

A Clone/Forwarder Bot with advanced features.

Source Code : [CloneBot](https://t.me/DigitalGalaxyHQ)
Framework : [Pyrogram](https://docs.pyrogram.org)
Language : [Python](https://www.python.org)
Developer : [𝑷𝒆𝒕𝒆𝒓 𝑷𝒂𝒓𝒌𝒆𝒓 🕸](https://t.me/Spider_Man_02)
"""
