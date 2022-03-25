#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"𝑴𝒚 𝑵𝒂𝒎𝒆 : <a href='https://t.me/ff_file_share_bot'>Nam-Ra Bot</a>\n\n𝑴𝒚 𝑪𝒓𝒆𝒂𝒕𝒐𝒓 : <a href='tg://user?id={OWNER_ID}'>Naughty Nonsense</a>\n\n𝑶𝒇𝒇𝒊𝒄𝒊𝒂𝒍 𝑮𝒓𝒐𝒖𝒑 : <a href='https://t.me/freakersfilmy'>Freakers Filmy</a>\n\n𝑪𝒉𝒂𝒏𝒏𝒆𝒍 : <a href='https://t.me/freakersmovies'>Freakers Movies</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆 🗑️", callback_data = "close")
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
