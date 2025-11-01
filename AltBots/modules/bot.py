import sys
from os import execl, getenv
from telethon import events
from datetime import datetime
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    OWNER_ID, SUDO_USERS, CMD_HNDLR as hl
)

ALL_BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]


# ✅ Ping Command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}ping(?: |$)(.*)"))
    async def ping(e):
        if e.sender_id in SUDO_USERS:
            start = datetime.now()
            reply = await e.reply("» __[𝗔𝗟𝗧𝗥𝗢𝗡] ✘ [ 𝗕𝗢𝗧𝗦 ]__")
            end = datetime.now()
            ms = (end - start).microseconds / 1000
            await reply.edit(f"`🤖 ᴘɪɴɢ\n» 𓆩𝐀𝐒𓆪 ꭙ 𝐉𝐄𝐑𝐑𝐘 ⌯ 𝐊𝐈𝐍𝐆💀 #𝐅𝐔𝐂𝐊𝐄𝐑 ραρα нєяє αв кιѕкι gαи∂ мαяυ {mp} ᴍꜱ`")
        else:
            await e.reply("» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀ sᴜᴅᴏ ᴜsᴇʀ ❌")


# 🔁 Reboot Command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}reboot(?: |$)(.*)"))
    async def reboot(e):
        if e.sender_id in SUDO_USERS:
            await e.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
            await bot.disconnect()
            execl(sys.executable, sys.executable, *sys.argv)
        else:
            await e.reply("» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀ sᴜᴅᴏ ᴜsᴇʀ ❌")


# 🧑‍💻 Add Sudo User
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudo(?: |$)(.*)"))
    async def add_sudo(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ❌")

        ok = await event.reply("» ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ sᴜᴅᴏ ʀᴇǫᴜᴇsᴛ...")

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            return await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴛᴏ ᴀᴅᴅ ᴀs sᴜᴅᴏ !!")

        target = reply_msg.sender_id
        if target in SUDO_USERS:
            return await ok.edit("» ᴜsᴇʀ ᴀʟʀᴇᴀᴅʏ ɪɴ sᴜᴅᴏ ʟɪsᴛ ✅")

        SUDO_USERS.append(int(target))
        await ok.edit(f"» **ɴᴇᴡ sᴜᴅᴏ ᴜsᴇʀ ᴀᴅᴅᴇᴅ:** `{target}` ✅")


# 🚫 Remove Sudo User
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}rmsudo(?: |$)(.*)"))
    async def remove_sudo(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ❌")

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            return await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇᴍ ғʀᴏᴍ sᴜᴅᴏ")

        target = reply_msg.sender_id
        if target not in SUDO_USERS:
            return await event.reply("» ᴜsᴇʀ ɴᴏᴛ ɪɴ sᴜᴅᴏ ʟɪsᴛ ❌")

        SUDO_USERS.remove(int(target))
        await event.reply(f"» **ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ sᴜᴅᴏ:** `{target}` ✅")


# 📜 Show Sudo List
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudolist(?: |$)(.*)"))
    async def sudo_list(event):
        if not SUDO_USERS:
            return await event.reply("» ɴᴏ sᴜᴅᴏ ᴜsᴇʀs ᴀᴅᴅᴇᴅ ʏᴇᴛ ❌")

        text = "» **ᴀᴄᴛɪᴠᴇ sᴜᴅᴏ ᴜsᴇʀs:**\n\n"
        for i, user_id in enumerate(SUDO_USERS, 1):
            text += f"**{i}.** `{user_id}`\n"
        await event.reply(text)
