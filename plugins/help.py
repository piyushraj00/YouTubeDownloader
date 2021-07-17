from pyrogram import Client, Filters
from aiogram.utils.callback_data import CallbackData

select_lang_cb = CallbackData("select_lang_cb", "help", "back_btn")


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"✏️Enter The YouTube Video Url To Download"
    await message.reply_text(helptxt)
