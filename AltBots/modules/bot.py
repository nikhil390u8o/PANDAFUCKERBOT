import sys
import heroku3
from os import execl, getenv
from telethon import events
from datetime import datetime
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
)

# List of all bot clients
ALL_BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]


# 🏓 Ping command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}ping(?: |$)(.*)"))
    async def ping(e):
        if e.sender_id in SUDO_USERS:
            start = datetime.now()
            altron = await e.reply("» __𝐒𝐇𝐎𝐍𝐀𝐐𝐔𝐄𝐄𝐍__")
            end = datetime.now()
            mp = (end - start).microseconds / 1000
            await altron.edit(
                f"__🤖 ᴘɪɴɢ__\n» `αиσиумσυѕ ραρα нєяє αв кιѕкι gαи∂ мαяυ {mp} ᴍꜱ`"
            )


# 🔁 Reboot command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}reboot(?: |$)(.*)"))
    async def restart(e):
        if e.sender_id in SUDO_USERS:
            await e.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
            try:
                await bot.disconnect()
            except Exception:
                pass
            execl(sys.executable, sys.executable, *sys.argv)


# 🧑‍💻 Add sudo command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudo(?: |$)(.*)"))
    async def addsudo(event):
        if event.sender_id == OWNER_ID:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            sudousers = getenv("SUDO_USERS", default=None)

            ok = await event.reply("» __ᴄʜᴀʟ ᴛᴜᴊʜᴇ ᴀɴᴏɴʏᴍᴏᴜs ᴘᴀᴘᴀ ɴᴇ sᴜᴅᴏ ᴅᴇ ᴅɪʏᴀ ᴀꜱ...__")
            target = ""
            if HEROKU_APP_NAME is not None:
                app = Heroku.app(HEROKU_APP_NAME)
            else:
                await ok.edit("`[HEROKU]: Please setup your HEROKU_APP_NAME`")
                return
            heroku_var = app.config()

            try:
                reply_msg = await event.get_reply_message()
                target = reply_msg.sender_id
            except:
                await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ !!")
                return

            if str(target) in sudousers:
                await ok.edit("» ᴀʙᴇ ᴛᴜ ᴘʜᴇʟᴇ sᴇ sᴜᴅᴏ ᴍᴇ ʜᴀɪ !!")
            else:
                if len(sudousers) > 0:
                    newsudo = f"{sudousers} {target}"
                else:
                    newsudo = f"{target}"
                await ok.edit(f"» **ɴᴇᴡ ꜱᴜᴅᴏ ᴜꜱᴇʀ**: `{target}`\n» `ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
                heroku_var["SUDO_USERS"] = newsudo

        elif event.sender_id in SUDO_USERS:
            await event.reply("» ꜱᴏʀʀʏ, ʏᴇ ᴄᴏᴍᴍᴀɴᴅ ʙᴀss ᴛᴇʀᴀ ᴀɴᴏɴʏᴍᴏᴜs ʙᴀᴀᴘ ᴅᴇ sᴋᴛᴀ ʜᴀɪ.")

