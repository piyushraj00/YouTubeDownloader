from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"✏️Enter The YouTube Video Url To Download"
    await message.reply_text(helptxt)
