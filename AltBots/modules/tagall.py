from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

@events.register(events.NewMessage(pattern=r"\.tagall"))
async def tag_all_handler(event):
    if not event.is_group:
        return await event.reply("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘ")

    # Optional custom message
    msg = event.text.split(" ", 1)
    if len(msg) > 1:
        message = msg[1]
    else:
        message = "ᴛᴀɢɢɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs"

    mentions = []
    async for user in event.client.iter_participants(event.chat_id):
        if user.bot:
            continue
        mention = f"[{user.first_name}]"
        mentions.append(mention)

    BATCH_SIZE = 20  # number of users to mention per message
    total = len(mentions)
    count = 0

    for i in range(0, total, BATCH_SIZE):
        batch = mentions[i:i+BATCH_SIZE]
        text = f"{message}\n\n" + " ".join(batch)
        try:
            await event.client.send_message(event.chat_id, text)
            count += len(batch)
        except Exception as e:
            print(f"Error: {e}")
        await event.client.loop.run_in_executor(None, lambda: None)

    await event.reply(f"✅ ᴛᴀɢɢᴇᴅ {count} ᴍᴇᴍʙᴇʀs sᴜᴄᴄᴇssғᴜʟʟʏ.")

# Attach handler to all bots
for bot in BOTS:
    bot.add_event_handler(tag_all_handler)
