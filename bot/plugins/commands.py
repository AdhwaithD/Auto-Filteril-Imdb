#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/Mo_Tech_YT"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
            InlineKeyboardButton('𝓐𝓵𝓫𝓮𝓻𝓽 𝓔𝓲𝓷𝓼𝓽𝓮𝓲𝓷 [ᴛɢ]★', url='http://t.me/AlbertEinstein_TG')
            ],[
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019'),
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies'),
            InlineKeyboardButton('🤴 𝙳𝚎𝚟', url='https://t.me/Sanoob_Achu_18')
           ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
            InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019')           
            ],[
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/Sanoob_Achu_18')
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
            InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
            InlineKeyboardButton('♻️ 𝙶𝚛𝚘𝚞𝚙', url='https://t.me/Movies_Club_2019')           
            ],[
            InlineKeyboardButton('⭕️ 𝙲𝚑𝚊𝚗𝚗𝚎𝚕', url='https://t.me/mcnewmovies')
            InlineKeyboardButton('🕵‍♂️ 𝙰𝚗𝚢 𝙳𝚘𝚞𝚋𝚝𝚜 🕵‍♀️', url='http://t.me/Sanoob_Achu_18')
        ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
