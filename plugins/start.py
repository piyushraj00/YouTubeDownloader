from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍀 Service Channel", url="https://t.me/YouTubeVideoDownloaderService")],
        [InlineKeyboardButton(
            "👩‍💻 Owner", url="https://t.me/Piyush0FF")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\nUse /help For Download YouTube Video"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
