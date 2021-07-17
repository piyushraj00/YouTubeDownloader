from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🍀 Service Channel", url="https://t.me/YouTubeVideoDownloaderService")],
        [InlineKeyboardButton(
            "👩‍💻 Owner", url="https://t.me/Piyush0FF")],[InlineKeyboardButton("🚨 Download Videos" , callback_data="/help")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n➡️ Start Video Downloading By Using Download Videos"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
