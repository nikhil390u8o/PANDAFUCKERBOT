from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ASUR_SAMRAJY_NET"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/ASUR_SAMRAJY_NET")
    ],
    [Button.url("• ʀᴇᴘᴏ •", "https://t.me/REPO_679/2")]
]

# List of all bot clients
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

async def start_handler(event):
    AltBot = await event.client.get_me()
    bot_name = AltBot.first_name
    bot_id = AltBot.id
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id} ),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𓆩𝐀𝐒𓆪 ꭙ 𝐉𝐄𝐑𝐑𝐘 ⌯ 𝐊𝐈𝐍𝐆💀 #𝐅𝐔𝐂𝐊𝐄𝐑](tg://openmessage?user_id=7290768963)**\n\n"
    TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
    TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"

    await event.client.send_file(
        event.chat_id,
        "https://t.me/ANIME_HUB6229/75",
        caption=TEXT,
        buttons=START_BUTTON
    )

# --- Callback for "Back" Button ---


# Attach the same /start handler to all bots
for bot in BOTS:
    bot.add_event_handler(start_handler, events.NewMessage(pattern="/start"))
    
