#(Ā©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"š“š šµššš : <a href='https://t.me/ff_file_share_bot'>Nam-Ra Bot</a>\n\nš“š šŖšššššš : <a href='tg://user?id={OWNER_ID}'>Naughty Nonsense</a>\n\nš¶ššššššš š®šššš : <a href='https://t.me/freakersfilmy'>Freakers Filmy</a>\n\nšŖšššššš : <a href='https://t.me/freakersmovies'>Freakers Movies</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("šŖšššš šļø", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
